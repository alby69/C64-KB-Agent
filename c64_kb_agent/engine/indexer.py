"""Wiki search indexer module for C64 LLM-Wiki Engine.

Indexes compiled data/wiki/ Markdown documents into SQLite FTS5 search_index.db
under dedicated wiki_pages and wiki_pages_fts tables.
"""

import json
from pathlib import Path

from c64_kb_agent.config import settings
from c64_kb_agent.db import DatabaseDAO
from c64_kb_agent.engine.ingestor import load_yaml_frontmatter
from c64_kb_agent.utils.logging import logger


class WikiIndexer:
    """Indexer engine extending DatabaseDAO to index Layer 2 wiki pages into FTS5."""

    def __init__(
        self,
        db_dao: DatabaseDAO | None = None,
        wiki_dir: Path | None = None,
        docs_dir: Path | None = None,
    ) -> None:
        self.dao = db_dao or DatabaseDAO()
        self.wiki_dir = wiki_dir or (settings.base_dir / "data" / "wiki")
        self.docs_dir = docs_dir

    def rebuild_fts_index_with_wiki(self) -> int:
        """Rebuilds SQLite FTS5 index including both data/docs/ and data/wiki/ pages.

        Returns total count of indexed documents (Layer 1 + Layer 2 wiki pages).
        """
        indexed_docs, _ = self.dao.rebuild_index(docs_dir=self.docs_dir)
        indexed_count = indexed_docs

        if self.wiki_dir.exists():
            wiki_pages = [
                p
                for p in self.wiki_dir.rglob("*.md")
                if p.is_file() and p.name not in ["index.md", "log.md"]
            ]
            with self.dao.get_connection() as conn:
                cursor = conn.cursor()
                for page in wiki_pages:
                    fm, body = load_yaml_frontmatter(page)
                    doc_id = fm.get("id") or page.stem
                    page_type = fm.get("type", "entity")
                    title = fm.get("title") or page.stem
                    aliases = fm.get("aliases") or []
                    aliases_str = ", ".join(aliases) if isinstance(aliases, list) else str(aliases)
                    tags = fm.get("tags") or []
                    tags_str = ", ".join(tags) if isinstance(tags, list) else str(tags)
                    status = fm.get("status", "stable")
                    contradictions = json.dumps(fm.get("contradictions", []))
                    links_out = json.dumps(fm.get("links_out", []))

                    rel_path = (
                        str(page.relative_to(settings.base_dir))
                        if page.is_relative_to(settings.base_dir)
                        else str(page)
                    )

                    cursor.execute(
                        """
                        INSERT OR REPLACE INTO wiki_pages (id, filepath, type, title, aliases, tags, status, contradictions, links_out, body)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            doc_id,
                            rel_path,
                            page_type,
                            title,
                            aliases_str,
                            tags_str,
                            status,
                            contradictions,
                            links_out,
                            body.strip(),
                        ),
                    )
                    cursor.execute(
                        """
                        INSERT INTO wiki_pages_fts (id, type, title, aliases, tags, status, body)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            doc_id,
                            page_type,
                            title,
                            aliases_str,
                            tags_str,
                            status,
                            body.strip(),
                        ),
                    )
                    indexed_count += 1
                conn.commit()

        logger.info("wiki_fts_index_rebuilt", total_indexed=indexed_count)
        return indexed_count
