"""SQLite Database DAO for C64-KB-Agent."""

import datetime
import sqlite3
from pathlib import Path
from typing import Any

from c64_kb_agent.config import settings
from c64_kb_agent.validators.document import get_all_documents, parse_frontmatter


class DatabaseDAO:
    """Data Access Object for SQLite FTS5 search index."""

    def __init__(self, db_path: Path | None = None):
        self.db_path = db_path or settings.db_path

    def get_connection(self) -> sqlite3.Connection:
        """Establishes and returns a connection to the SQLite database."""
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def get_status(self) -> dict[str, Any]:
        """Returns database status and document/routine counts."""
        status_info: dict[str, Any] = {
            "exists": self.db_path.exists(),
            "path": str(self.db_path),
            "size_mb": 0.0,
            "last_modified": None,
            "indexed_documents": 0,
            "indexed_routines": 0,
        }

        if not self.db_path.exists():
            return status_info

        stat = self.db_path.stat()
        status_info["size_mb"] = round(stat.st_size / (1024 * 1024), 2)
        status_info["last_modified"] = datetime.datetime.fromtimestamp(
            stat.st_mtime, tz=datetime.timezone.utc
        ).isoformat()

        try:
            with self.get_connection() as conn:
                doc_row = conn.execute("SELECT COUNT(*) FROM documents").fetchone()
                status_info["indexed_documents"] = doc_row[0] if doc_row else 0

                routine_table = conn.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name='routines'"
                ).fetchone()
                if routine_table:
                    rt_row = conn.execute("SELECT COUNT(*) FROM routines").fetchone()
                    status_info["indexed_routines"] = rt_row[0] if rt_row else 0
        except sqlite3.Error as e:
            status_info["error"] = str(e)

        return status_info

    def rebuild_index(self, docs_dir: Path | None = None) -> tuple[int, int]:
        """Rebuilds SQLite FTS5 search index from Markdown documents.

        Returns:
            Tuple of (indexed_documents_count, indexed_routines_count)
        """
        target_docs = docs_dir or settings.docs_dir

        if self.db_path.exists():
            self.db_path.unlink()

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE documents (
                id TEXT PRIMARY KEY,
                filepath TEXT,
                title TEXT,
                source_url TEXT,
                category TEXT,
                difficulty TEXT,
                language TEXT,
                hardware TEXT,
                topics TEXT,
                body TEXT
            )
        """)

        cursor.execute("""
            CREATE VIRTUAL TABLE documents_fts USING fts5(
                id,
                title,
                category,
                difficulty,
                language,
                hardware,
                topics,
                body
            )
        """)

        cursor.execute("""
            CREATE TABLE routines (
                name TEXT,
                address TEXT,
                description TEXT,
                source_url TEXT,
                doc_id TEXT
            )
        """)

        doc_paths = get_all_documents(target_docs)
        indexed_docs = 0
        indexed_routines = 0

        for doc in doc_paths:
            rel_path = (
                str(doc.relative_to(target_docs))
                if doc.is_relative_to(target_docs)
                else str(doc)
            )
            try:
                fm, body = parse_frontmatter(doc)
            except Exception:
                continue

            if not fm:
                continue

            doc_id = fm.get("id") or rel_path
            title = fm.get("title", "")
            source_url = fm.get("source_url", "")
            category = fm.get("category", "")
            difficulty = fm.get("difficulty", "")
            language = fm.get("language", "")

            hw = fm.get("hardware", [])
            hardware_str = ", ".join(hw) if isinstance(hw, list) else str(hw)

            tp = fm.get("topics", fm.get("tags", []))
            topics_str = ", ".join(tp) if isinstance(tp, list) else str(tp)

            body_str = body.strip()

            cursor.execute(
                """
                INSERT INTO documents (id, filepath, title, source_url, category, difficulty, language, hardware, topics, body)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    doc_id,
                    rel_path,
                    title,
                    source_url,
                    category,
                    difficulty,
                    language,
                    hardware_str,
                    topics_str,
                    body_str,
                ),
            )

            cursor.execute(
                """
                INSERT INTO documents_fts (id, title, category, difficulty, language, hardware, topics, body)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    doc_id,
                    title,
                    category,
                    difficulty,
                    language,
                    hardware_str,
                    topics_str,
                    body_str,
                ),
            )

            indexed_docs += 1

            c64ref_meta = fm.get("c64ref", {})
            if c64ref_meta and isinstance(c64ref_meta, dict):
                symbol = c64ref_meta.get("symbol")
                address = c64ref_meta.get("address", "")
                if symbol:
                    cursor.execute(
                        """
                        INSERT INTO routines (name, address, description, source_url, doc_id)
                        VALUES (?, ?, ?, ?, ?)
                    """,
                        (symbol, address, title, source_url, doc_id),
                    )
                    indexed_routines += 1

        conn.commit()
        conn.close()

        return indexed_docs, indexed_routines
