"""Tests for semantic linting and auto-synthesis enhancements."""

from c64_kb_agent.engine.ingestor import WikiIngestor
from c64_kb_agent.engine.linter import WikiLinter
from c64_kb_agent.engine.synthesizer import WikiSynthesizer


def test_auto_synthesize_topics(tmp_path):
    wiki_dir = tmp_path / "wiki"
    doc1 = tmp_path / "c64ref" / "io-map" / "doc1.md"
    doc1.parent.mkdir(parents=True, exist_ok=True)
    doc1.write_text("---\ntitle: \"Doc 1\"\ntags: [graphics, raster]\n---\n# Doc 1\n", encoding="utf-8")

    ingestor = WikiIngestor(wiki_dir=wiki_dir)
    ingestor.ingest_document(doc1)

    synth = WikiSynthesizer(wiki_dir=wiki_dir)
    topics = synth.auto_synthesize_topics()

    assert len(topics) >= 1
    assert any("topic-graphics" in str(t) or "topic-raster" in str(t) for t in topics)


def test_semantic_linter_hex_warning(tmp_path):
    wiki_dir = tmp_path / "wiki"
    (wiki_dir / "entities").mkdir(parents=True, exist_ok=True)
    page = wiki_dir / "entities" / "test-hex.md"
    page.write_text(
        "---\nid: \"test-hex\"\ntype: \"entity\"\ntitle: \"Test Hex\"\naliases: []\ntags: []\nsources: []\ncreated_at: \"2026-08-26\"\nupdated_at: \"2026-08-26\"\nstatus: \"stable\"\ncontradictions: []\nlinks_out: []\n---\n\nAddress is 0xD020.\n",
        encoding="utf-8"
    )

    linter = WikiLinter(wiki_dir=wiki_dir)
    report = linter.lint_wiki()

    assert len(report["hex_formatting_warnings"]) == 1
    assert "0xD020" in report["hex_formatting_warnings"][0]["warning"]
