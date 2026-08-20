"""Tests for c64_kb_agent/validators."""

import json
from pathlib import Path

import pytest
from jsonschema import ValidationError

from c64_kb_agent.validators import load_schema
from c64_kb_agent.validators.dataset import validate_dataset_jsonl
from c64_kb_agent.validators.document import (
    parse_frontmatter,
    validate_document,
)
from c64_kb_agent.validators.graph_and_api import (
    validate_api_index,
    validate_cross_references,
    validate_knowledge_graph,
)
from c64_kb_agent.validators.manifest import validate_manifest


def test_load_schema():
    schema = load_schema("document.schema.json")
    assert schema["title"] == "C64 Knowledge Document"


def test_parse_frontmatter_tags_normalization(tmp_path):
    doc_path = tmp_path / "test_tags.md"
    doc_path.write_text(
        """---
title: "Test Tags"
tags: ["tag1", "tag2"]
---
Body text here.
""",
        encoding="utf-8",
    )

    fm, body = parse_frontmatter(doc_path)
    assert fm["title"] == "Test Tags"
    assert "topics" in fm
    assert fm["topics"] == ["tag1", "tag2"]
    assert body.strip() == "Body text here."


def test_parse_frontmatter_invalid_yaml(tmp_path):
    doc_path = tmp_path / "invalid_yaml.md"
    doc_path.write_text(
        """---
title: : invalid yaml syntax
---
Body
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        parse_frontmatter(doc_path)


def test_validate_document_unsupported_version(tmp_path):
    doc_path = tmp_path / "unsupported_ver.md"
    doc_path.write_text(
        """---
schema_version: 99
title: "Invalid Version"
---
Body
""",
        encoding="utf-8",
    )

    with pytest.raises(ValidationError):
        validate_document(doc_path)


def test_validate_dataset_nonexistent():
    total, errors = validate_dataset_jsonl(Path("/nonexistent/file.jsonl"))
    assert total == 0
    assert len(errors) == 1


def test_validate_manifest_nonexistent():
    ok, errors = validate_manifest(Path("/nonexistent/manifest.json"))
    assert not ok
    assert len(errors) == 1


def test_validate_graph_and_api_nonexistent():
    kg_ok, _ = validate_knowledge_graph(Path("/nonexistent/kg.json"))
    assert kg_ok
    api_ok, _ = validate_api_index(Path("/nonexistent/api.json"))
    assert api_ok


def test_validate_cross_references(tmp_path):
    docs_dir = tmp_path / "docs"
    dataset_dir = tmp_path / "dataset"
    docs_dir.mkdir()
    dataset_dir.mkdir()

    (docs_dir / "valid.md").write_text(
        """---
id: "doc1"
title: "Doc 1"
---
Body
""",
        encoding="utf-8",
    )

    api_file = dataset_dir / "api_index.json"
    api_file.write_text(
        json.dumps(
            [{"filepath": "nonexistent.md", "doc_id": "missing_doc", "title": "Bad Reference"}]
        ),
        encoding="utf-8",
    )

    errors = validate_cross_references(docs_dir=docs_dir, dataset_dir=dataset_dir)
    assert len(errors) >= 1
