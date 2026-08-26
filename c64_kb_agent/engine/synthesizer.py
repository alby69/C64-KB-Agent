"""Wiki synthesizer module for C64 LLM-Wiki Engine.

Aggregates compiled entity and source data into topic pages (data/wiki/topics/),
synthesis pages (data/wiki/synthesis/), and updates data/wiki/index.md.
"""

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from c64_kb_agent.config import settings
from c64_kb_agent.engine.ingestor import load_yaml_frontmatter, write_wiki_page
from c64_kb_agent.utils.logging import logger


class WikiSynthesizer:
    """Synthesizer engine aggregating Layer 2 wiki entries into topics and index."""

    def __init__(self, wiki_dir: Path | None = None) -> None:
        self.wiki_dir = wiki_dir or (settings.base_dir / "data" / "wiki")

    def rebuild_index(self) -> Path:
        """Rebuilds data/wiki/index.md listing all compiled pages by type."""
        index_path = self.wiki_dir / "index.md"
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        by_type: dict[str, list[tuple[str, str, str]]] = {
            "entities": [],
            "concepts": [],
            "topics": [],
            "sources": [],
            "synthesis": [],
            "code": [],
        }

        if self.wiki_dir.exists():
            for page_path in sorted(self.wiki_dir.rglob("*.md")):
                if page_path.name in ["index.md", "log.md"]:
                    continue
                category = page_path.parent.name
                if category in by_type:
                    fm, _ = load_yaml_frontmatter(page_path)
                    page_id = fm.get("id") or page_path.stem
                    title = fm.get("title") or page_path.stem
                    rel_path = str(page_path.relative_to(self.wiki_dir))
                    by_type[category].append((page_id, title, rel_path))

        content_lines = [
            "# C64 LLM-Wiki Master Index",
            "",
            f"*Last Updated: {today}*",
            "",
            "Welcome to the C64 LLM-Wiki Knowledge Base. Master content catalog maintained by Wiki Engine.",
            "",
            "---",
            "",
        ]

        for category, items in by_type.items():
            content_lines.append(f"## {category.title()} ({len(items)})")
            if not items:
                content_lines.append("*No compiled pages in this section yet.*")
            else:
                for page_id, title, rel_path in items:
                    content_lines.append(f"- [[{page_id}]] — [{title}]({rel_path})")
            content_lines.append("")

        index_path.parent.mkdir(parents=True, exist_ok=True)
        index_path.write_text("\n".join(content_lines), encoding="utf-8")
        logger.info("wiki_index_rebuilt", total_pages=sum(len(v) for v in by_type.values()))
        return index_path

    def auto_synthesize_topics(self) -> list[Path]:
        """Scans all compiled entity pages and automatically groups them into topic pages."""
        created_topics: list[Path] = []
        topic_groups: dict[str, list[str]] = {}

        for page in sorted(self.wiki_dir.rglob("*.md")):
            if page.parent.name == "entities":
                fm, _ = load_yaml_frontmatter(page)
                page_id = fm.get("id") or page.stem
                tags = fm.get("tags") or []
                for tag in tags:
                    topic_groups.setdefault(tag, []).append(page_id)

        for tag, eids in topic_groups.items():
            if len(eids) >= 1:
                path = self.update_topic_page(tag.replace("-", " ").title(), eids)
                created_topics.append(path)

        return created_topics

    def update_topic_page(self, topic_name: str, entity_ids: list[str]) -> Path:
        """Creates or updates a aggregated topic page under data/wiki/topics/."""
        topic_id = f"topic-{topic_name.lower().replace(' ', '-')}"
        topic_path = self.wiki_dir / "topics" / f"{topic_id}.md"
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        existing_fm: dict[str, Any] = {}
        if topic_path.exists():
            existing_fm, _ = load_yaml_frontmatter(topic_path)

        topic_fm = {
            "id": topic_id,
            "type": "topic",
            "title": f"Topic: {topic_name}",
            "aliases": [topic_name],
            "tags": [topic_name.lower()],
            "sources": existing_fm.get("sources", []),
            "created_at": existing_fm.get("created_at") or today,
            "updated_at": today,
            "status": "stable",
            "contradictions": [],
            "links_out": entity_ids,
        }

        body_lines = [
            f"# Topic: {topic_name}",
            "",
            "Aggregated technical topic page maintained by Wiki Engine.",
            "",
            "## Related Entities & Concepts",
        ]
        for eid in entity_ids:
            body_lines.append(f"- [[{eid}]]")

        write_wiki_page(topic_path, topic_fm, "\n".join(body_lines))
        return topic_path
