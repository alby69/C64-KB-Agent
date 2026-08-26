"""Ingestion engine for C64 LLM-Wiki.

Ingests Layer 1 raw Markdown files (from data/docs/) into compiled Layer 2 wiki pages
(under data/wiki/) while maintaining complete traceability, strict schema validation,
and conflict detection without modifying Layer 1 data.
"""

import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from jsonschema import validate

from c64_kb_agent.config import settings


def compute_sha256(filepath: Path) -> str:
    """Computes SHA256 checksum of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def slugify(text: str) -> str:
    """Converts string into lower-kebab-case slug identifier."""
    slug = text.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "unnamed"


def load_yaml_frontmatter(file_path: Path) -> tuple[dict[str, Any], str]:
    """Parses YAML frontmatter and body from Markdown file."""
    content = file_path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, parts[2]


def write_wiki_page(filepath: Path, frontmatter: dict[str, Any], body: str) -> None:
    """Writes a wiki page file with formatted YAML frontmatter and Markdown body."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    yaml_str = yaml.safe_dump(
        frontmatter, sort_keys=False, allow_unicode=True, default_flow_style=False
    )
    content = f"---\n{yaml_str}---\n\n{body.strip()}\n"
    filepath.write_text(content, encoding="utf-8")


class WikiIngestor:
    """Ingestion engine compiling Layer 1 raw docs into Layer 2 Wiki pages."""

    def __init__(self, wiki_dir: Path | None = None, docs_dir: Path | None = None) -> None:
        self.wiki_dir = wiki_dir or (settings.base_dir / "data" / "wiki")
        self.docs_dir = docs_dir or settings.docs_dir
        self.schema_path = settings.schemas_dir / "wiki_page.schema.json"
        self.schema = self._load_schema()

    def _load_schema(self) -> dict[str, Any]:
        with open(self.schema_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return dict(data) if isinstance(data, dict) else {}

    def log_operation(self, entry: str) -> None:
        """Appends a log entry to data/wiki/log.md."""
        log_path = self.wiki_dir / "log.md"
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        log_entry = f"\n## [{today}] ingest | {entry}\n"
        if not log_path.exists():
            log_path.write_text(
                "# C64 LLM-Wiki Log\n\nAppend-only chronological operation log.\n\n---\n"
            )
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(log_entry)

    def ingest_document(self, doc_path: Path) -> list[Path]:
        """Ingests a single Layer 1 document into Layer 2 Wiki pages.

        Returns list of created/updated wiki page paths.
        """
        if not doc_path.exists():
            raise FileNotFoundError(f"Document not found: {doc_path}")

        rel_doc_path = (
            str(doc_path.relative_to(settings.base_dir))
            if doc_path.is_relative_to(settings.base_dir)
            else str(doc_path)
        )
        sha256 = compute_sha256(doc_path)
        fm, body = load_yaml_frontmatter(doc_path)

        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        title = fm.get("title") or doc_path.stem.replace("-", " ").title()
        doc_id = slugify(doc_path.stem)
        tags = fm.get("tags") or fm.get("topics") or ["general"]
        if isinstance(tags, str):
            tags = [tags]

        created_pages: list[Path] = []

        # 1. Create or update Source Summary page under data/wiki/sources/
        source_page_id = f"src-{doc_id}"
        source_page_path = self.wiki_dir / "sources" / f"{source_page_id}.md"

        source_fm = {
            "id": source_page_id,
            "type": "source",
            "title": f"Source Summary: {title}",
            "aliases": [title, doc_path.name],
            "tags": list(tags),
            "sources": [{"path": rel_doc_path, "sha256": sha256}],
            "created_at": today,
            "updated_at": today,
            "status": "stable",
            "contradictions": [],
            "links_out": [],
        }

        source_body = (
            f"# Source Summary: {title}\n\n"
            f"**Raw Source File**: `{rel_doc_path}`\n"
            f"**SHA256**: `{sha256}`\n\n"
            f"## Summary\n\n{body[:500]}...\n"
        )

        validate(instance=source_fm, schema=self.schema)
        write_wiki_page(source_page_path, source_fm, source_body)
        created_pages.append(source_page_path)

        # 2. Extract potential entity page (for hardware/registers/ROM labels)
        if any(keyword in rel_doc_path.lower() for keyword in ["c64ref", "io-map", "rom"]):
            entity_id = doc_id
            entity_path = self.wiki_dir / "entities" / f"{entity_id}.md"

            existing_fm: dict[str, Any] = {}
            if entity_path.exists():
                existing_fm, _ = load_yaml_frontmatter(entity_path)

            sources_list = existing_fm.get("sources", [])
            if not any(s.get("path") == rel_doc_path for s in sources_list):
                sources_list.append({"path": rel_doc_path, "sha256": sha256})

            entity_fm = {
                "id": entity_id,
                "type": "entity",
                "title": title,
                "aliases": existing_fm.get("aliases") or [title],
                "tags": list(set((existing_fm.get("tags") or []) + tags)),
                "sources": sources_list,
                "created_at": existing_fm.get("created_at") or today,
                "updated_at": today,
                "status": existing_fm.get("status") or "stable",
                "contradictions": existing_fm.get("contradictions") or [],
                "links_out": existing_fm.get("links_out") or [],
            }

            entity_body = f"# {title}\n\n{body}\n\n## References\n- Source: [[{source_page_id}]]\n"

            validate(instance=entity_fm, schema=self.schema)
            write_wiki_page(entity_path, entity_fm, entity_body)
            created_pages.append(entity_path)

        self.log_operation(f"Ingested `{rel_doc_path}` -> created {len(created_pages)} wiki pages")
        return created_pages
