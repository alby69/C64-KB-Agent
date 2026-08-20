"""CLI Entry Point module for c64_kb_agent."""

import argparse
import sys

from c64_kb_agent.cli_handlers import (
    cmd_quality_report,
    cmd_rebuild_index,
    cmd_search,
    cmd_serve,
    cmd_status,
    cmd_validate,
)


def main(args: list[str] | None = None) -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="c64-kb-agent",
        description="C64-KB-Agent CLI — Knowledge Base management, validation, and indexing.",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    p_status = subparsers.add_parser("status", help="Show Knowledge Base status and counts")
    p_status.add_argument(
        "--format", choices=["text", "json"], default="text", help="Output format"
    )

    p_val = subparsers.add_parser(
        "validate", help="Validate documents and datasets against JSON schemas"
    )
    p_val.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    p_reb = subparsers.add_parser("rebuild-index", help="Rebuild SQLite FTS5 search index")
    p_reb.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    p_src = subparsers.add_parser("search", help="Search FTS5 index using BM25")
    p_src.add_argument("query", type=str, help="Search query")
    p_src.add_argument("--category", type=str, help="Filter by category")
    p_src.add_argument("--difficulty", type=str, help="Filter by difficulty")
    p_src.add_argument("--language", type=str, help="Filter by language")
    p_src.add_argument("--hardware", type=str, help="Filter by hardware")
    p_src.add_argument("--limit", type=int, default=10, help="Results limit")
    p_src.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    p_qual = subparsers.add_parser("quality-report", help="Generate data quality report")
    p_qual.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    p_srv = subparsers.add_parser("serve", help="Launch FastAPI REST API server")
    p_srv.add_argument("--host", type=str, default="127.0.0.1", help="API host")
    p_srv.add_argument("--port", type=int, default=8001, help="API port")

    parsed = parser.parse_args(args)

    if parsed.command == "status":
        return cmd_status(output_format=parsed.format)
    elif parsed.command == "validate":
        return cmd_validate(output_format=parsed.format)
    elif parsed.command == "rebuild-index":
        return cmd_rebuild_index(output_format=parsed.format)
    elif parsed.command == "search":
        return cmd_search(
            query=parsed.query,
            category=parsed.category,
            difficulty=parsed.difficulty,
            language=parsed.language,
            hardware=parsed.hardware,
            limit=parsed.limit,
            output_format=parsed.format,
        )
    elif parsed.command == "quality-report":
        return cmd_quality_report(output_format=parsed.format)
    elif parsed.command == "serve":
        return cmd_serve(host=parsed.host, port=parsed.port)
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
