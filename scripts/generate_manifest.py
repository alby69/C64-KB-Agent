#!/usr/bin/env python3
"""scripts/generate_manifest.py — Generates data/manifest.json according to manifest schema."""

import datetime
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any

from c64_kb_agent.config import settings
from c64_kb_agent.validators.document import get_all_documents, parse_frontmatter
from c64_kb_agent.validators.manifest import validate_manifest


def compute_sha256(file_path: Path) -> str:
    """Computes SHA256 checksum of a file."""
    sha256 = hashlib.sha256()
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def generate_manifest() -> dict[str, Any]:
    """Collects metadata and returns the manifest dictionary."""
    doc_paths = get_all_documents(settings.docs_dir)

    by_source: dict[str, int] = {}
    doc_checksums: dict[str, str] = {}
    schema_distribution: dict[str, int] = {}

    for doc in doc_paths:
        rel_str = (
            str(doc.relative_to(settings.docs_dir))
            if doc.is_relative_to(settings.docs_dir)
            else str(doc)
        )
        source = rel_str.split(os.sep)[0] if os.sep in rel_str else "root"
        by_source[source] = by_source.get(source, 0) + 1

        doc_checksums[rel_str] = compute_sha256(doc)

        try:
            fm, _ = parse_frontmatter(doc)
            ver_str = f"v{fm.get('schema_version', 1)}"
        except Exception:
            ver_str = "v1"
        schema_distribution[ver_str] = schema_distribution.get(ver_str, 0) + 1

    dataset_files_info: dict[str, Any] = {}
    target_files = ["scraped_dataset.jsonl", "api_index.json", "knowledge_graph.json"]
    for fname in target_files:
        fpath = settings.dataset_dir / fname
        if fpath.is_file():
            dataset_files_info[fname] = {
                "size_bytes": fpath.stat().st_size,
                "sha256": compute_sha256(fpath),
            }

    manifest_data: dict[str, Any] = {
        "schema_version": 1,
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "documents": {
            "total": len(doc_paths),
            "by_source": by_source,
            "schema_versions_distribution": schema_distribution,
            "document_checksums": doc_checksums,
        },
        "dataset_files": dataset_files_info,
    }

    producer_commit = os.environ.get("SCRAPY_COMMIT") or os.environ.get("PRODUCER_COMMIT")
    if producer_commit:
        manifest_data["producer"] = {"name": "C64-Scrapy", "commit": producer_commit}

    return manifest_data


def main() -> None:
    manifest = generate_manifest()
    settings.manifest_path.parent.mkdir(parents=True, exist_ok=True)
    settings.manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    is_valid, errors = validate_manifest(settings.manifest_path)
    if not is_valid:
        print(f"ERROR: Generated manifest failed validation: {errors}", file=sys.stderr)
        sys.exit(1)

    print(f"Generated and validated manifest at {settings.manifest_path}")


if __name__ == "__main__":
    main()
