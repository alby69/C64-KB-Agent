"""Dataset JSONL validator for C64-KB-Agent."""

import json
from pathlib import Path

from jsonschema import SchemaError, ValidationError, validate

from c64_kb_agent.config import settings
from c64_kb_agent.validators import load_schema


def validate_dataset_jsonl(
    jsonl_path: Path | None = None,
) -> tuple[int, list[tuple[str, str]]]:
    """Validates records in scraped_dataset.jsonl against dataset.schema.json.

    Returns:
        Tuple of (total_records, list_of_errors_as_tuples(location, error_msg))
    """
    target_path = jsonl_path or (settings.dataset_dir / "scraped_dataset.jsonl")
    if not target_path.is_file():
        return 0, [(str(target_path), "File does not exist")]

    schema = load_schema("dataset.schema.json")
    invalid = []
    total = 0

    with target_path.open(encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            total += 1
            try:
                rec = json.loads(line)
                validate(instance=rec, schema=schema)
            except (json.JSONDecodeError, ValidationError, SchemaError) as e:
                msg = e.message if isinstance(e, ValidationError) else str(e)
                invalid.append((f"Line {line_no}", msg))

    return total, invalid
