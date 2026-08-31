#!/usr/bin/env python3
"""Knowledge base statistics aggregator and METRICS.md generator script.

Part of the C64-KB-Agent quality pipeline (Fase 3).
"""

import json
import sqlite3
from datetime import datetime, timezone

from c64_kb_agent.config import settings


def collect_metrics() -> dict:
    """Collect statistics across Layer 1 raw docs, Layer 2 wiki pages, dataset, and search index."""
    docs_dir = settings.docs_dir
    wiki_dir = settings.wiki_dir
    dataset_dir = settings.dataset_dir
    db_path = settings.db_path

    # Layer 1 raw docs
    raw_doc_files = list(docs_dir.rglob("*.md")) if docs_dir.exists() else []
    raw_doc_count = len([f for f in raw_doc_files if f.name != "index.md"])

    # Breakdown by directory
    docs_breakdown = {}
    if docs_dir.exists():
        for subdir in sorted(p for p in docs_dir.iterdir() if p.is_dir()):
            count = len(list(subdir.rglob("*.md")))
            docs_breakdown[subdir.name] = count

    # Layer 2 wiki pages
    wiki_page_files = list(wiki_dir.rglob("*.md")) if wiki_dir.exists() else []
    wiki_page_count = len([f for f in wiki_page_files if f.name not in ("index.md", "log.md")])

    wiki_breakdown = {}
    if wiki_dir.exists():
        for subdir in sorted(p for p in wiki_dir.iterdir() if p.is_dir()):
            count = len(list(subdir.rglob("*.md")))
            wiki_breakdown[subdir.name] = count

    # Dataset file sizes
    dataset_metrics = {}
    if dataset_dir.exists():
        for p in sorted(dataset_dir.iterdir()):
            if p.is_file():
                dataset_metrics[p.name] = p.stat().st_size

    # Knowledge graph metrics
    kg_nodes = 0
    kg_edges = 0
    kg_file = dataset_dir / "knowledge_graph.json"
    if kg_file.exists():
        try:
            kg_data = json.loads(kg_file.read_text(encoding="utf-8"))
            kg_nodes = len(kg_data.get("nodes", []))
            kg_edges = len(kg_data.get("edges", []))
        except (json.JSONDecodeError, OSError):
            pass

    # Search index metrics
    indexed_doc_count = 0
    if db_path.exists():
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM search_index;")
            row = cursor.fetchone()
            if row:
                indexed_doc_count = row[0]
            conn.close()
        except sqlite3.Error:
            pass

    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "raw_doc_count": raw_doc_count,
        "docs_breakdown": docs_breakdown,
        "wiki_page_count": wiki_page_count,
        "wiki_breakdown": wiki_breakdown,
        "dataset_files": dataset_metrics,
        "kg_nodes": kg_nodes,
        "kg_edges": kg_edges,
        "indexed_doc_count": indexed_doc_count,
    }


def generate_metrics_markdown(metrics: dict) -> str:
    """Format metrics dictionary into Markdown string."""
    docs_breakdown_rows = "\n".join(
        f"| `data/docs/{k}/` | {v:,} |" for k, v in metrics["docs_breakdown"].items()
    )
    wiki_breakdown_rows = "\n".join(
        f"| `data/wiki/{k}/` | {v:,} |" for k, v in metrics["wiki_breakdown"].items()
    )
    dataset_rows = "\n".join(
        f"| `{k}` | {v / 1024:.1f} KB |" for k, v in metrics["dataset_files"].items()
    )

    return f"""# METRICS.md — Knowledge Base Metrics & Index Dashboard

**Last Updated**: {metrics["generated_at"]}

---

## 1. Overview Summary

| Metric | Count |
|---|---|
| **Layer 1 Raw Documents (`data/docs/`)** | {metrics["raw_doc_count"]:,} |
| **Layer 2 Compiled Wiki Pages (`data/wiki/`)** | {metrics["wiki_page_count"]:,} |
| **SQLite FTS5 Indexed Documents** | {metrics["indexed_doc_count"]:,} |
| **Knowledge Graph Entities (Nodes)** | {metrics["kg_nodes"]:,} |
| **Knowledge Graph Relationships (Edges)** | {metrics["kg_edges"]:,} |

---

## 2. Layer 1 Raw Documents Breakdown (`data/docs/`)

| Directory Source | Document Count |
|---|---|
{docs_breakdown_rows or "| *None* | 0 |"}

---

## 3. Layer 2 Compiled Wiki Breakdown (`data/wiki/`)

| Wiki Category | Page Count |
|---|---|
{wiki_breakdown_rows or "| *None* | 0 |"}

---

## 4. Dataset Artifacts (`data/dataset/`)

| Artifact Name | Size |
|---|---|
{dataset_rows or "| *None* | 0 |"}
"""


def main() -> None:
    metrics = collect_metrics()
    content = generate_metrics_markdown(metrics)
    output_path = settings.base_dir / "METRICS.md"
    output_path.write_text(content, encoding="utf-8")
    print(f"Successfully generated METRICS.md at {output_path}")


if __name__ == "__main__":
    main()
