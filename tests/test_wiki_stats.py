"""Unit tests for scripts/wiki_stats.py."""

from scripts.wiki_stats import collect_metrics, generate_metrics_markdown


def test_collect_metrics() -> None:
    metrics = collect_metrics()
    assert "generated_at" in metrics
    assert "raw_doc_count" in metrics
    assert "wiki_page_count" in metrics
    assert "docs_breakdown" in metrics
    assert "wiki_breakdown" in metrics
    assert "indexed_doc_count" in metrics


def test_generate_metrics_markdown() -> None:
    metrics = {
        "generated_at": "2026-08-26 12:00:00 UTC",
        "raw_doc_count": 1878,
        "docs_breakdown": {"c64ref": 1112, "codebase_c64_org": 436},
        "wiki_page_count": 42,
        "wiki_breakdown": {"entities": 20, "concepts": 22},
        "dataset_files": {"scraped_dataset.jsonl": 102400},
        "kg_nodes": 150,
        "kg_edges": 300,
        "indexed_doc_count": 1878,
    }

    md = generate_metrics_markdown(metrics)
    assert "# METRICS.md" in md
    assert "1,878" in md
    assert "c64ref" in md
    assert "scraped_dataset.jsonl" in md
