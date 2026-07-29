import json
import hashlib
import sqlite3
from pathlib import Path
from typing import List, Dict, Any, Tuple
from cleaners.c64ref_parser import Entity, SourceComment
from cleaners.c64ref_merger import get_slug

def generate_entity_id(module: str, key_id: str) -> str:
    """Generates a unique SHA-1 based ID for the c64ref entity."""
    sha = hashlib.sha1(key_id.encode("utf-8")).hexdigest()[:8]
    return f"c64ref_{module}_{sha}"

class C64RefDatasetBuilder:
    """Updates JSONL dataset, knowledge graph, SQLite search index, and main documentation index."""
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.jsonl_path = data_dir / "dataset" / "scraped_dataset.jsonl"
        self.graph_path = data_dir / "dataset" / "knowledge_graph.json"
        self.db_path = data_dir / "dataset" / "search_index.db"
        self.index_md_path = data_dir / "docs" / "index.md"

    def build(self, entities: List[Entity]) -> None:
        """Executes the full update pipeline."""
        print("=== Updating Dataset & Indexes ===")
        self.update_jsonl(entities)
        self.update_knowledge_graph(entities)
        self.update_sqlite_index(entities)
        self.update_index_md(entities)
        print("=== Dataset & Indexes Updated Successfully ===")

    def get_doc_relative_path(self, entity: Entity) -> str:
        """Computes the relative path from data/docs/ for the entity."""
        module = entity.module
        slug = get_slug(entity)
        filename = f"{slug}.md"

        if module == "c64mem":
            return f"c64ref/memory-map/{filename}"
        elif module == "kernal":
            return f"c64ref/kernal-api/{filename}"
        elif module == "6502":
            return f"c64ref/cpu-instructions/{filename}"
        elif module == "c64disasm":
            addr_val = int(entity.address.replace("$", ""), 16) if entity.address else 0
            subfolder = "basic-rom" if (0xA000 <= addr_val < 0xC000) else "kernal-rom"
            return f"c64ref/rom-disassembly/{subfolder}/{filename}"
        elif module == "c64io":
            addr_val = int(entity.address.replace("$", ""), 16) if entity.address else 0
            if 0xD000 <= addr_val <= 0xD3FF:
                subfolder = "vic-ii"
            elif 0xD400 <= addr_val <= 0xD7FF:
                subfolder = "sid"
            elif 0xDC00 <= addr_val <= 0xDDFF:
                subfolder = "cia"
            else:
                subfolder = ""
            if subfolder:
                return f"c64ref/io-map/{subfolder}/{filename}"
            return f"c64ref/io-map/{filename}"
        return f"c64ref/{filename}"

    def update_jsonl(self, entities: List[Entity]) -> None:
        """Saves or appends c64ref records to scraped_dataset.jsonl without duplicates."""
        existing_records = []
        if self.jsonl_path.exists():
            with open(self.jsonl_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        rec = json.loads(line)
                        # Filter out existing c64ref records to maintain idempotency
                        if not rec.get("id", "").startswith("c64ref_"):
                            existing_records.append(rec)

        new_records = []
        for entity in entities:
            key_id = entity.address if entity.address else entity.symbol
            entity_id = generate_entity_id(entity.module, key_id)

            # Setup metadata
            category = "reference"
            topics = ["assembly"]
            hardware = ["C64"]
            difficulty = "intermediate"

            if entity.module == "c64mem":
                topics = ["memory-map", "zero-page", "rom-layout"]
                difficulty = "beginner" if hex_to_dec(entity.address) < 0x0100 else "intermediate"
            elif entity.module == "kernal":
                topics = ["kernal-api", "system-routines", "jumps"]
            elif entity.module == "6502":
                topics = ["cpu-instructions", "opcodes", "addressing-modes"]
                hardware = ["6502"]
                if entity.opcodes_list and any(op["undocumented"] for op in entity.opcodes_list):
                    difficulty = "advanced"
            elif entity.module == "c64disasm":
                category = "source-code"
                topics = ["rom-disassembly"]
                difficulty = "advanced"
            elif entity.module == "c64io":
                topics = ["io-map"]
                addr_val = hex_to_dec(entity.address)
                if 0xD000 <= addr_val <= 0xD3FF:
                    topics.append("vic-ii-registers")
                    hardware = ["VIC-II"]
                elif 0xD400 <= addr_val <= 0xD7FF:
                    topics.append("sid-registers")
                    hardware = ["SID"]
                elif 0xDC00 <= addr_val <= 0xDDFF:
                    topics.append("cia-registers")
                    hardware = ["CIA"]

            sources_list = [s.source_name for s in entity.sources]

            # Generate body without frontmatter
            # Description is unified text from the highest priority source
            body_text = entity.description if entity.description else entity.heading

            meta = {
                "source": "https://github.com/mist64/c64ref",
                "category": category,
                "topics": topics,
                "difficulty": difficulty,
                "language": "assembly",
                "hardware": hardware,
                "related": entity.related,
                "scraped_at": "2026-07-29",
                "spider": "c64ref",
                "c64ref": {
                    "module": entity.module,
                    "symbol": entity.symbol,
                    "address": entity.address,
                    "sources": sources_list
                }
            }

            new_records.append({
                "id": entity_id,
                "text": body_text,
                "metadata": meta
            })

        all_records = existing_records + new_records

        # Write back to JSONL
        with open(self.jsonl_path, "w", encoding="utf-8") as f:
            for rec in all_records:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    def update_knowledge_graph(self, entities: List[Entity]) -> None:
        """Updates knowledge_graph.json with nodes and edges."""
        graph = {"nodes": [], "edges": []}
        if self.graph_path.exists():
            try:
                graph = json.loads(self.graph_path.read_text(encoding="utf-8"))
            except Exception:
                pass

        # Clean existing c64ref entries
        graph["nodes"] = [n for n in graph.get("nodes", []) if not n.get("id", "").startswith("c64ref/")]
        graph["edges"] = [e for e in graph.get("edges", []) if not (e.get("source", "").startswith("c64ref/") or e.get("target", "").startswith("c64ref/"))]

        # Add new nodes and edges
        new_nodes = []
        new_edges = []

        for entity in entities:
            doc_rel_path = self.get_doc_relative_path(entity)
            new_nodes.append({
                "id": doc_rel_path,
                "type": "document",
                "label": entity.heading
            })

            # Edges to hardware
            hardware_list = []
            if entity.module == "6502":
                hardware_list.append("6502")
            elif entity.module == "c64io":
                addr_val = hex_to_dec(entity.address)
                if 0xD000 <= addr_val <= 0xD3FF:
                    hardware_list.append("VIC-II")
                elif 0xD400 <= addr_val <= 0xD7FF:
                    hardware_list.append("SID")
                elif 0xDC00 <= addr_val <= 0xDDFF:
                    hardware_list.append("CIA")
            else:
                hardware_list.append("C64")

            for hw in hardware_list:
                new_edges.append({
                    "source": doc_rel_path,
                    "target": hw,
                    "relation": "related_to_hardware"
                })

            # Edges to related documents
            for rel in entity.related:
                # Target path can be derived roughly
                # For simplicity, we can link them if they are documents
                pass

        graph["nodes"].extend(new_nodes)
        graph["edges"].extend(new_edges)

        # Save back as pretty JSON
        self.graph_path.write_text(json.dumps(graph, indent=2, ensure_ascii=False), encoding="utf-8")

    def update_sqlite_index(self, entities: List[Entity]) -> None:
        """Deletes old c64ref and inserts new documents & routines into search_index.db."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # 1. Clean existing records
        cursor.execute("DELETE FROM documents WHERE id LIKE 'c64ref_%'")
        cursor.execute("DELETE FROM documents_fts WHERE id LIKE 'c64ref_%'")
        cursor.execute("DELETE FROM routines WHERE doc_id LIKE 'c64ref_%'")

        # 2. Insert new documents and virtual FTS records
        for entity in entities:
            key_id = entity.address if entity.address else entity.symbol
            entity_id = generate_entity_id(entity.module, key_id)
            doc_rel_path = self.get_doc_relative_path(entity)

            category = "reference"
            topics = ["assembly"]
            hardware = "C64"
            difficulty = "intermediate"

            if entity.module == "c64mem":
                topics = ["memory-map", "zero-page", "rom-layout"]
                difficulty = "beginner" if hex_to_dec(entity.address) < 0x0100 else "intermediate"
            elif entity.module == "kernal":
                topics = ["kernal-api", "system-routines", "jumps"]
            elif entity.module == "6502":
                topics = ["cpu-instructions", "opcodes", "addressing-modes"]
                hardware = "6502"
                if entity.opcodes_list and any(op["undocumented"] for op in entity.opcodes_list):
                    difficulty = "advanced"
            elif entity.module == "c64disasm":
                category = "source-code"
                topics = ["rom-disassembly"]
                difficulty = "advanced"
            elif entity.module == "c64io":
                topics = ["io-map"]
                addr_val = hex_to_dec(entity.address)
                if 0xD000 <= addr_val <= 0xD3FF:
                    topics.append("vic-ii-registers")
                    hardware = "VIC-II"
                elif 0xD400 <= addr_val <= 0xD7FF:
                    topics.append("sid-registers")
                    hardware = "SID"
                elif 0xDC00 <= addr_val <= 0xDDFF:
                    topics.append("cia-registers")
                    hardware = "CIA"

            body_text = entity.description if entity.description else entity.heading
            source_file_rel = f"{entity.module}.txt"
            source_url = f"https://github.com/mist64/c64ref/blob/main/src/{entity.module}/{source_file_rel}"

            # Standard documents table
            cursor.execute("""
                INSERT INTO documents (id, filepath, title, source_url, category, difficulty, language, hardware, topics, body)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                entity_id,
                doc_rel_path,
                entity.heading,
                source_url,
                category,
                difficulty,
                "assembly",
                hardware,
                ",".join(topics),
                body_text
            ))

            # Virtual FTS table
            cursor.execute("""
                INSERT INTO documents_fts (id, title, category, difficulty, language, hardware, topics, body)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                entity_id,
                entity.heading,
                category,
                difficulty,
                "assembly",
                hardware,
                ",".join(topics),
                body_text
            ))

            # If KERNAL API, insert into routines
            if entity.module == "kernal":
                cursor.execute("""
                    INSERT INTO routines (name, address, description, source_url, doc_id)
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    entity.symbol,
                    entity.address,
                    entity.heading,
                    source_url,
                    entity_id
                ))

        conn.commit()
        conn.close()

    def update_index_md(self, entities: List[Entity]) -> None:
        """Parses, filters, and rebuilds data/docs/index.md to include new references."""
        if not self.index_md_path.exists():
            return

        content = self.index_md_path.read_text(encoding="utf-8")

        # Group lines under categories
        # Let's find sections like ## reference, ## source-code, etc.
        sections_dict: Dict[str, List[str]] = {}
        current_section = None

        for line in content.splitlines():
            line_stripped = line.strip()
            if line_stripped.startswith("## "):
                current_section = line_stripped[3:].strip()
                sections_dict[current_section] = []
            elif current_section:
                if line_stripped.startswith("- ["):
                    # Check if it already references c64ref, skip to avoid duplicates
                    if "(c64ref/" not in line_stripped:
                        sections_dict[current_section].append(line_stripped)
                elif line_stripped != "":
                    # Skip other random lines or empty lines under sections, but we want to retain the main header
                    pass

        # Now, append our new entities to reference and source-code lists
        for entity in entities:
            doc_rel_path = self.get_doc_relative_path(entity)
            item = f"- [{entity.heading}]({doc_rel_path})"

            if entity.module == "c64disasm":
                sections_dict.setdefault("source-code", []).append(item)
            else:
                sections_dict.setdefault("reference", []).append(item)

        # Deduplicate and sort sections alphabetically
        for sec in sections_dict:
            sections_dict[sec] = sorted(list(set(sections_dict[sec])))

        # Reconstruct index.md cleanly
        rebuilt_parts = [
            "# Indice — Manuale di programmazione per Commodore 64\n",
            "> Documentazione aggiornata il 1785145870.6636875\n"
        ]

        # Sort section keys to keep index consistent
        for sec_name in sorted(sections_dict.keys()):
            rebuilt_parts.append(f"## {sec_name}\n")
            for item in sections_dict[sec_name]:
                rebuilt_parts.append(item)
            rebuilt_parts.append("") # blank line after section

        self.index_md_path.write_text("\n".join(rebuilt_parts).strip() + "\n", encoding="utf-8")

def hex_to_dec(hex_str: str) -> int:
    """Safely converts hex string like $D012 to decimal integer."""
    if not hex_str:
        return 0
    try:
        return int(hex_str.replace("$", ""), 16)
    except ValueError:
        return 0
