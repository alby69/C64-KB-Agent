#!/usr/bin/env python3
"""scripts/generate_manifest.py — Generates data/manifest.json according to schemas/manifest.schema.json."""

import datetime
import hashlib
import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "data" / "docs"
DATASET_DIR = BASE_DIR / "data" / "dataset"
MANIFEST_PATH = BASE_DIR / "data" / "manifest.json"


def compute_sha256(file_path: Path) -> str:
    """Computes SHA256 checksum of a file."""
    sha256 = hashlib.sha256()
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def generate_manifest() -> dict:
    """Collects metadata and returns the manifest dictionary."""
    # Count documents
    doc_paths = sorted(
        p for p in DOCS_DIR.rglob("*.md")
        if p.is_file() and p.name != "index.md"
    ) if DOCS_DIR.exists() else []

    by_source = {}
    for doc in doc_paths:
        rel = doc.relative_to(DOCS_DIR)
        source = rel.parts[0] if len(rel.parts) > 1 else "root"
        by_source[source] = by_source.get(source, 0) + 1

    # Process dataset files
    dataset_files_info = {}
    target_files = ["scraped_dataset.jsonl", "api_index.json", "knowledge_graph.json"]
    for fname in target_files:
        fpath = DATASET_DIR / fname
        if fpath.is_file():
            dataset_files_info[fname] = {
                "size_bytes": fpath.stat().st_size,
                "sha256": compute_sha256(fpath)
            }

    manifest_data = {
        "schema_version": 1,
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "documents": {
            "total": len(doc_paths),
            "by_source": by_source
        },
        "dataset_files": dataset_files_info
    }

    # Optional producer commit info from environment
    producer_commit = os.environ.get("SCRAPY_COMMIT") or os.environ.get("PRODUCER_COMMIT")
    if producer_commit:
        manifest_data["producer"] = {
            "name": "C64-Scrapy",
            "commit": producer_commit
        }

    return manifest_data


def main():
    manifest = generate_manifest()
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Generated manifest at {MANIFEST_PATH.relative_to(BASE_DIR)}")


if __name__ == "__main__":
    main()
