"""Comprehensive unit and integration tests for C64 LLM-Wiki Engine modules."""

import json

import pytest

from c64_kb_agent.db import DatabaseDAO
from c64_kb_agent.engine.cli import handle_engine_cli
from c64_kb_agent.engine.indexer import WikiIndexer
from c64_kb_agent.engine.ingestor import WikiIngestor, compute_sha256, slugify
from c64_kb_agent.engine.linker import WikiLinker
from c64_kb_agent.engine.linter import WikiLinter
from c64_kb_agent.engine.synthesizer import WikiSynthesizer


@pytest.fixture
def temp_wiki_dir(tmp_path):
    wiki_dir = tmp_path / "wiki"
    for sub in ["entities", "concepts", "topics", "sources", "synthesis", "code"]:
        (wiki_dir / sub).mkdir(parents=True, exist_ok=True)
    return wiki_dir


@pytest.fixture
def sample_doc(tmp_path):
    doc_path = tmp_path / "data" / "docs" / "c64ref" / "test-doc.md"
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    content = """---
title: "Test SID Register"
tags: ["hardware", "audio"]
---

# Test SID Register ($D400)

This register controls Voice 1 Frequency Low Byte [[vic-ii]].
See also [[sid-6581]].
"""
    doc_path.write_text(content, encoding="utf-8")
    return doc_path


def test_slugify_and_sha256(sample_doc):
    assert slugify("SID 6581 — Sound Chip!") == "sid-6581-sound-chip"
    sha = compute_sha256(sample_doc)
    assert len(sha) == 64


def test_ingestor_flow(temp_wiki_dir, sample_doc):
    ingestor = WikiIngestor(wiki_dir=temp_wiki_dir, docs_dir=sample_doc.parent)
    created = ingestor.ingest_document(sample_doc)

    assert len(created) == 2  # 1 source summary + 1 entity page
    source_page = temp_wiki_dir / "sources" / "src-test-doc.md"
    entity_page = temp_wiki_dir / "entities" / "test-doc.md"
    assert source_page.exists()
    assert entity_page.exists()


def test_linker_flow(temp_wiki_dir, sample_doc):
    ingestor = WikiIngestor(wiki_dir=temp_wiki_dir)
    ingestor.ingest_document(sample_doc)

    linker = WikiLinker(wiki_dir=temp_wiki_dir)
    res = linker.link_all_pages()

    assert res["pages_processed"] >= 2
    assert res["total_links"] >= 2


def test_synthesizer_flow(temp_wiki_dir, sample_doc):
    ingestor = WikiIngestor(wiki_dir=temp_wiki_dir)
    ingestor.ingest_document(sample_doc)

    synth = WikiSynthesizer(wiki_dir=temp_wiki_dir)
    topic_path = synth.update_topic_page("Audio Hardware", ["test-doc"])
    index_path = synth.rebuild_index()

    assert topic_path.exists()
    assert index_path.exists()
    index_text = index_path.read_text(encoding="utf-8")
    assert "Sources (1)" in index_text or "Entities (1)" in index_text


def test_linter_flow(temp_wiki_dir, sample_doc):
    ingestor = WikiIngestor(wiki_dir=temp_wiki_dir)
    ingestor.ingest_document(sample_doc)

    linker = WikiLinker(wiki_dir=temp_wiki_dir)
    linker.link_all_pages()

    linter = WikiLinter(wiki_dir=temp_wiki_dir)
    report = linter.lint_wiki()

    assert report["total_pages_scanned"] >= 2
    assert len(report["invalid_schema"]) == 0


def test_indexer_flow(temp_wiki_dir, sample_doc, tmp_path):
    ingestor = WikiIngestor(wiki_dir=temp_wiki_dir)
    ingestor.ingest_document(sample_doc)

    db_path = tmp_path / "search_index.db"
    dao = DatabaseDAO(db_path=db_path)

    indexer = WikiIndexer(db_dao=dao, wiki_dir=temp_wiki_dir)
    indexed_count = indexer.rebuild_fts_index_with_wiki()
    assert indexed_count >= 2


def test_engine_cli_commands(temp_wiki_dir, sample_doc, capsys):
    ingestor = WikiIngestor(wiki_dir=temp_wiki_dir)
    ingestor.ingest_document(sample_doc)

    class Args:
        wiki_command = "lint"
        format = "json"

    ret = handle_engine_cli(Args())
    assert ret == 0
    captured = capsys.readouterr()
    json_start = captured.out.find("{")
    assert json_start != -1
    data = json.loads(captured.out[json_start:])
    assert "total_pages_scanned" in data
