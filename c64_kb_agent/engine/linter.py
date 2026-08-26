"""Wiki linter module for C64 LLM-Wiki Engine.

Scans data/wiki/ for broken links, orphan pages, schema validation errors, and flagged contradictions.
"""

import re
from pathlib import Path
from typing import Any

from jsonschema import ValidationError, validate

from c64_kb_agent.config import settings
from c64_kb_agent.engine.ingestor import load_yaml_frontmatter
from c64_kb_agent.utils.logging import logger


class WikiLinter:
    """Linter engine running quality and schema health checks on data/wiki/."""

    def __init__(self, wiki_dir: Path | None = None) -> None:
        self.wiki_dir = wiki_dir or (settings.base_dir / "data" / "wiki")
        self.schema_path = settings.schemas_dir / "wiki_page.schema.json"
        self.schema = self._load_schema()

    def _load_schema(self) -> dict[str, Any]:
        import json

        with open(self.schema_path, encoding="utf-8") as f:
            data = json.load(f)
            return dict(data) if isinstance(data, dict) else {}

    def lint_wiki(self) -> dict[str, Any]:
        """Runs full lint analysis over all compiled wiki pages.

        Returns dict report containing invalid_schema, broken_links, orphans, and flagged_contradictions.
        """
        all_pages = [
            p
            for p in self.wiki_dir.rglob("*.md")
            if p.is_file() and p.name not in ["index.md", "log.md"]
        ]

        valid_ids: set[str] = set()
        page_links: dict[str, list[str]] = {}
        inbound_count: dict[str, int] = {}
        invalid_schema: list[dict[str, str]] = []
        flagged_contradictions: list[dict[str, Any]] = []

        for p in all_pages:
            fm, _ = load_yaml_frontmatter(p)
            rel_p = str(p.relative_to(self.wiki_dir))

            try:
                validate(instance=fm, schema=self.schema)
            except ValidationError as e:
                invalid_schema.append({"path": rel_p, "error": e.message})
                continue

            page_id = fm.get("id", p.stem)
            valid_ids.add(page_id)
            links = fm.get("links_out", [])
            page_links[page_id] = links

            if fm.get("status") == "contradiction_flagged" or fm.get("contradictions"):
                flagged_contradictions.append(
                    {
                        "id": page_id,
                        "path": rel_p,
                        "contradictions": fm.get("contradictions", []),
                    }
                )

        for links in page_links.values():
            for target_id in links:
                inbound_count[target_id] = inbound_count.get(target_id, 0) + 1

        broken_links: list[dict[str, str]] = []
        for page_id, links in page_links.items():
            for target_id in links:
                if target_id not in valid_ids:
                    broken_links.append({"source_id": page_id, "broken_target_id": target_id})

        orphans: list[str] = [
            pid for pid in valid_ids if inbound_count.get(pid, 0) == 0 and not pid.startswith("topic-")
        ]

        hex_discrepancies: list[dict[str, str]] = []
        for p in all_pages:
            _, body = load_yaml_frontmatter(p)
            rel_p = str(p.relative_to(self.wiki_dir))
            # Check for non-standard 0x hex address formatting vs standard $ prefix
            raw_hexes = re.findall(r"\b0x[0-9a-fA-F]{4}\b", body)
            if raw_hexes:
                hex_discrepancies.append({
                    "path": rel_p,
                    "warning": f"Non-standard hex address format found ({', '.join(set(raw_hexes))}); use '$' prefix."
                })

        report = {
            "total_pages_scanned": len(all_pages),
            "valid_pages": len(valid_ids),
            "invalid_schema": invalid_schema,
            "broken_links": broken_links,
            "orphans": orphans,
            "flagged_contradictions": flagged_contradictions,
            "hex_formatting_warnings": hex_discrepancies,
        }

        logger.info(
            "wiki_lint_completed",
            scanned=len(all_pages),
            invalid=len(invalid_schema),
            broken=len(broken_links),
            orphans=len(orphans),
        )
        return report
