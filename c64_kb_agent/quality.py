"""Data quality and deduplication analyzer for C64-KB-Agent."""

import hashlib
from pathlib import Path
from typing import Any

from c64_kb_agent.config import settings
from c64_kb_agent.validators.document import get_all_documents, parse_frontmatter


def analyze_data_quality(docs_dir: Path | None = None) -> dict[str, Any]:
    """Analyzes data quality across markdown documents.

    Returns a report dictionary containing metrics and issues found.
    """
    target_docs = docs_dir or settings.docs_dir
    doc_paths = get_all_documents(target_docs)

    total_docs = len(doc_paths)
    empty_body_docs: list[str] = []
    malformed_frontmatter_docs: list[str] = []

    seen_ids: dict[str, list[str]] = {}
    seen_urls: dict[str, list[str]] = {}
    seen_content_hashes: dict[str, list[str]] = {}

    for p in doc_paths:
        rel_path = (
            str(p.relative_to(settings.base_dir)) if p.is_relative_to(settings.base_dir) else str(p)
        )
        try:
            fm, body = parse_frontmatter(p)
        except Exception:
            malformed_frontmatter_docs.append(rel_path)
            continue

        if not body.strip():
            empty_body_docs.append(rel_path)

        doc_id = fm.get("id") or (
            str(p.relative_to(target_docs)) if p.is_relative_to(target_docs) else str(p)
        )
        seen_ids.setdefault(doc_id, []).append(rel_path)

        url = fm.get("source_url")
        if url:
            seen_urls.setdefault(url, []).append(rel_path)

        content_hash = hashlib.sha256(body.strip().encode("utf-8")).hexdigest()
        seen_content_hashes.setdefault(content_hash, []).append(rel_path)

    duplicate_ids = {doc_id: paths for doc_id, paths in seen_ids.items() if len(paths) > 1}
    duplicate_urls = {url: paths for url, paths in seen_urls.items() if len(paths) > 1}
    duplicate_content = {
        chash: paths for chash, paths in seen_content_hashes.items() if len(paths) > 1
    }

    return {
        "total_documents": total_docs,
        "empty_body_count": len(empty_body_docs),
        "malformed_frontmatter_count": len(malformed_frontmatter_docs),
        "duplicate_ids_count": len(duplicate_ids),
        "duplicate_urls_count": len(duplicate_urls),
        "duplicate_content_count": len(duplicate_content),
        "issues": {
            "empty_bodies": empty_body_docs,
            "malformed_frontmatters": malformed_frontmatter_docs,
            "duplicate_ids": duplicate_ids,
            "duplicate_urls": duplicate_urls,
            "duplicate_content": duplicate_content,
        },
    }
