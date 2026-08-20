"""Manifest validator for C64-KB-Agent."""

import json
from pathlib import Path

from jsonschema import SchemaError, ValidationError, validate

from c64_kb_agent.config import settings
from c64_kb_agent.validators import load_schema


def validate_manifest(manifest_path: Path | None = None) -> tuple[bool, list[str]]:
    """Validates data/manifest.json against manifest.schema.json.

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    target_path = manifest_path or settings.manifest_path
    if not target_path.is_file():
        return False, [f"Manifest file not found: {target_path}"]

    schema = load_schema("manifest.schema.json")
    try:
        data = json.loads(target_path.read_text(encoding="utf-8"))
        validate(instance=data, schema=schema)
        return True, []
    except (json.JSONDecodeError, ValidationError, SchemaError) as e:
        msg = e.message if isinstance(e, ValidationError) else str(e)
        return False, [msg]
