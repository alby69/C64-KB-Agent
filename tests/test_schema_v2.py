"""Test suite for Schema v2 document validation."""

import pytest
from jsonschema import ValidationError, validate

import kbvalidate


def test_document_schema_v2_valid():
    v2_doc = {
        "schema_version": 2,
        "title": "Test Title v2",
        "source_url": "https://example.com/v2",
        "category": "reference",
        "topics": ["assembly"],
        "tags": ["assembly", "vic-ii"],
        "difficulty": "intermediate",
        "language": "assembly",
        "hardware": ["C64"],
        "related": [],
        "scraped_at": "2026-01-01",
    }
    schema_v2 = kbvalidate.load_schema("document.schema.v2.json")
    validate(instance=v2_doc, schema=schema_v2)


def test_document_schema_v2_invalid_version():
    v2_doc = {
        "schema_version": 1,  # Must be 2 for document.schema.v2.json
        "title": "Test Title v2",
        "source_url": "https://example.com/v2",
        "category": "reference",
        "topics": ["assembly"],
        "difficulty": "intermediate",
        "language": "assembly",
        "hardware": ["C64"],
        "related": [],
        "scraped_at": "2026-01-01",
    }
    schema_v2 = kbvalidate.load_schema("document.schema.v2.json")
    with pytest.raises(ValidationError):
        validate(instance=v2_doc, schema=schema_v2)


def test_kbvalidate_accepts_v2_doc(tmp_path, monkeypatch):
    test_docs = tmp_path / "docs"
    test_docs.mkdir(parents=True)

    v2_file = test_docs / "v2_doc.md"
    v2_file.write_text(
        """---
schema_version: 2
title: "Document v2"
source_url: "https://example.com/doc2"
category: "tutorial"
topics: ["basic"]
tags: ["basic", "intro"]
difficulty: "beginner"
language: "basic"
hardware: ["C64"]
related: []
scraped_at: "2026-02-01"
---
Body text
""",
        encoding="utf-8",
    )

    monkeypatch.setattr(kbvalidate, "DOCS_DIR", test_docs)
    count, errors = kbvalidate.validate_all_documents(test_docs)
    assert count == 1
    assert errors == []
