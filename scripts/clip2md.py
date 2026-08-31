#!/usr/bin/env python3
"""Web clipping converter script (HTML/URL -> Markdown with YAML frontmatter).

Part of the C64-KB-Agent ingestion pipeline (Fase 2).
"""

import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml


def clip_content_to_markdown(
    title: str,
    source_url: str,
    body_text: str,
    output_dir: Path,
    category: str = "reference",
    topics: list[str] | None = None,
    language: str = "assembly",
) -> Path:
    """Save web-clipped content into a Schema-compliant Markdown file with YAML frontmatter.

    Args:
        title: Article or page title.
        source_url: Original web URL.
        body_text: Main article content in Markdown or plain text.
        output_dir: Target directory.
        category: Article category.
        topics: List of topics/tags.
        language: Programming language context.

    Returns:
        Path to generated Markdown file.
    """
    if topics is None:
        topics = ["c64", "reference"]

    output_dir.mkdir(parents=True, exist_ok=True)

    slug = title.lower().replace(" ", "-").replace("/", "-").replace("_", "-")
    slug = "".join(c for c in slug if c.isalnum() or c == "-")

    frontmatter = {
        "title": title,
        "source_url": source_url,
        "category": category,
        "topics": topics,
        "difficulty": "intermediate",
        "language": language,
        "hardware": ["c64"],
        "related": [],
        "scraped_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "content_sha256": hashlib.sha256(body_text.encode("utf-8")).hexdigest(),
    }

    yaml_header = yaml.dump(frontmatter, sort_keys=False, allow_unicode=True)
    full_content = f"---\n{yaml_header}---\n\n# {title}\n\n{body_text}\n"

    output_file = output_dir / f"{slug}.md"
    output_file.write_text(full_content, encoding="utf-8")
    return output_file


def main() -> None:
    if len(sys.argv) < 4:
        print("Usage: python clip2md.py <title> <source_url> <text_file_or_content> <output_dir>")
        sys.exit(1)

    title = sys.argv[1]
    source_url = sys.argv[2]
    content_arg = sys.argv[3]
    output_dir = Path(sys.argv[4])

    content_path = Path(content_arg)
    if content_path.exists() and content_path.is_file():
        body_text = content_path.read_text(encoding="utf-8")
    else:
        body_text = content_arg

    out_path = clip_content_to_markdown(title, source_url, body_text, output_dir)
    print(f"Successfully clipped '{title}' -> {out_path}")


if __name__ == "__main__":
    main()
