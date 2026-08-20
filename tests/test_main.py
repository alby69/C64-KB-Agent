"""Test suite for CLI commands in main.py and kbvalidate.py."""

import sqlite3

import kbvalidate
import main


def test_status_command(capsys):
    ret = main.cmd_status()
    assert ret == 0
    captured = capsys.readouterr()
    assert "=== C64-KB-Agent Status ===" in captured.out
    assert "[Documents]" in captured.out
    assert "[Dataset files]" in captured.out
    assert "[Search Index (SQLite FTS5)]" in captured.out


def test_validate_command(capsys):
    ret = main.cmd_validate()
    assert ret == 0
    captured = capsys.readouterr()
    assert "=== Validating C64-KB-Agent Data ===" in captured.out
    assert "Validation Result: PASSED" in captured.out


def test_rebuild_index_command(tmp_path, monkeypatch, capsys):
    # Test rebuild-index using a temporary dataset directory
    test_data = tmp_path / "data"
    test_docs = test_data / "docs"
    test_dataset = test_data / "dataset"
    test_docs.mkdir(parents=True)
    test_dataset.mkdir(parents=True)

    # Create dummy doc
    dummy_doc = test_docs / "test.md"
    dummy_doc.write_text(
        """---
title: "Test Doc"
source_url: "https://example.com/test"
category: "reference"
topics: ["assembly"]
difficulty: "beginner"
language: "assembly"
hardware: ["C64"]
related: []
scraped_at: "2026-01-01"
c64ref:
  symbol: "TEST_SYM"
  address: "$1234"
---
Test body content.
""",
        encoding="utf-8",
    )

    monkeypatch.setattr(main, "DOCS_DIR", test_docs)
    monkeypatch.setattr(main, "DATASET_DIR", test_dataset)
    monkeypatch.setattr(kbvalidate, "DOCS_DIR", test_docs)

    ret = main.cmd_rebuild_index()
    assert ret == 0

    db_file = test_dataset / "search_index.db"
    assert db_file.exists()

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    docs = cursor.execute("SELECT id, title, body FROM documents").fetchall()
    assert len(docs) == 1
    assert docs[0][1] == "Test Doc"
    assert "Test body content." in docs[0][2]

    routines = cursor.execute("SELECT name, address FROM routines").fetchall()
    assert len(routines) == 1
    assert routines[0][0] == "TEST_SYM"
    assert routines[0][1] == "$1234"
    conn.close()


def test_invalid_document_detected(tmp_path, monkeypatch):
    test_docs = tmp_path / "docs"
    test_docs.mkdir(parents=True)

    invalid_doc = test_docs / "invalid.md"
    invalid_doc.write_text(
        """---
title: "Missing category"
---
No category present.
""",
        encoding="utf-8",
    )

    monkeypatch.setattr(kbvalidate, "DOCS_DIR", test_docs)
    count, errors = kbvalidate.validate_all_documents(test_docs)
    assert count == 1
    assert len(errors) == 1
    assert "invalid.md" in errors[0][0]
