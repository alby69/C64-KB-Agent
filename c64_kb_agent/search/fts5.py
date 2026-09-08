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
        layer: str = "all",
        limit: int = 10,
        offset: int = 0,
    ) -> dict[str, Any]:
        """Performs full-text search with BM25 ranking, filters, and snippets.

        Supports layer filtering ("docs", "wiki", or "all").

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

            results: list[dict[str, Any]] = []

            # 1. Search Layer 1 (documents) if layer in ("all", "docs")
            if layer in ("all", "docs"):
                sql_base_docs = """
                    FROM documents_fts fts
                    JOIN documents d ON fts.id = d.id
                    WHERE documents_fts MATCH ?
                """
                params_docs: list[Any] = [clean_query]

                if category:
                    sql_base_docs += " AND d.category = ?"
                    params_docs.append(category)
                if difficulty:
                    sql_base_docs += " AND d.difficulty = ?"
                    params_docs.append(difficulty)
                if language:
                    sql_base_docs += " AND d.language = ?"
                    params_docs.append(language)
                if hardware:
                    sql_base_docs += " AND d.hardware LIKE ?"
                    params_docs.append(f"%{hardware}%")

                select_docs = f"""
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
                        'docs' AS source_layer,
                        bm25(documents_fts) AS rank,
                        snippet(documents_fts, 7, '<b>', '</b>', '...', 64) AS snippet
                    {sql_base_docs}
                """
                try:
                    rows_docs = conn.execute(select_docs, params_docs).fetchall()
                    for r in rows_docs:
                        results.append(
                            {
                                "id": r["id"],
                                "filepath": r["filepath"],
                                "title": r["title"],
                                "source_url": r["source_url"],
                                "category": r["category"],
                                "difficulty": r["difficulty"],
                                "language": r["language"],
                                "hardware": r["hardware"],
                                "topics": [t.strip() for t in r["topics"].split(",")]
                                if r["topics"]
                                else [],
                                "source_layer": r["source_layer"],
                                "rank": round(r["rank"], 4),
                                "snippet": r["snippet"],
                            }
                        )
                except sqlite3.Error:
                    pass

            # 2. Search Layer 2 (wiki_pages) if layer in ("all", "wiki")
            wiki_table_check = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='wiki_pages_fts'"
            ).fetchone()
            if layer in ("all", "wiki") and wiki_table_check:
                sql_base_wiki = """
                    FROM wiki_pages_fts fts
                    JOIN wiki_pages w ON fts.id = w.id
                    WHERE wiki_pages_fts MATCH ?
                """
                params_wiki: list[Any] = [clean_query]

                select_wiki = f"""
                    SELECT
                        w.id,
                        w.filepath,
                        w.title,
                        w.type AS category,
                        '' AS difficulty,
                        '' AS language,
                        '' AS hardware,
                        w.tags AS topics,
                        'wiki' AS source_layer,
                        bm25(wiki_pages_fts) AS rank,
                        snippet(wiki_pages_fts, 6, '<b>', '</b>', '...', 64) AS snippet
                    {sql_base_wiki}
                """
                try:
                    rows_wiki = conn.execute(select_wiki, params_wiki).fetchall()
                    for r in rows_wiki:
                        results.append(
                            {
                                "id": r["id"],
                                "filepath": r["filepath"],
                                "title": r["title"],
                                "source_url": f"wiki/{r['category']}",
                                "category": r["category"],
                                "difficulty": r["difficulty"],
                                "language": r["language"],
                                "hardware": r["hardware"],
                                "topics": [t.strip() for t in r["topics"].split(",")]
                                if r["topics"]
                                else [],
                                "source_layer": r["source_layer"],
                                "rank": round(r["rank"], 4),
                                "snippet": r["snippet"],
                            }
                        )
                except sqlite3.Error:
                    pass

            # Sort by BM25 rank ascending (smaller rank score is better match in SQLite BM25)
            results.sort(key=lambda x: x["rank"])
            total = len(results)
            paginated = results[offset : offset + limit]

            return {
                "query": query,
                "total": total,
                "limit": limit,
                "offset": offset,
                "results": paginated,
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
