"""CLI interface for C64 LLM-Wiki Engine subcommands."""

import argparse
import json
from pathlib import Path

from c64_kb_agent.engine.indexer import WikiIndexer
from c64_kb_agent.engine.ingestor import WikiIngestor
from c64_kb_agent.engine.linker import WikiLinker
from c64_kb_agent.engine.linter import WikiLinter
from c64_kb_agent.engine.synthesizer import WikiSynthesizer
from c64_kb_agent.search.fts5 import FTSSearchEngine


def build_engine_parser(subparsers: argparse._SubParsersAction) -> None:
    """Attaches wiki engine subcommands to main CLI subparser."""
    wiki_parser = subparsers.add_parser(
        "wiki",
        help="LLM-Wiki Engine commands (ingest, link, synthesize, lint, rebuild-index, query)",
    )
    wiki_subparsers = wiki_parser.add_subparsers(dest="wiki_command", required=True)

    # ingest
    ingest_p = wiki_subparsers.add_parser("ingest", help="Ingest Layer 1 doc into Layer 2 Wiki")
    ingest_p.add_argument(
        "--file", "-f", required=True, help="Path to raw Markdown document to ingest"
    )

    # link
    wiki_subparsers.add_parser("link", help="Extract and update [[wiki-links]] across wiki pages")

    # synthesize
    wiki_subparsers.add_parser(
        "synthesize", help="Rebuild wiki master index.md and topic aggregations"
    )

    # lint
    wiki_subparsers.add_parser("lint", help="Run schema and link integrity health-checks")

    # rebuild-index
    wiki_subparsers.add_parser("rebuild-index", help="Rebuild FTS5 search index with wiki pages")

    # query
    query_p = wiki_subparsers.add_parser("query", help="Query knowledge base via FTS5 search")
    query_p.add_argument("text", help="Search query string")
    query_p.add_argument("--limit", "-l", type=int, default=10, help="Max search results")


def handle_engine_cli(args: argparse.Namespace) -> int:
    """Handles execution of wiki engine subcommands."""
    cmd = getattr(args, "wiki_command", None)
    output_format = getattr(args, "format", "text")

    if cmd == "ingest":
        ingestor = WikiIngestor()
        created = ingestor.ingest_document(Path(args.file))
        result = {
            "status": "ok",
            "ingested_file": args.file,
            "pages_created": [str(p) for p in created],
        }
        if output_format == "json":
            print(json.dumps(result, indent=2))
        else:
            print(f"Ingested '{args.file}' -> Created/updated {len(created)} wiki page(s).")
        return 0

    if cmd == "link":
        linker = WikiLinker()
        res = linker.link_all_pages()
        if output_format == "json":
            print(json.dumps(res, indent=2))
        else:
            print(
                f"Wiki linking completed: {res['pages_processed']} pages processed, {res['total_links']} links updated."
            )
        return 0

    if cmd == "synthesize":
        synth = WikiSynthesizer()
        idx = synth.rebuild_index()
        result = {"status": "ok", "index_path": str(idx)}
        if output_format == "json":
            print(json.dumps(result, indent=2))
        else:
            print(f"Wiki index rebuilt at '{idx}'.")
        return 0

    if cmd == "lint":
        linter = WikiLinter()
        report = linter.lint_wiki()
        if output_format == "json":
            import sys

            sys.stdout.write(json.dumps(report, indent=2) + "\n")
        else:
            print(f"Wiki Lint Summary: Scanned {report['total_pages_scanned']} pages.")
            print(f"  Schema errors: {len(report['invalid_schema'])}")
            print(f"  Broken links: {len(report['broken_links'])}")
            print(f"  Orphans: {len(report['orphans'])}")
            print(f"  Flagged contradictions: {len(report['flagged_contradictions'])}")
        return 0 if len(report["invalid_schema"]) == 0 else 1

    if cmd == "rebuild-index":
        indexer = WikiIndexer()
        total = indexer.rebuild_fts_index_with_wiki()
        res = {"status": "ok", "total_indexed": total}
        if output_format == "json":
            print(json.dumps(res, indent=2))
        else:
            print(f"FTS5 index rebuilt successfully ({total} total documents indexed).")
        return 0

    if cmd == "query":
        engine = FTSSearchEngine()
        results = engine.search(args.text, limit=args.limit)
        if output_format == "json":
            print(json.dumps(results, indent=2))
        else:
            print(f"Search Results for '{args.text}' ({len(results)} found):")
            for r in results:
                if isinstance(r, dict):
                    title_val = r.get("title", "")
                    fp_val = r.get("filepath", "")
                    rank_val = float(r.get("rank", 0.0))
                    print(f"  - [{title_val}] ({fp_val}) score={rank_val:.3f}")
        return 0

    return 1
