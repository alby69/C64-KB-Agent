"""Unit tests for ingestion converters (scripts/conv2md.py & scripts/clip2md.py)."""

from pathlib import Path

import yaml
from jsonschema import validate

from c64_kb_agent.validators import load_schema
from scripts.clip2md import clip_content_to_markdown
from scripts.conv2md import convert_file_to_markdown


def test_convert_file_to_markdown(tmp_path: Path) -> None:
    source_file = tmp_path / "sample_manual.txt"
    source_file.write_text("VIC-II Chip Registers and Bad Lines details.\n", encoding="utf-8")

    out_dir = tmp_path / "output"
    out_file = convert_file_to_markdown(source_file, out_dir, category="manual")

    assert out_file.exists()
    content = out_file.read_text(encoding="utf-8")
    assert content.startswith("---")
    assert "# Sample Manual" in content

    parts = content.split("---", 2)
    fm = yaml.safe_load(parts[1])
    assert fm["category"] == "manual"
    assert "source_sha256" in fm

    # Validate against document schema
    v1_schema = load_schema("document.schema.json")
    validate(instance=fm, schema=v1_schema)


def test_convert_binary_file_to_markdown(tmp_path: Path) -> None:
    binary_file = tmp_path / "sample_binary.pdf"
    # Write sample binary data with embedded readable text
    binary_file.write_bytes(b"%PDF-1.4\n1 0 obj << /Title (C64 Assembly Guide) >>\nendobj\n")

    out_dir = tmp_path / "output"
    out_file = convert_file_to_markdown(binary_file, out_dir, category="manual")

    assert out_file.exists()
    content = out_file.read_text(encoding="utf-8")
    assert "PDF" in content or "C64" in content


def test_clip_content_to_markdown(tmp_path: Path) -> None:
    out_dir = tmp_path / "clipped"
    out_file = clip_content_to_markdown(
        title="VIC-II Raster Interrupts",
        source_url="https://codebase64.org/doku.php?id=base:raster_interrupts",
        body_text="To set up a raster interrupt, write to register $D012.",
        output_dir=out_dir,
        category="tutorial",
        topics=["vic-ii", "interrupts"],
    )

    assert out_file.exists()
    content = out_file.read_text(encoding="utf-8")
    assert "VIC-II Raster Interrupts" in content

    parts = content.split("---", 2)
    fm = yaml.safe_load(parts[1])
    assert fm["title"] == "VIC-II Raster Interrupts"
    assert fm["category"] == "tutorial"

    # Validate against document schema
    v1_schema = load_schema("document.schema.json")
    validate(instance=fm, schema=v1_schema)
