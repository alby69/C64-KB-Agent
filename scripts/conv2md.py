#!/usr/bin/env python3
"""Local document converter script (PDF/EPUB/DOCX/TXT/MD -> Markdown with YAML frontmatter).

Part of the C64-KB-Agent ingestion pipeline (Fase 2).
"""

import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml


def calculate_sha256(filepath: Path) -> str:
    """Calculate SHA256 hash of a file."""
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()


def convert_text_to_markdown(filepath: Path) -> str:
    """Read a text, markdown, or binary document and return its string body."""
    suffix = filepath.suffix.lower()

    # Try PyMuPDF/fitz for PDF if installed
    if suffix == ".pdf":
        try:
            import fitz  # PyMuPDF

            doc = fitz.open(filepath)
            text_pages = [page.get_text() for page in doc]
            return "\n\n".join(text_pages)
        except ImportError:
            pass

    # Try python-docx for DOCX if installed
    if suffix == ".docx":
        try:
            import docx

            doc = docx.Document(filepath)
            return "\n\n".join(p.text for p in doc.paragraphs if p.text)
        except ImportError:
            pass

    # Fallback text reading with safe encoding handling
    try:
        return filepath.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        content_bytes = filepath.read_bytes()
        # Filter printable ASCII characters if binary file
        printable = bytes(c for c in content_bytes if 32 <= c <= 126 or c in (9, 10, 13))
        return printable.decode("ascii", errors="ignore")


def convert_file_to_markdown(
    input_path: Path,
    output_dir: Path,
    category: str = "manual",
    topics: list[str] | None = None,
    language: str = "assembly",
) -> Path:
    """Convert an input document file to a validated Markdown file with YAML frontmatter.

    Args:
        input_path: Source file path.
        output_dir: Target directory for converted Markdown file.
        category: Document category (e.g. manual, reference, tutorial).
        topics: List of topic tags.
        language: Programming language context (assembly, basic, mixed, none).

    Returns:
        Path to generated Markdown file.
    """
    if topics is None:
        topics = ["c64", "hardware", "manual"]

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    output_dir.mkdir(parents=True, exist_ok=True)

    body_text = convert_text_to_markdown(input_path)
    file_hash = calculate_sha256(input_path)

    title = input_path.stem.replace("_", " ").replace("-", " ").title()
    slug = input_path.stem.lower().replace("_", "-")

    frontmatter = {
        "title": f"C64 Manual — {title}",
        "source_url": f"file://{input_path.resolve()}",
        "category": category,
        "topics": topics,
        "difficulty": "intermediate",
        "language": language,
        "hardware": ["c64"],
        "related": [],
        "scraped_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "source_sha256": file_hash,
    }

    yaml_header = yaml.dump(frontmatter, sort_keys=False, allow_unicode=True)
    full_content = f"---\n{yaml_header}---\n\n# {title}\n\n{body_text}\n"

    output_file = output_dir / f"{slug}.md"
    output_file.write_text(full_content, encoding="utf-8")
    return output_file


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python conv2md.py <input_file> <output_dir> [category]")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    category = sys.argv[3] if len(sys.argv) > 3 else "manual"

    out_path = convert_file_to_markdown(input_file, output_dir, category=category)
    print(f"Successfully converted {input_file} -> {out_path}")


if __name__ == "__main__":
    main()
