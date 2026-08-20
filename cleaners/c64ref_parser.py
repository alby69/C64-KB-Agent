import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# Sources metadata lookup from Appendix A of the Technical Specification
SOURCES_METADATA = {
    # c64mem
    "c64mem_sheldon.txt": ("Mapping the Commodore 64", "Sheldon Leemon", 3, "en"),
    "c64mem_hauck.txt": ("Memory Map mit Wandervorschlägen", "Dr. H. Hauck", 2, "de"),
    "c64mem_64intern.txt": ("Commodore-64-intern-Buch", "Commodore", 4, "de"),
    "c64mem_jb.txt": ("Memory Map", "Jim Butterfield", 3, "en"),
    "c64mem_mapc64.txt": ("Mapping the Commodore 64", "Sheldon Leemon", 3, "en"),
    "c64mem_prg.txt": ("C64 Programmer's Reference Guide", "Commodore", 4, "en"),
    "c64mem_src.txt": ("Original Source Comments", "Microsoft/Commodore", 5, "en"),
    "c64mem_sta.txt": ("Reference", "Joe Forster / STA", 3, "en"),
    "c64mem_64er.txt": ("64'er Magazin", "64'er", 2, "de"),
    "c64mem_64map.txt": ("64map", "—", 2, "en"),
    # c64disasm
    "c64disasm_cbm.txt": ("Original Disassembly", "Commodore", 5, "en"),
    "c64disasm_de.txt": ("Commodore-64-intern-Buch", "Commodore", 4, "de"),
    "c64disasm_en.txt": ("Original Disassembly", "—", 5, "en"),
    "c64disasm_mm.txt": ("Marko Mäkelä", "Marko Mäkelä", 3, "en"),
    "c64disasm_mn.txt": ("Magnus Nyman", "Magnus Nyman", 3, "en"),
    "c64disasm_ms.txt": ("Lee Davison", "Lee Davison", 4, "en"),
    "c64disasm_sc.txt": ("Bob Sander-Cederlof", "Bob Sander-Cederlof", 3, "en"),
    # kernal
    "kernal_prg.txt": ("C64 Programmer's Reference Guide", "Commodore", 5, "en"),
    "kernal_dh.txt": ("COMPUTE!'s Tool Kit: Kernal", "Dan Heeb", 3, "en"),
    "kernal_mlr.txt": ("Machine Language Routines", "Todd D Heimarck", 3, "en"),
    "kernal_mapc64.txt": ("Mapping the Commodore 64", "Sheldon Leemon", 3, "en"),
    "kernal_128intern.txt": ("Commodore 128 intern", "Jörg Schieb et al.", 2, "en"),
    "kernal_ld.txt": ("Commented ROM Disassembly", "Lee Davison", 4, "en"),
    "kernal_pm.txt": ("Cracking The Kernal", "Peter Marcotty", 3, "en"),
    "kernal_ct.txt": ("Kernal 64 / 128", "Craig Taylor", 3, "en"),
    "kernal_sta.txt": ("Standard KERNAL Functions", "Joe Forster / STA", 4, "en"),
    "kernal_fk.txt": ("C64 KERNAL jump table", "Frank Kontros", 3, "en"),
    "kernal_64intern.txt": ("Das neue Commodore-64-intern-Buch", "Baloui et al.", 3, "de"),
    # c64io
    "c64io_mapc64.txt": ("Mapping the Commodore 64", "Sheldon Leemon", 3, "en"),
    "c64io_prg.txt": ("C64 Programmer's Reference Guide", "Commodore", 4, "en"),
}


@dataclass
class SourceComment:
    source_name: str
    author: str
    text: str
    priority: int  # per ordinamento fonti


@dataclass
class Entity:
    module: str
    address: str | None  # e.g., "$D012"
    address_end: str | None  # e.g., "$D013"
    symbol: str | None  # e.g., "RASTER"
    heading: str
    description: str
    sources: list[SourceComment]
    related: list[str]
    disasm_lines: list[dict[str, Any]] | None = (
        None  # to store raw disassembly lines for disasm module
    )
    category: str | None = None  # 6502 custom fields
    flags: str | None = None  # 6502 custom fields
    formula: str | None = None  # 6502 custom fields
    opcodes_list: list[dict[str, Any]] | None = None  # 6502 custom fields


