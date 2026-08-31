# Data Contract Audit & Verification Report (Fase 0)

**Date**: 2026-08-26
**Auditor**: Google Jules
**Repository**: `alby69/C64-KB-Agent` (Submodule `kb-agent/` in `alby69/C64-Intelligence-SDK`)

---

## 1. Executive Summary

This report completes **Fase 0** of the C64-KB-Agent alignment with the `wiki-forge` architecture. It establishes a complete audit of all active data contracts, schema definitions, producer/consumer relationships, and integration points across the C64 ecosystem (`C64-Scrapy`, `C64-KB-Agent`, `C64-LLM`, `C64-Intelligence-SDK`).

### Key Audit Findings:
1. **Producer Contract (`C64-Scrapy` → `C64-KB-Agent`)**: `C64-Scrapy` deposits scraped Commodore 64 documentation into `data/docs/` (Markdown with YAML frontmatter) and `data/dataset/` (`scraped_dataset.jsonl`). Frontmatter adheres to Schema v1 (`schemas/document.schema.json`) and Schema v2 (`schemas/document.schema.v2.json`).
2. **Consumer Contract (`C64-KB-Agent` → `C64-LLM`)**: `C64-LLM` (`agent/knowledge_base.py`) consumes Markdown files directly from `data/docs/` to build its FAISS vector store (`index.faiss` + `docstore.pkl`). In addition, `C64-LLM` supports native Obsidian `[[wikilink]]` graph traversal, enabling seamless transition to Layer 2 `data/wiki/` compiled pages (`docs/C64_LLM_INTEGRATION.md`).
3. **SDK Orchestration Contract (`plugin.yaml` & `plugins/knowledge/plugin.json`)**: `C64-KB-Agent` acts as a self-contained plugin declared via `plugin.yaml` (SDK API v1) and integrated into `C64-Intelligence-SDK`.
4. **Non-Destructive Principle**: Raw scraped inputs in `data/docs/`, legacy dataset artifacts in `data/dataset/`, and Git submodules in `data/sources/` represent **Layer 1 Raw Truth** and remain immutable. The LLM-Wiki Engine maintained layer operates strictly in `data/wiki/` (Layer 2).

---

## 2. Active Schema Contracts & Output Artifacts

| Schema ID / File | Version | Scope / Artifact Path | Producer | Primary Consumers |
|---|---|---|---|---|
| `schemas/document.schema.json` | v1 | `data/docs/**/*.md` | `C64-Scrapy`, `cleaners` | `C64-KB-Agent`, `C64-LLM` |
| `schemas/document.schema.v2.json` | v2 | `data/docs/**/*.md` (with optional `tags`) | `C64-Scrapy` | `C64-KB-Agent`, `C64-LLM` |
| `schemas/dataset.schema.json` | v1 | `data/dataset/scraped_dataset.jsonl` | `C64-Scrapy`, `cleaners` | `C64-KB-Agent` (FTS5 search index) |
| `schemas/knowledge_graph.schema.json` | v1 | `data/dataset/knowledge_graph.json` | `c64_kb_agent` | `C64-KB-Agent` API, `C64-LLM` |
| `schemas/api_index.schema.json` | v1 | `data/dataset/api_index.json` | `c64_kb_agent` | `C64-KB-Agent` API |
| `schemas/manifest.schema.json` | v1 | `data/manifest.json` | `scripts/generate_manifest.py` | CI / Integrity Gate |
| `schemas/wiki_page.schema.json` | Draft 2020-12 | `data/wiki/**/*.md` | `c64_kb_agent.engine` | `C64-KB-Agent` Engine, `C64-LLM` (WikiKBAdapter) |

---

## 3. Producer-Consumer Relationship Matrix

```
  [C64-Scrapy] / [c64ref Submodule]
               │
               ▼ (Layer 1 Raw Data)
     ┌──────────────────┐
     │  data/docs/      │ ──► Consumed by legacy C64-LLM FAISS index builder
     │  data/dataset/   │ ──► SQLite FTS5 index (search_index.db)
     │  data/sources/   │
     └──────────────────┘
               │
               ▼ (Wiki Ingest & Synthesis via c64_kb_agent.engine)
     ┌──────────────────┐
     │  data/wiki/      │ ──► Consumed by C64-LLM WikiKBAdapter (Layer 2 Compiled Wiki)
     │  (entities,      │
     │   concepts, etc) │
     └──────────────────┘
```

---

## 4. Verification & Validation Commands

All data contracts are verified continuously via `c64_kb_agent.validators` and unit tests:

```bash
# Validate Layer 1 docs against Schema v1/v2
c64-kb-agent validate --type docs

# Validate dataset JSONL and graph artifacts
c64-kb-agent validate --type dataset

# Validate Layer 2 wiki frontmatter against schemas/wiki_page.schema.json
c64-kb-agent validate --type wiki
```

---

## 5. Migration Strategy & Compatibility Assurance

To ensure zero downtime or breaking changes across `C64-Intelligence-SDK` and `C64-LLM`:
1. **Layer 1 Immutability**: Existing files in `data/docs/` and `data/dataset/` are never overwritten or removed.
2. **Dual-Adapter Support**: `C64-LLM` supports both `ScrapyKBAdapter` (reading `data/docs/`) and `WikiKBAdapter` (reading compiled `data/wiki/`), allowing gradual transition.
3. **Legacy Bundle Export**: The engine CLI supports generating/updating legacy FTS5 indices and dataset manifests alongside compiling `data/wiki/`.
