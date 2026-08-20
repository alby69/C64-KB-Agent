"""Tests for c64_kb_agent/search/fts5.py and db.py."""

from c64_kb_agent.db import DatabaseDAO
from c64_kb_agent.search.fts5 import FTSSearchEngine


def test_database_dao_and_fts_search(tmp_path):
    docs_dir = tmp_path / "docs"
    dataset_dir = tmp_path / "dataset"
    docs_dir.mkdir()
    dataset_dir.mkdir()

    (docs_dir / "sprite_test.md").write_text(
        """---
id: "sprite_test_01"
title: "Sprite Test Guide"
category: "reference"
difficulty: "beginner"
language: "assembly"
hardware: ["VIC-II"]
topics: ["sprite programming", "assembly"]
source_url: "https://example.com/sprite"
c64ref:
  symbol: "SPRITE_INIT"
  address: "$D015"
---
This document explains sprite collision and VIC-II registers for Commodore 64.
""",
        encoding="utf-8",
    )

    db_path = dataset_dir / "search_index.db"
    dao = DatabaseDAO(db_path=db_path)
    indexed_docs, indexed_routines = dao.rebuild_index(docs_dir=docs_dir)

    assert indexed_docs == 1
    assert indexed_routines == 1

    status = dao.get_status()
    assert status["exists"]
    assert status["indexed_documents"] == 1

    engine = FTSSearchEngine(dao=dao)
    results = engine.search(query="sprite", category="reference", language="assembly")

    assert results["total"] == 1
    assert results["results"][0]["id"] == "sprite_test_01"
    assert "<b>sprite</b>" in results["results"][0]["snippet"]
