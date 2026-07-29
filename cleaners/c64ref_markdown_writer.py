import re
from pathlib import Path
from typing import List, Dict, Any, Optional
import yaml
from cleaners.c64ref_parser import Entity, SourceComment
from cleaners.c64ref_merger import get_slug

def hex_to_dec(hex_str: str) -> int:
    """Converts a hex string like $D012 to decimal."""
    try:
        return int(hex_str.replace("$", ""), 16)
    except ValueError:
        return 0

def get_address_size(start: Optional[str], end: Optional[str]) -> str:
    """Computes size in bytes for a given address range."""
    if not start:
        return "N/A"
    try:
        start_val = hex_to_dec(start)
        if not end:
            return "1 byte"
        end_val = hex_to_dec(end)
        size = end_val - start_val + 1
        return f"{size} byte"
    except Exception:
        return "1 byte"

class C64RefMarkdownWriter:
    """Writes merged entities into fully styled Markdown files with YAML frontmatter."""
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir

    def get_output_path(self, entity: Entity) -> Path:
        """Determines the target folder and filename for the entity."""
        module = entity.module
        slug = get_slug(entity)
        filename = f"{slug}.md"

        if module == "c64mem":
            return self.output_dir / "memory-map" / filename
        elif module == "kernal":
            return self.output_dir / "kernal-api" / filename
        elif module == "6502":
            return self.output_dir / "cpu-instructions" / filename
        elif module == "c64disasm":
            # Decide subfolders: basic-rom or kernal-rom based on address
            addr_val = hex_to_dec(entity.address) if entity.address else 0
            if 0xA000 <= addr_val < 0xC000:
                subfolder = "basic-rom"
            elif 0xE000 <= addr_val <= 0xFFFF:
                subfolder = "kernal-rom"
            else:
                subfolder = ""

            if subfolder:
                return self.output_dir / "rom-disassembly" / subfolder / filename
            return self.output_dir / "rom-disassembly" / filename
        elif module == "c64io":
            # Decide subfolders: vic-ii, sid, cia based on address
            addr_val = hex_to_dec(entity.address) if entity.address else 0
            if 0xD000 <= addr_val <= 0xD3FF:
                subfolder = "vic-ii"
            elif 0xD400 <= addr_val <= 0xD7FF:
                subfolder = "sid"
            elif 0xDC00 <= addr_val <= 0xDDFF:
                subfolder = "cia"
            else:
                subfolder = ""

            if subfolder:
                return self.output_dir / "io-map" / subfolder / filename
            return self.output_dir / "io-map" / filename

        return self.output_dir / filename

    def write_entity(self, entity: Entity) -> None:
        """Writes a single merged Entity into its markdown file."""
        target_path = self.get_output_path(entity)
        target_path.parent.mkdir(parents=True, exist_ok=True)

        # Build frontmatter
        frontmatter = self._build_frontmatter(entity)

        # Build body
        body = self._build_body(entity)

        content = f"---\n{frontmatter}---\n\n{body}"
        target_path.write_text(content, encoding="utf-8")

    def _build_frontmatter(self, entity: Entity) -> str:
        """Builds valid YAML frontmatter conforming to C64-KB-Agent's schema."""
        module = entity.module
        addr = entity.address
        sym = entity.symbol if entity.symbol else (entity.heading if module != "6502" else "")

        # Categorization & Topics
        category = "reference"
        topics = []
        hardware = ["C64"]
        difficulty = "intermediate"

        if module == "c64mem":
            category = "reference"
            topics = ["memory-map", "zero-page", "rom-layout"]
            addr_val = hex_to_dec(addr) if addr else 0
            if addr_val < 0x0100:
                topics.append("zero-page")
                difficulty = "beginner"
        elif module == "kernal":
            category = "reference"
            topics = ["kernal-api", "system-routines", "jumps"]
        elif module == "6502":
            category = "reference"
            topics = ["cpu-instructions", "opcodes", "addressing-modes"]
            hardware = ["6502"]
            difficulty = "intermediate"
            if entity.opcodes_list and any(op["undocumented"] for op in entity.opcodes_list):
                difficulty = "advanced"
        elif module == "c64disasm":
            category = "source-code"
            topics = ["rom-disassembly"]
            addr_val = hex_to_dec(addr) if addr else 0
            if 0xA000 <= addr_val < 0xC000:
                topics.append("basic-rom")
            else:
                topics.append("kernal-rom")
            difficulty = "advanced"
        elif module == "c64io":
            category = "reference"
            topics = ["io-map"]
            addr_val = hex_to_dec(addr) if addr else 0
            if 0xD000 <= addr_val <= 0xD3FF:
                topics.append("vic-ii-registers")
                hardware = ["VIC-II"]
            elif 0xD400 <= addr_val <= 0xD7FF:
                topics.append("sid-registers")
                hardware = ["SID"]
            elif 0xDC00 <= addr_val <= 0xDDFF:
                topics.append("cia-registers")
                hardware = ["CIA"]

        # Source files and comments metadata
        source_files = list(set([s.source_name.lower().replace(" ", "_") + ".txt" for s in entity.sources]))
        sources_meta = []
        for s in entity.sources:
            # Short description is the first sentence or heading of the comment
            short_desc = s.text.split("\n")[0].strip() if s.text else ""
            if len(short_desc) > 80:
                short_desc = short_desc[:77] + "..."
            sources_meta.append({
                "name": s.source_name,
                "author": s.author,
                "description": short_desc
            })

        # Base GitHub source URL
        source_file_rel = source_files[0] if source_files else f"{module}.txt"
        source_url = f"https://github.com/mist64/c64ref/blob/main/src/{module}/{source_file_rel}"

        fm_dict = {
            "title": entity.heading,
            "source_url": source_url,
            "category": category,
            "topics": topics,
            "difficulty": difficulty,
            "language": "assembly",
            "hardware": hardware,
            "related": entity.related,
            "scraped_at": "2026-07-29",
            "c64ref": {
                "module": module,
                "source_files": source_files,
                "address": addr,
                "address_end": entity.address_end,
                "symbol": entity.symbol,
                "sources": sources_meta
            }
        }

        # Clean null values
        if not entity.address_end:
            del fm_dict["c64ref"]["address_end"]
        if not entity.symbol:
            del fm_dict["c64ref"]["symbol"]

        return yaml.dump(fm_dict, allow_unicode=True, default_flow_style=False, sort_keys=False)

    def _build_body(self, entity: Entity) -> str:
        """Formulates structured body templates for each type of entity."""
        module = entity.module
        addr = entity.address
        sym = entity.symbol
        title = entity.symbol if sym else (addr if addr else "Reference")

        body_parts = []

        if module in ["c64mem", "c64io"]:
            # Title
            body_parts.append(f"# {title} — {entity.heading} ({addr})")
            body_parts.append("\n## Panoramica\nIl registro o area di memoria " + (sym if sym else addr) + " è descritto in dettaglio di seguito.")

            # Technical Details
            dec_val = hex_to_dec(addr) if addr else 0
            size_bytes = get_address_size(addr, entity.address_end)
            permissions = "R/W"
            # Some standard registers have specific permissions
            if sym in ["POTX", "POTY", "RANDOM", "ENV3", "STATUS", "STKEY", "SFDX"]:
                permissions = "R"
            elif sym in ["FRELO1", "FREHI1", "FRELO2", "FREHI2", "FRELO3", "FREHI3"]:
                permissions = "W"

            body_parts.append(f"""
## Dettagli Tecnici
- **Indirizzo**: `{addr}` (`{dec_val}` decimale)
- **Range**: `{addr}`""" + (f"-`{entity.address_end}`" if entity.address_end else "") + f"""
- **Dimensione**: `{size_bytes}`
- **Permessi**: `{permissions}`""")

            # Source Descriptions
            body_parts.append("\n## Descrizioni per Fonte")
            for source in entity.sources:
                body_parts.append(f"\n### {source.source_name} ({source.author})\n{source.text}")

        elif module == "kernal":
            body_parts.append(f"# {title} — {entity.heading} ({addr})")
            dec_val = hex_to_dec(addr) if addr else 0
            body_parts.append(f"""
## Panoramica
La routine KERNAL `{sym}` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `{addr}`
- **Chiamata**: `JSR {sym}` o `SYS {dec_val}`
""")
            body_parts.append("\n## Note per Fonte")
            for source in entity.sources:
                body_parts.append(f"\n### {source.source_name} ({source.author})\n{source.text}")

        elif module == "6502":
            body_parts.append(f"# {entity.symbol} — {entity.heading}")
            body_parts.append(f"""
## Panoramica
L'istruzione `{entity.symbol}` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `{entity.category}` |
| Formula | `{entity.formula}` |
| Flag alterati | `{entity.flags}` |
""")
            # Addressing modes table
            body_parts.append("\n## Modalità di Indirizzamento")
            body_parts.append("| Modalità | Opcode | Byte | Cicli | Note |")
            body_parts.append("|----------|--------|------|-------|------|")
            for op in (entity.opcodes_list or []):
                undoc_note = "Non documentata" if op["undocumented"] else "Standard"
                body_parts.append(f"| {op['mode']} | `${op['opcode']}` | {op['bytes']} | {op['cycles']} | {undoc_note} |")

            body_parts.append(f"\n## Descrizione\n{entity.description}")

        elif module == "c64disasm":
            body_parts.append(f"# {addr} — {entity.heading}")

            # Format disassembly lines
            disasm_lines = []
            for line in (entity.disasm_lines or []):
                comment_suffix = f"   ; {line['comment']}" if line['comment'] else ""
                disasm_lines.append(f".{line['addr'][1:]}  {line['code']}{comment_suffix}")

            disasm_block = "\n".join(disasm_lines)

            body_parts.append(f"""
## Disassemblatura
```assembly
{disasm_block}
```
""")
            body_parts.append("\n## Commenti")
            for source in entity.sources:
                body_parts.append(f"\n### {source.source_name} ({source.author})\n{source.text}")

        # Footer
        body_parts.append(f"\n---\n*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*")

        return "\n".join(body_parts)
