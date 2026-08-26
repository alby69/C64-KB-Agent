"""Unit tests for schemas/wiki_page.schema.json validation."""

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, validate
from jsonschema.exceptions import ValidationError

WIKI_SCHEMA_PATH = Path("schemas/wiki_page.schema.json")


def load_wiki_schema():
    with open(WIKI_SCHEMA_PATH, encoding="utf-8") as f:
        return json.load(f)


def test_wiki_schema_is_valid_json_schema():
    schema = load_wiki_schema()
    Draft202012Validator.check_schema(schema)


def test_valid_wiki_page_frontmatter():
    schema = load_wiki_schema()
    valid_data = {
        "id": "sid-6581",
        "type": "entity",
        "title": "SID 6581 — Sound Interface Device",
        "aliases": ["SID", "6581"],
        "tags": ["audio", "hardware", "chip"],
        "sources": [
            {
                "path": "data/docs/c64ref/io-map/sid/d400.md",
                "sha256": "a" * 64,
            }
        ],
        "created_at": "2026-08-26",
        "updated_at": "2026-08-26",
        "status": "stable",
        "contradictions": [],
        "links_out": ["vic-ii", "cia-6526"],
    }
    validate(instance=valid_data, schema=schema)


def test_invalid_wiki_page_frontmatter_missing_required():
    schema = load_wiki_schema()
    invalid_data = {
        "id": "sid-6581",
        "type": "entity",
        "title": "SID 6581",
    }
    with pytest.raises(ValidationError):
        validate(instance=invalid_data, schema=schema)


def test_invalid_wiki_page_frontmatter_bad_id_pattern():
    schema = load_wiki_schema()
    invalid_data = {
        "id": "SID_6581_Invalid",
        "type": "entity",
        "title": "SID 6581",
        "aliases": [],
        "tags": [],
        "sources": [],
        "created_at": "2026-08-26",
        "updated_at": "2026-08-26",
        "status": "stable",
        "contradictions": [],
        "links_out": [],
    }
    with pytest.raises(ValidationError):
        validate(instance=invalid_data, schema=schema)
