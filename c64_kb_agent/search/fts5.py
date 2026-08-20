"""SQLite FTS5 Search Engine implementation for C64-KB-Agent."""

import sqlite3
from typing import Any

from c64_kb_agent.db import DatabaseDAO


class FTSSearchEngine:
    """FTS5 Search Engine providing full-text search with BM25 ranking and filtering."""

    def __init__(self, dao: DatabaseDAO | None = None):
        self.dao = dao or DatabaseDAO()

    def search(
        self,
        query: str,
        category: str | None = None,
        difficulty: str | None = None,
        language: str | None = None,
        hardware: str | None = None,
        limit: int = 10,
        offset: int = 0,
    ) -> dict[str, Any]:
        """Performs full-text search with BM25 ranking, filters, and snippets.

        Returns:
            Dict containing query, total, and results list.
        """
        if not self.dao.db_path.exists():
            return {
                "query": query,
                "total": 0,
                "results": [],
                "error": "Search index database not found. Run rebuild-index first.",
            }

        conn = self.dao.get_connection()
        try:
            clean_query = query.strip().replace('"', '""')
            if not clean_query:
                return {"query": query, "total": 0, "results": []}

            sql_base = """
                FROM documents_fts fts
                JOIN documents d ON fts.id = d.id
                WHERE documents_fts MATCH ?
            """
            params: list[Any] = [clean_query]

            if category:
                sql_base += " AND d.category = ?"
                params.append(category)
            if difficulty:
                sql_base += " AND d.difficulty = ?"
                params.append(difficulty)
            if language:
                sql_base += " AND d.language = ?"
                params.append(language)
            if hardware:
                sql_base += " AND d.hardware LIKE ?"
                params.append(f"%{hardware}%")

            count_sql = f"SELECT COUNT(*) {sql_base}"
            total = conn.execute(count_sql, params).fetchone()[0]

            select_sql = f"""
                SELECT
                    d.id,
                    d.filepath,
                    d.title,
                    d.source_url,
                    d.category,
                    d.difficulty,
                    d.language,
                    d.hardware,
                    d.topics,
                    bm25(documents_fts) AS rank,
                    snippet(documents_fts, 7, '<b>', '</b>', '...', 64) AS snippet
                {sql_base}
                ORDER BY rank ASC
                LIMIT ? OFFSET ?
            """
            params.extend([limit, offset])

            rows = conn.execute(select_sql, params).fetchall()

            results = []
            for r in rows:
                results.append({
                    "id": r["id"],
                    "filepath": r["filepath"],
                    "title": r["title"],
                    "source_url": r["source_url"],
                    "category": r["category"],
                    "difficulty": r["difficulty"],
                    "language": r["language"],
                    "hardware": r["hardware"],
                    "topics": [t.strip() for t in r["topics"].split(",")] if r["topics"] else [],
                    "rank": round(r["rank"], 4),
                    "snippet": r["snippet"],
                })

            return {
                "query": query,
                "total": total,
                "limit": limit,
                "offset": offset,
                "results": results,
            }
        except sqlite3.Error as e:
            return {
                "query": query,
                "total": 0,
                "results": [],
                "error": f"FTS5 Search Query Error: {e}",
            }
        finally:
            conn.close()
