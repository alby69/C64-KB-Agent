"""kbvalidate.py — Modular dataset and document validation logic for C64-KB-Agent.

Used by main.py CLI and test suites to validate Markdown documents and JSONL
datasets against contract JSON schemas.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Tuple, Any

import yaml
import jsonschema
from jsonschema import validate, ValidationError


BASE_DIR = Path(__file__).resolve().parent
SCHEMAS_DIR = BASE_DIR / "schemas"
DOCS_DIR = BASE_DIR / "data" / "docs"
DATASET_DIR = BASE_DIR / "data" / "dataset"


def load_schema(schema_name: str) -> dict:
    """Loads a JSON schema from the schemas directory."""
    schema_path = SCHEMAS_DIR / schema_name
    if not schema_path.is_file():
        raise FileNotFoundError(f"Schema file not found: {schema_path}")
    return json.loads(schema_path.read_text(encoding="utf-8"))


def parse_frontmatter(file_path: Path) -> Tuple[dict, str]:
    """Parses YAML frontmatter and body from a Markdown document."""
    text = file_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm = yaml.safe_load(parts[1]) or {}
    body = parts[2]
    return fm, body


def get_all_documents(docs_dir: Path = DOCS_DIR) -> List[Path]:
    """Returns all Markdown document paths (excluding navigation indices)."""
    if not docs_dir.exists():
        return []
    return sorted(
        p for p in docs_dir.rglob("*.md")
        if p.is_file() and p.name != "index.md"
    )


def validate_document(
    doc_path: Path,
    v1_schema: dict = None,
    v2_schema: dict = None
) -> None:
    """Validates a single document against v1 or v2 document schema."""
    if v1_schema is None:
        v1_schema = load_schema("document.schema.json")

    fm, _ = parse_frontmatter(doc_path)
    version = fm.get("schema_version", 1)

    if version == 1:
        validate(instance=fm, schema=v1_schema)
    elif version == 2:
        if v2_schema is None:
            v2_schema = load_schema("document.schema.v2.json")
        validate(instance=fm, schema=v2_schema)
    else:
        raise ValidationError(f"Unsupported schema_version: {version}")


def validate_all_documents(
    docs_dir: Path = DOCS_DIR
) -> Tuple[int, List[Tuple[str, str]]]:
    """Validates all documents under docs_dir.

    Returns:
        Tuple of (total_count, list_of_errors_as_tuples(rel_path, error_msg))
    """
    v1_schema = load_schema("document.schema.json")
    v2_path = SCHEMAS_DIR / "document.schema.v2.json"
    v2_schema = load_schema("document.schema.v2.json") if v2_path.exists() else None

    docs = get_all_documents(docs_dir)
    invalid = []

    for doc in docs:
        try:
            validate_document(doc, v1_schema=v1_schema, v2_schema=v2_schema)
        except (ValidationError, jsonschema.SchemaError, Exception) as e:
            rel_path = str(doc.relative_to(BASE_DIR)) if doc.is_relative_to(BASE_DIR) else str(doc)
            msg = e.message if isinstance(e, ValidationError) else str(e)
            invalid.append((rel_path, msg))

    return len(docs), invalid


def validate_dataset_jsonl(
    jsonl_path: Path = DATASET_DIR / "scraped_dataset.jsonl"
) -> Tuple[int, List[Tuple[str, str]]]:
    """Validates records in scraped_dataset.jsonl against dataset.schema.json.

    Returns:
        Tuple of (total_records, list_of_errors)
    """
    if not jsonl_path.is_file():
        return 0, [("scraped_dataset.jsonl", "File does not exist")]

    schema = load_schema("dataset.schema.json")
    invalid = []
    total = 0

    with jsonl_path.open(encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            total += 1
            try:
                rec = json.loads(line)
                validate(instance=rec, schema=schema)
            except (json.JSONDecodeError, ValidationError) as e:
                msg = e.message if isinstance(e, ValidationError) else str(e)
                invalid.append((f"Line {line_no}", msg))

    return total, invalid
