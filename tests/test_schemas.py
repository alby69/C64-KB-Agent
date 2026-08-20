"""Test del contratto dati: valida i file del dataset contro gli schemi JSON (B3).

Gli schemi vivono in schemas/ e sono l'unico artefatto condiviso tra
C64-KB-Agent (consumatore) e C64-Scrapy (produttore): nessun import di codice.
"""

import json
import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

try:
    import jsonschema
    from jsonschema import validate
except ImportError:  # pragma: no cover
    pytest.skip("jsonschema non installato", allow_module_level=True)

BASE = Path(__file__).resolve().parent.parent
SCHEMAS = BASE / "schemas"
DATASET = BASE / "data" / "dataset"


def _load_schema(name: str) -> dict:
    return json.loads((SCHEMAS / name).read_text(encoding="utf-8"))


def _valid_docs():
    docs_dir = BASE / "data" / "docs"
    # index.md è generato da build_index.py (indice di navigazione),
    # non è un documento prodotto dal contratto Scrapy -> KB-Agent.
    return sorted(
        p for p in docs_dir.rglob("*.md")
        if p.is_file() and p.name != "index.md"
    )


def _parse_frontmatter(path: Path):
    import yaml
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


class TestDocumentSchema:
    def test_all_docs_valid(self):
        schema = _load_schema("document.schema.json")
        docs = _valid_docs()
        assert docs, "Nessun documento trovato in data/docs/"
        invalid = []
        for doc in docs:
            fm = _parse_frontmatter(doc)
            try:
                validate(instance=fm, schema=schema)
            except jsonschema.ValidationError as e:
                invalid.append((str(doc.relative_to(BASE)), e.message))
        assert not invalid, f"Documenti non conformi: {invalid}"


class TestDatasetSchema:
    def test_jsonl_records_valid(self):
        schema = _load_schema("dataset.schema.json")
        path = DATASET / "scraped_dataset.jsonl"
        if not path.is_file():
            pytest.skip("scraped_dataset.jsonl non presente (dati non sincronizzati)")
        invalid = []
        total = 0
        with path.open(encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                total += 1
                try:
                    validate(instance=json.loads(line), schema=schema)
                except (json.JSONDecodeError, jsonschema.ValidationError) as e:
                    invalid.append((line[:80], str(e)))
        assert total > 0, "scraped_dataset.jsonl vuoto"
        assert not invalid, f"Record non conformi ({len(invalid)}/{total})"


class TestKnowledgeGraphSchema:
    def test_knowledge_graph_valid(self):
        schema = _load_schema("knowledge_graph.schema.json")
        path = DATASET / "knowledge_graph.json"
        if not path.is_file():
            pytest.skip("knowledge_graph.json non presente")
        data = json.loads(path.read_text(encoding="utf-8"))
        validate(instance=data, schema=schema)


class TestApiIndexSchema:
    def test_api_index_valid(self):
        schema = _load_schema("api_index.schema.json")
        path = DATASET / "api_index.json"
        if not path.is_file():
            pytest.skip("api_index.json non presente")
        data = json.loads(path.read_text(encoding="utf-8"))
        validate(instance=data, schema=schema)


class TestSchemaVersioning:
    def test_schema_version_absent_means_v1(self):
        """Documenti senza schema_version (storici) restano validi come v1 (B4)."""
        schema = _load_schema("document.schema.json")
        doc = {
            "title": "X", "source_url": "https://example.com/x",
            "category": "reference", "topics": ["assembly"],
            "difficulty": "beginner", "language": "assembly",
            "hardware": ["VIC-II"], "related": [], "scraped_at": "2026-01-01",
        }
        validate(instance=doc, schema=schema)

    def test_unknown_schema_version_rejected(self):
        schema = dict(_load_schema("document.schema.json"))
        schema["properties"]["schema_version"] = {"const": 1}
        doc = {"schema_version": 2, "title": "X"}
        with pytest.raises(jsonschema.ValidationError):
            validate(instance=doc, schema=schema)
