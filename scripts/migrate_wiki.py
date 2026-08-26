"""Initial wiki migration script (Fase 2).

Compiles Layer 1 raw Markdown documents under data/docs/ into initial Layer 2 wiki pages
under data/wiki/ without modifying or deleting any Layer 1 data.
"""

import argparse
from pathlib import Path
import sys

from c64_kb_agent.config import settings
from c64_kb_agent.engine.ingestor import WikiIngestor
from c64_kb_agent.engine.linker import WikiLinker
from c64_kb_agent.engine.synthesizer import WikiSynthesizer
from c64_kb_agent.utils.logging import logger


def run_migration(sources: list[str] | None = None, limit: int | None = None) -> None:
    """Executes initial non-destructive migration of raw docs into data/wiki/."""
    docs_dir = settings.docs_dir
    wiki_dir = settings.base_dir / "data" / "wiki"

    if not docs_dir.exists():
        logger.error("docs_dir_not_found", path=str(docs_dir))
        sys.exit(1)

    ingestor = WikiIngestor(wiki_dir=wiki_dir, docs_dir=docs_dir)
    linker = WikiLinker(wiki_dir=wiki_dir)
    synthesizer = WikiSynthesizer(wiki_dir=wiki_dir)

    target_sources = sources or ["c64ref", "codebase_c64_org", "elite_bbcelite_com", "sta_c64_org", "dustlayer_com", "github_com"]
    logger.info("starting_wiki_migration", target_sources=target_sources, limit=limit)

    all_docs: list[Path] = []
    for src in target_sources:
        src_dir = docs_dir / src
        if src_dir.exists():
            md_files = sorted(p for p in src_dir.rglob("*.md") if p.is_file() and p.name != "index.md")
            all_docs.extend(md_files)

    if limit:
        all_docs = all_docs[:limit]

    logger.info("total_documents_to_migrate", count=len(all_docs))

    total_pages_created = 0
    for idx, doc in enumerate(all_docs, start=1):
        try:
            created = ingestor.ingest_document(doc)
            total_pages_created += len(created)
            if idx % 100 == 0:
                logger.info("migration_progress", processed=idx, total=len(all_docs), pages_created=total_pages_created)
        except Exception as e:
            logger.error("migration_doc_failed", path=str(doc), error=str(e))

    logger.info("ingestion_phase_complete", total_docs=len(all_docs), total_pages=total_pages_created)

    # Linker phase
    link_res = linker.link_all_pages()
    logger.info("linking_phase_complete", pages_processed=link_res["pages_processed"], links_updated=link_res["total_links"])

    # Synthesizer phase
    index_path = synthesizer.rebuild_index()
    logger.info("synthesis_phase_complete", index_path=str(index_path))


def main() -> None:
    parser = argparse.ArgumentParser(description="Initial C64 LLM-Wiki non-destructive data migration script")
    parser.add_argument("--sources", nargs="+", help="Sources to migrate (e.g. c64ref codebase_c64_org)")
    parser.add_argument("--limit", type=int, help="Optional limit on total docs to migrate")
    args = parser.parse_args()

    run_migration(sources=args.sources, limit=args.limit)


if __name__ == "__main__":
    main()
