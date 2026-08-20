"""CLI command handlers for C64-KB-Agent."""

import json
from collections.abc import Callable
from typing import Any

from c64_kb_agent.config import settings
from c64_kb_agent.db import DatabaseDAO
from c64_kb_agent.quality import analyze_data_quality
from c64_kb_agent.search.fts5 import FTSSearchEngine
from c64_kb_agent.validators.dataset import validate_dataset_jsonl
from c64_kb_agent.validators.document import get_all_documents, validate_all_documents
from c64_kb_agent.validators.graph_and_api import (
    validate_api_index,
    validate_cross_references,
    validate_knowledge_graph,
)
from c64_kb_agent.validators.manifest import validate_manifest


def output_result(
    data: dict[str, Any], text_formatter: Callable[[dict[str, Any]], int], output_format: str = "text"
) -> int:
    """Outputs result in JSON or plain text based on output_format."""
    if output_format == "json":
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return 0
    else:
        return text_formatter(data)


def cmd_status(output_format: str = "text") -> int:
    """Status command handler."""
    dao = DatabaseDAO()
    db_status = dao.get_status()

    doc_paths = get_all_documents(settings.docs_dir)
    by_source: dict[str, int] = {}
    for doc in doc_paths:
        rel = doc.relative_to(settings.docs_dir)
        src = rel.parts[0] if len(rel.parts) > 1 else "root"
        by_source[src] = by_source.get(src, 0) + 1

    dataset_files_info = {}
    for fname in [
        "scraped_dataset.jsonl",
        "api_index.json",
        "knowledge_graph.json",
        "manifest.json",
    ]:
        fpath = (
            settings.dataset_dir / fname
            if fname != "manifest.json"
            else settings.manifest_path
        )
        if fpath.exists():
            stat = fpath.stat()
            dataset_files_info[fname] = {
                "exists": True,
                "size_mb": round(stat.st_size / (1024 * 1024), 2),
            }
        else:
            dataset_files_info[fname] = {"exists": False}

    status_data = {
        "documents": {
            "total": len(doc_paths),
            "by_source": by_source,
        },
        "dataset_files": dataset_files_info,
        "search_index": db_status,
    }

    def print_text(data: dict[str, Any]) -> int:
        print("=== C64-KB-Agent Status ===")
        print(f"\n[Documents] Total: {data['documents']['total']}")
        for src, count in sorted(data["documents"]["by_source"].items()):
            print(f"  - {src}: {count} files")

        print("\n[Dataset files]")
        for fname, info in data["dataset_files"].items():
            if info["exists"]:
                print(f"  - {fname}: {info['size_mb']:.2f} MB")
            else:
                print(f"  - {fname}: NOT FOUND")

        print("\n[Search Index (SQLite FTS5)]")
        idx = data["search_index"]
        if idx["exists"]:
            print(f"  - Path: {idx['path']}")
            print(f"  - Size: {idx['size_mb']:.2f} MB")
            print(f"  - Indexed documents: {idx['indexed_documents']}")
            print(f"  - Indexed routines: {idx['indexed_routines']}")
        else:
            print("  - search_index.db: NOT FOUND")
        return 0

    return output_result(status_data, print_text, output_format)


