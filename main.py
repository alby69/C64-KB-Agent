"""main.py — CLI Entry Point for C64-KB-Agent.

Provides commands:
  - status: Summary of documents, dataset files, and search index status.
  - validate: Validates documents and dataset JSONL against schemas.
  - rebuild-index: Rebuilds SQLite FTS5 index (data/dataset/search_index.db) from data/docs.
"""

import argparse
import datetime
import sqlite3
import sys

from kbvalidate import (
    BASE_DIR,
    DATASET_DIR,
    DOCS_DIR,
    get_all_documents,
    parse_frontmatter,
    validate_all_documents,
    validate_dataset_jsonl,
)


def cmd_status() -> int:
    """Displays status of documents, dataset files, and search index."""
    print("=== C64-KB-Agent Status ===")

    # Documents status
    docs = get_all_documents(DOCS_DIR)
    print(f"\n[Documents] Total: {len(docs)}")
    if docs:
        by_source = {}
        for doc in docs:
            rel = doc.relative_to(DOCS_DIR)
            source = rel.parts[0] if len(rel.parts) > 1 else "root"
            by_source[source] = by_source.get(source, 0) + 1
        for src, count in sorted(by_source.items()):
            print(f"  - {src}: {count} files")

    # Dataset status
    print("\n[Dataset files]")
    dataset_files = [
        "scraped_dataset.jsonl",
        "api_index.json",
        "knowledge_graph.json",
        "manifest.json",
    ]
    for filename in dataset_files:
        fpath = (
            DATASET_DIR / filename
            if filename != "manifest.json"
            else BASE_DIR / "data" / "manifest.json"
        )
        if fpath.exists():
            stat = fpath.stat()
            size_mb = stat.st_size / (1024 * 1024)
            mtime = datetime.datetime.fromtimestamp(
                stat.st_mtime, tz=datetime.timezone.utc
            ).strftime("%Y-%m-%d %H:%M:%S UTC")
            print(f"  - {filename}: {size_mb:.2f} MB (modified {mtime})")
        else:
            print(f"  - {filename}: NOT FOUND")

    # Search index status
    db_path = DATASET_DIR / "search_index.db"
    print("\n[Search Index (SQLite FTS5)]")
    if db_path.exists():
        size_mb = db_path.stat().st_size / (1024 * 1024)
        mtime = datetime.datetime.fromtimestamp(
            db_path.stat().st_mtime, tz=datetime.timezone.utc
        ).strftime("%Y-%m-%d %H:%M:%S UTC")
        print(f"  - Path: {db_path.relative_to(BASE_DIR)}")
        print(f"  - Size: {size_mb:.2f} MB")
        print(f"  - Last modified: {mtime}")
        try:
            conn = sqlite3.connect(db_path)
            doc_count = conn.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
            routine_count = (
                conn.execute("SELECT COUNT(*) FROM routines").fetchone()[0]
                if conn.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name='routines'"
                ).fetchone()
                else 0
            )
            conn.close()
            print(f"  - Indexed documents: {doc_count}")
            print(f"  - Indexed routines: {routine_count}")
        except sqlite3.Error as e:
            print(f"  - Error reading DB: {e}")
    else:
        print("  - search_index.db: NOT FOUND (Run 'python main.py rebuild-index' to create)")

    return 0


def cmd_validate() -> int:
    """Validates documents and dataset files against JSON schemas."""
    print("=== Validating C64-KB-Agent Data ===")
    has_errors = False

    # Validate Markdown documents
    print("\n1. Validating Markdown documents in data/docs/...")
    doc_count, doc_errors = validate_all_documents(DOCS_DIR)
    print(f"   Checked {doc_count} documents.")
    if doc_errors:
        has_errors = True
        print(f"   FAILED: {len(doc_errors)} invalid documents found:")
        for rel_path, msg in doc_errors[:20]:
            print(f"     - {rel_path}: {msg}")
        if len(doc_errors) > 20:
            print(f"     ... and {len(doc_errors) - 20} more.")
    else:
        print("   OK: All documents conform to schema.")

    # Validate dataset JSONL
    jsonl_path = DATASET_DIR / "scraped_dataset.jsonl"
    if jsonl_path.exists():
        print(f"\n2. Validating {jsonl_path.relative_to(BASE_DIR)}...")
        rec_count, jsonl_errors = validate_dataset_jsonl(jsonl_path)
        print(f"   Checked {rec_count} records.")
        if jsonl_errors:
            has_errors = True
            print(f"   FAILED: {len(jsonl_errors)} invalid records found:")
            for item, msg in jsonl_errors[:20]:
                print(f"     - {item}: {msg}")
            if len(jsonl_errors) > 20:
                print(f"     ... and {len(jsonl_errors) - 20} more.")
        else:
            print("   OK: All dataset records conform to schema.")

    if has_errors:
        print("\nValidation Result: FAILED")
        return 1

    print("\nValidation Result: PASSED")
    return 0


def cmd_rebuild_index() -> int:
    """Rebuilds the SQLite FTS5 search index (data/dataset/search_index.db) from Markdown docs."""
    print("=== Rebuilding SQLite FTS5 Search Index ===")
    DATASET_DIR.mkdir(parents=True, exist_ok=True)
    db_path = DATASET_DIR / "search_index.db"

    # Remove existing db if present to build fresh
    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create tables matching the original schema
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

    docs = get_all_documents(DOCS_DIR)
    indexed_docs = 0
    indexed_routines = 0

    for doc in docs:
        rel_path = str(doc.relative_to(DOCS_DIR))
        fm, body = parse_frontmatter(doc)
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
            (doc_id, title, category, difficulty, language, hardware_str, topics_str, body_str),
        )

        indexed_docs += 1

        # Check for routine metadata (e.g. kernal or c64ref routine info)
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

    print("Index rebuild complete!")
    print(f"  - Indexed documents: {indexed_docs}")
    print(f"  - Indexed routines: {indexed_routines}")
    db_rel = db_path.relative_to(BASE_DIR) if db_path.is_relative_to(BASE_DIR) else db_path
    print(f"  - Database path: {db_rel}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="c64-kb-agent",
        description="C64-KB-Agent CLI — Knowledge Base management, validation, and indexing.",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("status", help="Show Knowledge Base status and counts")
    subparsers.add_parser("validate", help="Validate documents and datasets against JSON schemas")
    subparsers.add_parser("rebuild-index", help="Rebuild SQLite FTS5 search index")

    args = parser.parse_args()

    if args.command == "status":
        sys.exit(cmd_status())
    elif args.command == "validate":
        sys.exit(cmd_validate())
    elif args.command == "rebuild-index":
        sys.exit(cmd_rebuild_index())
    else:
        parser.print_help()
        sys.exit(0)


if __name__ == "__main__":
    main()
