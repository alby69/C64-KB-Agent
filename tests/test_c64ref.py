import json
import sqlite3
import unittest
from pathlib import Path
import yaml

from cleaners.c64ref_dataset_builder import C64RefDatasetBuilder
from cleaners.c64ref_markdown_writer import C64RefMarkdownWriter
from cleaners.c64ref_merger import C64RefMerger, get_slug
from cleaners.c64ref_parser import C64DisasmParser, C64MemParser, CPU6502Parser, Entity
from c64_kb_agent.db import DatabaseDAO

BASE_PATH = Path(__file__).resolve().parent.parent
C64REF_SRC = BASE_PATH / "data" / "sources" / "c64ref" / "src"


class TestC64RefParser(unittest.TestCase):
    @unittest.skipUnless(
        (C64REF_SRC / "c64mem" / "c64mem_jb.txt").exists(),
        "c64ref submodule not checked out",
    )
    def test_parse_memory_map_jb(self):
        parser = C64MemParser()
        file_path = C64REF_SRC / "c64mem" / "c64mem_jb.txt"

        entities = parser.parse_file(file_path)
        self.assertTrue(len(entities) > 50)
        self.assertEqual(entities[0].address, "$0000")
        self.assertEqual(entities[0].symbol, "D6510")
        self.assertIn("Chip directional register", entities[0].heading)

    @unittest.skipUnless(
        (C64REF_SRC / "c64disasm" / "c64disasm_en.txt").exists(),
        "c64ref submodule not checked out",
    )
    def test_parse_disassembly_en(self):
        parser = C64DisasmParser()
        file_path = C64REF_SRC / "c64disasm" / "c64disasm_en.txt"

        entities = parser.parse_file(file_path)
        self.assertTrue(len(entities) > 10)
        self.assertEqual(entities[0].address, "$A000")
        self.assertEqual(entities[0].heading, "start of the BASIC ROM")

    @unittest.skipUnless(
        (C64REF_SRC / "6502" / "cpu_6502.txt").exists(),
        "c64ref submodule not checked out",
    )
    def test_parse_cpu_6502(self):
        parser = CPU6502Parser()
        file_path = C64REF_SRC / "6502" / "cpu_6502.txt"

        entities = parser.parse_file(file_path)
        self.assertTrue(len(entities) > 30)

        lda_entities = [e for e in entities if e.symbol == "LDA"]
        self.assertEqual(len(lda_entities), 1)
        self.assertIn("Load Accumulator", lda_entities[0].heading)
        self.assertEqual(lda_entities[0].category, "load")
        self.assertEqual(lda_entities[0].flags, "N-----Z-")


class TestC64RefMerger(unittest.TestCase):
    def test_slug_generation(self):
        entity = Entity(
            module="c64mem",
            address="$D012",
            address_end=None,
            symbol="RASTER",
            heading="Current Raster Line",
            description="",
            sources=[],
            related=[],
        )
        self.assertEqual(get_slug(entity), "d012-raster")

    def test_merge_entities(self):
        from cleaners.c64ref_parser import SourceComment

        entity1 = Entity(
            module="c64mem",
            address="$D012",
            address_end=None,
            symbol="RASTER",
            heading="Heading 1",
            description="Comment 1",
            sources=[],
            related=[],
        )
        entity1.sources = [
            SourceComment(source_name="Source 1", author="Author 1", text="Comment 1", priority=3)
        ]

        entity2 = Entity(
            module="c64mem",
            address="$D012",
            address_end=None,
            symbol="RASTER",
            heading="Heading 2",
            description="Comment 2",
            sources=[],
            related=[],
        )
        entity2.sources = [
            SourceComment(source_name="Source 2", author="Author 2", text="Comment 2", priority=5)
        ]

        merger = C64RefMerger()
        merger.build_global_slug_map([entity1, entity2])
        merged = merger.merge_entities([entity1, entity2])

        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0].description, "Comment 2")
        self.assertEqual(len(merged[0].sources), 2)


class TestC64RefDatabase(unittest.TestCase):
    def test_database_indexing_and_query(self):
        db_path = BASE_PATH / "data" / "dataset" / "search_index.db"

        dao = DatabaseDAO(db_path=db_path)
        has_table = False
        if db_path.exists():
            try:
                conn = sqlite3.connect(db_path)
                tbl = conn.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name='documents'"
                ).fetchone()
                has_table = bool(tbl)
                conn.close()
            except Exception:
                has_table = False

        if not has_table:
            dao.rebuild_index()

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT id, title, category FROM documents LIMIT 5")
        rows = cursor.fetchall()
        self.assertTrue(len(rows) > 0)

        cursor.execute(
            "SELECT id, title FROM documents_fts WHERE documents_fts MATCH 'RASTER' LIMIT 5"
        )
        fts_rows = cursor.fetchall()
        self.assertTrue(len(fts_rows) > 0)

        conn.close()
