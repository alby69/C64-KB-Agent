"""Knowledge graph, API index, and cross-dataset validators for C64-KB-Agent."""

import json
from pathlib import Path

from jsonschema import SchemaError, ValidationError, validate

from c64_kb_agent.config import settings
from c64_kb_agent.validators import load_schema
from c64_kb_agent.validators.document import get_all_documents, parse_frontmatter


def validate_knowledge_graph(path: Path | None = None) -> tuple[bool, list[str]]:
    """Validates data/dataset/knowledge_graph.json against schema."""
    target = path or (settings.dataset_dir / "knowledge_graph.json")
    if not target.is_file():
        return True, []

    schema = load_schema("knowledge_graph.schema.json")
    try:
        data = json.loads(target.read_text(encoding="utf-8"))
        validate(instance=data, schema=schema)
        return True, []
    except (json.JSONDecodeError, ValidationError, SchemaError) as e:
        msg = e.message if isinstance(e, ValidationError) else str(e)
        return False, [msg]


def validate_api_index(path: Path | None = None) -> tuple[bool, list[str]]:
    """Validates data/dataset/api_index.json against schema."""
    target = path or (settings.dataset_dir / "api_index.json")
    if not target.is_file():
        return True, []

    schema = load_schema("api_index.schema.json")
    try:
        data = json.loads(target.read_text(encoding="utf-8"))
        validate(instance=data, schema=schema)
        return True, []
    except (json.JSONDecodeError, ValidationError, SchemaError) as e:
        msg = e.message if isinstance(e, ValidationError) else str(e)
        return False, [msg]


def validate_cross_references(
    docs_dir: Path | None = None, dataset_dir: Path | None = None
) -> list[str]:
    """Cross-validates document IDs and filepaths across dataset files and markdown docs."""
    target_docs = docs_dir or settings.docs_dir
    target_dataset = dataset_dir or settings.dataset_dir
    errors = []

    doc_paths = get_all_documents(target_docs)
    doc_ids: set[str] = set()
    doc_rel_paths: set[str] = set()

    for p in doc_paths:
        try:
            rel = str(p.relative_to(target_docs))
            doc_rel_paths.add(rel)
            fm, _ = parse_frontmatter(p)
            doc_id = fm.get("id") or rel
            doc_ids.add(doc_id)
        except Exception:
            pass

    api_path = target_dataset / "api_index.json"
    if api_path.is_file():
        try:
            entries = json.loads(api_path.read_text(encoding="utf-8"))
            if isinstance(entries, list):
                for idx, entry in enumerate(entries):
                    fp = entry.get("filepath")
                    if fp and fp not in doc_rel_paths and not (target_docs / fp).is_file():
                        errors.append(
                            f"api_index.json entry {idx} ('{entry.get('title')}') references non-existent filepath: {fp}"
                        )
                    doc_id = entry.get("doc_id")
                    if doc_id and doc_id not in doc_ids:
                        errors.append(
                            f"api_index.json entry {idx} references non-existent doc_id: {doc_id}"
                        )
        except Exception as e:
            errors.append(f"Error reading api_index.json for cross-validation: {e}")

    jsonl_path = target_dataset / "scraped_dataset.jsonl"
    if jsonl_path.is_file():
        try:
            with jsonl_path.open(encoding="utf-8") as fh:
                for line_no, line in enumerate(fh, 1):
                    line = line.strip()
                    if not line:
                        continue
                    rec = json.loads(line)
                    rec_id = rec.get("id")
                    meta = rec.get("metadata", {})
                    rel_p = meta.get("filepath")
                    if rel_p and rel_p not in doc_rel_paths and not (target_docs / rel_p).is_file():
                        errors.append(
                            f"scraped_dataset.jsonl line {line_no} (id: {rec_id}) references missing filepath: {rel_p}"
                        )
        except Exception as e:
            errors.append(f"Error reading scraped_dataset.jsonl for cross-validation: {e}")

    return errors
