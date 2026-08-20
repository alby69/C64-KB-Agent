"""Validators package for C64-KB-Agent."""

import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict

from c64_kb_agent.config import settings


@lru_cache(maxsize=32)
def load_schema(schema_name: str) -> dict[str, Any]:
    """Loads a JSON schema from the schemas directory with in-memory caching."""
    schema_path = settings.schemas_dir / schema_name
    if not schema_path.is_file():
        raise FileNotFoundError(f"Schema file not found: {schema_path}")
    return json.loads(schema_path.read_text(encoding="utf-8"))
