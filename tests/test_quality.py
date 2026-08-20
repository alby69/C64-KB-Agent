"""Tests for c64_kb_agent/quality.py."""

from c64_kb_agent.quality import analyze_data_quality


def test_quality_analysis(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()

    (docs_dir / "empty.md").write_text("""---
title: "Empty"
---
""", encoding="utf-8")

    (docs_dir / "dup1.md").write_text("""---
title: "Dup 1"
source_url: "https://example.com/same"
---
Duplicate content body.
""", encoding="utf-8")

    (docs_dir / "dup2.md").write_text("""---
title: "Dup 2"
source_url: "https://example.com/same"
---
Duplicate content body.
""", encoding="utf-8")

    report = analyze_data_quality(docs_dir=docs_dir)

    assert report["total_documents"] == 3
    assert report["empty_body_count"] == 1
    assert report["duplicate_urls_count"] == 1
    assert report["duplicate_content_count"] == 1