def cmd_validate(output_format: str = "text") -> int:
    """Validate command handler."""
    doc_count, doc_errors = validate_all_documents(settings.docs_dir)
    jsonl_count, jsonl_errors = validate_dataset_jsonl(
        settings.dataset_dir / "scraped_dataset.jsonl"
    )
    manifest_ok, manifest_errors = validate_manifest(settings.manifest_path)
    kg_ok, kg_errors = validate_knowledge_graph(settings.dataset_dir / "knowledge_graph.json")
    api_ok, api_errors = validate_api_index(settings.dataset_dir / "api_index.json")
    cross_errors = validate_cross_references(settings.docs_dir, settings.dataset_dir)

    all_errors = bool(
        doc_errors
        or jsonl_errors
        or manifest_errors
        or kg_errors
        or api_errors
        or cross_errors
    )

    data = {
        "passed": not all_errors,
        "documents": {"checked": doc_count, "errors": doc_errors},
        "dataset_jsonl": {"checked": jsonl_count, "errors": jsonl_errors},
        "manifest": {"valid": manifest_ok, "errors": manifest_errors},
        "knowledge_graph": {"valid": kg_ok, "errors": kg_errors},
        "api_index": {"valid": api_ok, "errors": api_errors},
        "cross_references": {"errors": cross_errors},
    }

    def print_text(res: dict[str, Any]) -> int:
        print("=== Validating C64-KB-Agent Data ===")
        print(
            f"\n1. Documents: Checked {res['documents']['checked']} docs. Errors: {len(res['documents']['errors'])}"
        )
        print(
            f"2. Dataset JSONL: Checked {res['dataset_jsonl']['checked']} records. Errors: {len(res['dataset_jsonl']['errors'])}"
        )
        print(f"3. Manifest: {'OK' if res['manifest']['valid'] else 'FAILED'}")
        print(f"4. Knowledge Graph: {'OK' if res['knowledge_graph']['valid'] else 'FAILED'}")
        print(f"5. API Index: {'OK' if res['api_index']['valid'] else 'FAILED'}")
        print(f"6. Cross References: Errors: {len(res['cross_references']['errors'])}")

        if res["passed"]:
            print("\nValidation Result: PASSED")
            return 0
        else:
            print("\nValidation Result: FAILED")
            return 1

    code = output_result(data, print_text, output_format)
    return 1 if all_errors else code


def cmd_rebuild_index(output_format: str = "text") -> int:
    """Rebuild-index command handler."""
    dao = DatabaseDAO()
    indexed_docs, indexed_routines = dao.rebuild_index(settings.docs_dir)

    data = {
        "status": "success",
        "db_path": str(settings.db_path),
        "indexed_documents": indexed_docs,
        "indexed_routines": indexed_routines,
    }

    def print_text(res: dict[str, Any]) -> int:
        print("=== Rebuilding SQLite FTS5 Search Index ===")
        print("Index rebuild complete!")
        print(f"  - Indexed documents: {res['indexed_documents']}")
        print(f"  - Indexed routines: {res['indexed_routines']}")
        print(f"  - Database path: {res['db_path']}")
        return 0

    return output_result(data, print_text, output_format)


def cmd_search(
    query: str,
    category: str | None = None,
    difficulty: str | None = None,
    language: str | None = None,
    hardware: str | None = None,
    limit: int = 10,
    output_format: str = "text",
) -> int:
    """Search command handler."""
    engine = FTSSearchEngine()
    results = engine.search(
        query=query,
        category=category,
        difficulty=difficulty,
        language=language,
        hardware=hardware,
        limit=limit,
    )

    def print_text(res: dict[str, Any]) -> int:
        print(f"=== Search results for '{res['query']}' (Total: {res['total']}) ===")
        if not res["results"]:
            print("No matching documents found.")
            return 0
        for i, item in enumerate(res["results"], 1):
            print(f"\n{i}. {item['title']} (ID: {item['id']})")
            print(
                f"   Category: {item['category']} | Language: {item['language']} | Hardware: {item['hardware']}"
            )
            print(f"   Snippet: {item['snippet']}")
        return 0

    return output_result(results, print_text, output_format)


def cmd_quality_report(output_format: str = "text") -> int:
    """Quality report command handler."""
    report = analyze_data_quality(settings.docs_dir)

    def print_text(res: dict[str, Any]) -> int:
        print("=== C64-KB-Agent Data Quality Report ===")
        print(f"Total documents: {res['total_documents']}")
        print(f"Empty body docs: {res['empty_body_count']}")
        print(f"Malformed frontmatter docs: {res['malformed_frontmatter_count']}")
        print(f"Duplicate IDs: {res['duplicate_ids_count']}")
        print(f"Duplicate URLs: {res['duplicate_urls_count']}")
        print(f"Duplicate Content: {res['duplicate_content_count']}")
        return 0

    return output_result(report, print_text, output_format)


def cmd_serve(host: str = "127.0.0.1", port: int = 8001) -> int:
    """Serve command handler launching FastAPI server via uvicorn."""
    import uvicorn

    print(f"Starting C64-KB-Agent REST API server on http://{host}:{port}")
    uvicorn.run("c64_kb_agent.server.api:app", host=host, port=port, reload=False)
    return 0