class C64RefParser:
    """Base parser class for c64ref txt source files."""

    def __init__(self, module: str):
        self.module = module

    def extract_cross_references(self, text: str) -> list[str]:
        """Extract internal cross references like addresses ($XXXX) and symbols from text."""
        refs = []
        # Find $XXXX addresses
        addresses = re.findall(r"(\$[0-9A-Fa-f]{4})", text)
        for addr in addresses:
            refs.append(addr.upper())

        # Find potential uppercase symbols (e.g. RASTER, VICCR0)
        symbols = re.findall(r"\b([A-Z][A-Z0-9_]{2,9})\b", text)
        for sym in symbols:
            if sym not in [
                "AND",
                "NOT",
                "FOR",
                "GET",
                "VAL",
                "LEN",
                "OR",
                "LET",
                "DIM",
                "SQR",
                "SGN",
            ]:
                refs.append(sym)

        return sorted(set(refs))


class C64MemParser(C64RefParser):
    """Memory Map Parser."""

    def __init__(self):
        super().__init__("c64mem")

    def parse_file(self, filepath: Path) -> list[Entity]:
        return self._parse_fixed_columns(filepath)

    def _parse_fixed_columns(self, filepath: Path) -> list[Entity]:
        filename = filepath.name
        metadata = SOURCES_METADATA.get(
            filename, (filename.replace(".txt", ""), "Unknown", 1, "en")
        )
        source_name, author, priority, lang = metadata

        entities = []
        current_entity = None

        with open(filepath, encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            line_stripped = line.rstrip("\r\n")
            if line_stripped.startswith("-") or line_stripped.startswith("#"):
                continue

            match = re.match(r"^(\$[0-9A-Fa-f]{4})(?:-(\$[0-9A-Fa-f]{4}))?", line_stripped)
            if match:
                if current_entity:
                    entities.append(current_entity)

                addr_start = match.group(1).upper()
                addr_end = match.group(2).upper() if match.group(2) else None

                symbol_raw = line_stripped[13:21].strip() if len(line_stripped) > 13 else ""
                symbol = (
                    symbol_raw
                    if (
                        symbol_raw
                        and not any(c in symbol_raw for c in " -*+=;:.,/?!~`@#$%^&()[]{}|\\")
                    )
                    else None
                )

                desc_raw = line_stripped[21:] if len(line_stripped) > 21 else ""
                heading = desc_raw.strip()

                current_entity = Entity(
                    module=self.module,
                    address=addr_start,
                    address_end=addr_end,
                    symbol=symbol,
                    heading=heading,
                    description=desc_raw,
                    sources=[],
                    related=[],
                )
            elif current_entity and (line_stripped.startswith(" ") or line_stripped == ""):
                content = line_stripped[21:] if len(line_stripped) > 21 else line_stripped.lstrip()
                current_entity.description += "\n" + content

        if current_entity:
            entities.append(current_entity)

        for entity in entities:
            desc_lines = entity.description.split("\n")
            heading_lines = []
            body_lines = []
            in_body = False
            for line in desc_lines:
                if not in_body:
                    if line.strip() == "":
                        in_body = True
                    else:
                        heading_lines.append(line.strip())
                else:
                    body_lines.append(line)

            entity.heading = " ".join(heading_lines).strip()
            if entity.heading.endswith("."):
                entity.heading = entity.heading[:-1].strip()

            entity.description = "\n".join(body_lines).strip()
            entity.sources = [
                SourceComment(
                    source_name=source_name,
                    author=author,
                    text=entity.description if entity.description else entity.heading,
                    priority=priority,
                )
            ]
            entity.related = self.extract_cross_references(
                entity.description + " " + entity.heading
            )

        return entities


class C64IOParser(C64MemParser):
    """I/O Map Parser."""

    def __init__(self):
        # We call the super init with c64io
        super().__init__()
        self.module = "c64io"


class KernalParser(C64MemParser):
    """KERNAL API Parser."""

    def __init__(self):
        super().__init__()
        self.module = "kernal"


class C64DisasmParser(C64RefParser):
    """ROM Disassembly Parser."""

    def __init__(self):
        super().__init__("c64disasm")

    def parse_file(self, filepath: Path) -> list[Entity]:
        filename = filepath.name
        metadata = SOURCES_METADATA.get(
            filename, (filename.replace(".txt", ""), "Unknown", 1, "en")
        )
        source_name, author, priority, lang = metadata

        with open(filepath, encoding="utf-8") as f:
            lines = f.readlines()

        entities = []
        current_heading = "start of the ROM"
        current_lines = []
        section_start_addr = None

        for line in lines:
            line_stripped = line.rstrip("\r\n")
            if line_stripped.startswith("-") or line_stripped.startswith("#"):
                continue

            # Check for section heading: 16+ leading spaces and "***"
            if "***" in line_stripped and line_stripped.startswith(" " * 12):
                if current_lines and section_start_addr:
                    entities.append(
                        self._create_entity(
                            current_heading,
                            current_lines,
                            section_start_addr,
                            source_name,
                            author,
                            priority,
                            filepath,
                        )
                    )
                current_heading = line_stripped.replace("***", "").strip()
                current_lines = []
                section_start_addr = None
                continue

            # Check for assembly code/data line
            match = re.match(r"^\.([,:])([0-9A-Fa-f]{4})", line_stripped)
            if match:
                addr = match.group(2).upper()
                if not section_start_addr:
                    section_start_addr = f"${addr}"

                kind = "code" if match.group(1) == "," else "data"
                code_part = line_stripped[6:32].strip() if len(line_stripped) > 6 else ""
                comment_part = line_stripped[32:].strip() if len(line_stripped) > 32 else ""

                current_lines.append(
                    {"addr": f"${addr}", "kind": kind, "code": code_part, "comment": comment_part}
                )
            else:
                if current_lines and line_stripped.startswith(" " * 30) and line_stripped.strip():
                    comment_overflow = line_stripped.strip()
                    if current_lines[-1]["comment"]:
                        current_lines[-1]["comment"] += " " + comment_overflow
                    else:
                        current_lines[-1]["comment"] = comment_overflow

        if current_lines and section_start_addr:
            entities.append(
                self._create_entity(
                    current_heading,
                    current_lines,
                    section_start_addr,
                    source_name,
                    author,
                    priority,
                    filepath,
                )
            )

        return entities

    def _create_entity(
        self,
        heading: str,
        lines: list[dict[str, Any]],
        start_addr: str,
        source_name: str,
        author: str,
        priority: int,
        filepath: Path,
    ) -> Entity:
        comments = []
        for line in lines:
            if line["comment"]:
                comments.append(f"- **{line['addr']}**: {line['comment']}")

        comments_block = "\n".join(comments) if comments else "Nessun commento disponibile."

        symbol = heading.lower().replace(" ", "-")
        symbol = re.sub(r"[^a-z0-9\-]", "", symbol)
        symbol = re.sub(r"\-+", "-", symbol).strip("-")

        end_addr = lines[-1]["addr"] if lines else start_addr

        entity = Entity(
            module="c64disasm",
            address=start_addr,
            address_end=end_addr,
            symbol=symbol,
            heading=heading,
            description=comments_block,
            sources=[
                SourceComment(
                    source_name=source_name, author=author, text=comments_block, priority=priority
                )
            ],
            related=[],
            disasm_lines=lines,
        )
        entity.related = self.extract_cross_references(comments_block + " " + heading)
        return entity


class CPU6502Parser(C64RefParser):
    """6502 CPU Instructions Parser."""

    def __init__(self):
        super().__init__("6502")

    def parse_file(self, filepath: Path) -> list[Entity]:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        sections = {}
        current_section = None
        current_lines = []

        for line in content.splitlines():
            line_stripped = line.strip()
            if line_stripped.startswith("##"):
                continue
            if line_stripped.startswith("[") and line_stripped.endswith("]"):
                if current_section:
                    sections[current_section] = current_lines
                current_section = line_stripped[1:-1]
                current_lines = []
            else:
                current_lines.append(line)

        if current_section:
            sections[current_section] = current_lines

        # 1. mnemos
        mnemos = {}
        for line in sections.get("mnemos", []):
            if not line.strip():
                continue
            parts = line.split(None, 1)
            if len(parts) == 2:
                mnemos[parts[0].strip()] = parts[1].strip()

        # 2. operations
        operations = {}
        for line in sections.get("operations", []):
            if not line.strip():
                continue
            parts = line.split(None, 3)
            if len(parts) >= 3:
                mnemonic = parts[0].strip()
                category = parts[1].strip()
                flags = parts[2].strip()
                formula = parts[3].strip() if len(parts) == 4 else ""
                operations[mnemonic] = {"category": category, "flags": flags, "formula": formula}

        # 3. addmodes
        addmodes = {}
        for line in sections.get("addmodes", []):
            if not line.strip():
                continue
            parts = line.split(None, 3)
            if len(parts) >= 3:
                mode_code = parts[0].strip()
                num_bytes = parts[1].strip()
                syntax = parts[2].strip()
                name = parts[3].strip() if len(parts) == 4 else ""
                addmodes[mode_code] = {"bytes": num_bytes, "syntax": syntax, "name": name}

        # 4. opcodes
        opcodes = {}
        for line in sections.get("opcodes", []):
            if not line.strip():
                continue
            parts = line.split(None, 2)
            if len(parts) >= 2:
                hex_opcode = parts[0].strip()
                mnemonic = parts[1].strip()
                mode_code = parts[2].strip() if len(parts) == 3 else "-"
                is_undocumented = mnemonic.startswith("*")
                clean_mnemonic = mnemonic.lstrip("*")
                opcodes[hex_opcode] = {
                    "mnemonic": clean_mnemonic,
                    "mode_code": mode_code,
                    "undocumented": is_undocumented,
                }

        # 5. timing
        timing = {}
        for line in sections.get("timing", []):
            if not line.strip():
                continue
            parts = line.split(None, 1)
            if len(parts) == 2:
                timing[parts[0].strip()] = parts[1].strip()

        # 6. documentation-mnemos
        doc_mnemos = {}
        current_doc_mnemonic = None
        current_doc_lines = []
        for line in sections.get("documentation-mnemos", []):
            if line and not line.startswith(" "):
                if current_doc_mnemonic:
                    doc_mnemos[current_doc_mnemonic] = "\n".join(current_doc_lines).strip()
                parts = line.split(None, 1)
                current_doc_mnemonic = parts[0].strip().lstrip("*")
                current_doc_lines = [parts[1].strip()] if len(parts) == 2 else []
            elif current_doc_mnemonic:
                current_doc_lines.append(line)
        if current_doc_mnemonic:
            doc_mnemos[current_doc_mnemonic] = "\n".join(current_doc_lines).strip()

        entities = []
        all_mnemonics = set(mnemos.keys()) | set(doc_mnemos.keys())
        for raw_mnemonic in all_mnemonics:
            clean_mnemonic = raw_mnemonic.lstrip("*")

            short_desc = mnemos.get(raw_mnemonic, mnemos.get(clean_mnemonic, ""))
            op_info = operations.get(raw_mnemonic, operations.get(clean_mnemonic, {}))
            category = op_info.get("category", "unknown")
            flags = op_info.get("flags", "--------")
            formula = op_info.get("formula", "")
            detailed_doc = doc_mnemos.get(clean_mnemonic, doc_mnemos.get(raw_mnemonic, ""))

            mnemonic_opcodes = []
            for hex_op, op_info_item in opcodes.items():
                if op_info_item["mnemonic"] == clean_mnemonic:
                    mode_code = op_info_item["mode_code"]
                    cycles = timing.get(hex_op, "unknown")
                    mode_info = addmodes.get(
                        mode_code, {"bytes": "1", "syntax": "-", "name": "Implied"}
                    )
                    mnemonic_opcodes.append(
                        {
                            "opcode": hex_op,
                            "mode": mode_info["name"],
                            "syntax": mode_info["syntax"],
                            "bytes": mode_info["bytes"],
                            "cycles": cycles,
                            "undocumented": op_info_item["undocumented"],
                        }
                    )

            mnemonic_opcodes.sort(key=lambda x: x["opcode"])
            heading = f"{clean_mnemonic} — {short_desc}" if short_desc else clean_mnemonic

            entity = Entity(
                module="6502",
                address=None,
                address_end=None,
                symbol=clean_mnemonic.upper(),
                heading=heading,
                description=detailed_doc,
                sources=[
                    SourceComment(
                        source_name="6502 Reference",
                        author="MOS Technology",
                        text=detailed_doc,
                        priority=5,
                    )
                ],
                related=[],
            )
            entity.category = category
            entity.flags = flags
            entity.formula = formula
            entity.opcodes_list = mnemonic_opcodes
            entity.related = self.extract_cross_references(detailed_doc + " " + heading)

            entities.append(entity)

        return entities
