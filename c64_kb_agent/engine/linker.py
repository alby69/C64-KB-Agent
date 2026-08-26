"""Wiki linker module for C64 LLM-Wiki Engine.

Scans compiled Layer 2 wiki pages under data/wiki/ for Obsidian [[slug]] wiki-links,
extracts outgoing references, updates links_out frontmatter arrays, and maintains link graph integrity.
"""

from pathlib import Path
import re
from typing import Any

from c64_kb_agent.config import settings
from c64_kb_agent.engine.ingestor import load_yaml_frontmatter, write_wiki_page
from c64_kb_agent.utils.logging import logger

WIKI_LINK_REGEX = re.compile(r"\[\[([a-zA-Z0-9_-]+)(?:\|[^\]]+)?\]\]")


class WikiLinker:
    """Linker engine managing wiki-links across Layer 2 wiki pages."""

    def __init__(self, wiki_dir: Path | None = None) -> None:
        self.wiki_dir = wiki_dir or (settings.base_dir / "data" / "wiki")

    def get_all_wiki_pages(self) -> list[Path]:
        """Returns list of all Markdown wiki pages excluding index.md and log.md."""
        if not self.wiki_dir.exists():
            return []
        return sorted(
            p
            for p in self.wiki_dir.rglob("*.md")
            if p.is_file() and p.name not in ["index.md", "log.md"]
        )

    def extract_wiki_links(self, body: str) -> list[str]:
        """Extracts unique Obsidian [[slug]] wiki-link target IDs from text body."""
        return sorted(list(set(WIKI_LINK_REGEX.findall(body))))

    def update_page_links(self, page_path: Path) -> list[str]:
        """Scans single wiki page, extracts links, and updates frontmatter links_out.

        Returns list of extracted outbound link IDs.
        """
        fm, body = load_yaml_frontmatter(page_path)
        if not fm:
            return []

        links_out = self.extract_wiki_links(body)
        fm["links_out"] = links_out
        write_wiki_page(page_path, fm, body)
        return links_out

    def link_all_pages(self) -> dict[str, Any]:
        """Updates outbound links for all wiki pages.

        Returns dict summary with total pages processed and total links extracted.
        """
        pages = self.get_all_wiki_pages()
        total_links = 0
        for page in pages:
            links = self.update_page_links(page)
            total_links += len(links)

        logger.info("wiki_linker_completed", pages_count=len(pages), total_links=total_links)
        return {"pages_processed": len(pages), "total_links": total_links}
