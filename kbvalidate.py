"""kbvalidate.py — Backwards-compatibility wrapper for c64_kb_agent.validators."""

from jsonschema import ValidationError, validate

from c64_kb_agent.config import settings
from c64_kb_agent.validators import load_schema
from c64_kb_agent.validators.dataset import validate_dataset_jsonl
from c64_kb_agent.validators.document import (
    get_all_documents,
    parse_frontmatter,
    validate_all_documents,
    validate_document,
)

BASE_DIR = settings.base_dir
SCHEMAS_DIR = settings.schemas_dir
DOCS_DIR = settings.docs_dir
DATASET_DIR = settings.dataset_dir

__all__ = [
    "BASE_DIR",
    "SCHEMAS_DIR",
    "DOCS_DIR",
    "DATASET_DIR",
    "load_schema",
    "parse_frontmatter",
    "get_all_documents",
    "validate_document",
    "validate_all_documents",
    "validate_dataset_jsonl",
    "ValidationError",
    "validate",
]
