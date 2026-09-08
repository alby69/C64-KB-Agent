"""Tests for c64_kb_agent/search/fts5.py and db.py."""

from c64_kb_agent.db import DatabaseDAO
from c64_kb_agent.engine.indexer import WikiIndexer
from c64_kb_agent.engine.ingestor import WikiIngestor
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


def test_cross_layer_search(tmp_path):
    docs_dir = tmp_path / "docs"
    wiki_dir = tmp_path / "wiki"
    dataset_dir = tmp_path / "dataset"
    docs_dir.mkdir()
    wiki_dir.mkdir()
    dataset_dir.mkdir()

    sample_doc = docs_dir / "c64ref" / "vic-ii.md"
    sample_doc.parent.mkdir(parents=True, exist_ok=True)
    sample_doc.write_text(
        """---
title: "VIC Controller"
tags: ["hardware"]
---
VIC Controller Chip details and registers $D000-$D02E.
""",
        encoding="utf-8",
    )

    ingestor = WikiIngestor(wiki_dir=wiki_dir, docs_dir=docs_dir)
    ingestor.ingest_document(sample_doc)

    db_path = dataset_dir / "search_index.db"
    dao = DatabaseDAO(db_path=db_path)

    indexer = WikiIndexer(db_dao=dao, wiki_dir=wiki_dir, docs_dir=docs_dir)
    total_indexed = indexer.rebuild_fts_index_with_wiki()

    assert total_indexed >= 2

    status = dao.get_status()
    assert status["indexed_documents"] == 1
    assert status["indexed_wiki_pages"] >= 2

    engine = FTSSearchEngine(dao=dao)

    res_all = engine.search(query="Controller", layer="all")
    assert res_all["total"] >= 2

    res_wiki = engine.search(query="Controller", layer="wiki")
    assert res_wiki["total"] >= 1
    assert all(r["source_layer"] == "wiki" for r in res_wiki["results"])

    res_docs = engine.search(query="Controller", layer="docs")
    assert res_docs["total"] >= 1
    assert all(r["source_layer"] == "docs" for r in res_docs["results"])
