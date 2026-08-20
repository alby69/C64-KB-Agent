"""Markdown document validator for C64-KB-Agent."""

from pathlib import Path
from typing import Any

import yaml
from jsonschema import SchemaError, ValidationError, validate

from c64_kb_agent.config import settings
from c64_kb_agent.validators import load_schema


def parse_frontmatter(file_path: Path) -> tuple[dict[str, Any], str]:
    """Parses YAML frontmatter and body from a Markdown document.

    Performs normalization of `tags` to `topics` if `tags` is specified.
    """
    text = file_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as e:
        raise ValueError(f"YAML frontmatter parse error: {e}") from e

    if isinstance(fm, dict):
        if "tags" in fm and "topics" not in fm:
            fm["topics"] = fm["tags"]
        elif (
            "tags" in fm and isinstance(fm.get("topics"), list) and isinstance(fm.get("tags"), list)
        ):
            for tag in fm["tags"]:
                if tag not in fm["topics"]:
                    fm["topics"].append(tag)

    body = parts[2]
    return fm, body


def get_all_documents(docs_dir: Path | None = None) -> list[Path]:
    """Returns all Markdown document paths (excluding navigation indices)."""
    target_dir = docs_dir or settings.docs_dir
    if not target_dir.exists():
        return []
    return sorted(p for p in target_dir.rglob("*.md") if p.is_file() and p.name != "index.md")


def validate_document(
    doc_path: Path, v1_schema: dict | None = None, v2_schema: dict | None = None
) -> dict[str, Any]:
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

    return fm


def validate_all_documents(
    docs_dir: Path | None = None,
) -> tuple[int, list[tuple[str, str]]]:
    """Validates all documents under docs_dir.

    Returns:
        Tuple of (total_count, list_of_errors_as_tuples(rel_path, error_msg))
    """
    target_dir = docs_dir or settings.docs_dir
    v1_schema = load_schema("document.schema.json")
    v2_path = settings.schemas_dir / "document.schema.v2.json"
    v2_schema = load_schema("document.schema.v2.json") if v2_path.exists() else None

    docs = get_all_documents(target_dir)
    invalid = []

    for doc in docs:
        try:
            validate_document(doc, v1_schema=v1_schema, v2_schema=v2_schema)
        except (ValidationError, SchemaError, ValueError) as e:
            rel_path = (
                str(doc.relative_to(settings.base_dir))
                if doc.is_relative_to(settings.base_dir)
                else str(doc)
            )
            msg = e.message if isinstance(e, ValidationError) else str(e)
            invalid.append((rel_path, msg))

    return len(docs), invalid
