# C64-LLM Downstream Adapter Integration Proposal (Fase 5)

## 1. Overview

This document specifies the integration contract for `alby69/C64-LLM` to consume compiled Layer 2 wiki pages (`data/wiki/`) from `alby69/C64-KB-Agent` as its primary FAISS vector store source, replacing raw document chunks (`data/docs/`).

---

## 2. Why Switch to `data/wiki/`?

1. **Higher Signal-to-Noise Ratio**: Raw OCR text and unprocessed HTML fragments introduce noise, formatting artifacts, and hallucinations. Pages in `data/wiki/` are compiled, deduplicated, and interlinked.
2. **Obsidian Wiki-Links Native Support**: `C64-LLM`'s `ResearcherAgent` already natively supports Obsidian `[[slug]]` wiki-links for graph traversal.
3. **Traceability**: Every page in `data/wiki/` contains explicit source provenance tracking back to Layer 1 files in its frontmatter (`sources` array with `path` and `sha256`).

---

## 3. Data Structure Contract

Each wiki file in `data/wiki/` adheres to `schemas/wiki_page.schema.json`:

```yaml
---
id: "sid-6581"
type: "entity"
title: "SID 6581 — Sound Interface Device"
aliases: ["SID", "6581"]
tags: ["audio", "hardware", "chip"]
sources:
  - path: "data/docs/c64ref/io-map/sid/d400.md"
    sha256: "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
created_at: "2026-08-26"
updated_at: "2026-08-26"
status: "stable"
contradictions: []
links_out: ["vic-ii", "cia-6526"]
---

# SID 6581 — Sound Interface Device

Detailed technical reference...
```

---

## 4. Required Adapter Changes in `C64-LLM`

In `C64-LLM` (`agent/knowledge_base.py` / `ScrapyKBAdapter`):

1. **Directory Source Update**:
   - Update `ScrapyKBAdapter` to read from `data/wiki/` instead of `data/kb/scraped/` or `data/docs/`.
   - Exclude navigation indices `index.md` and `log.md`.

2. **Frontmatter Processing**:
   - Parse YAML frontmatter using standard PyYAML.
   - Extract `id`, `title`, `tags`, `sources`, and `links_out` for vector metadata.

3. **FAISS Indexing & Metadata Enrichment**:
   - Store metadata attributes (`source_paths`, `wiki_links`, `contradictions_flagged`) alongside vector embeddings.
   - When generating RAG citations, reference the `title` and `id` (e.g., `[[sid-6581]]`).

---

## 5. Backward Compatibility & Human-Curated Knowledge Base

- The human-curated directory `knowledge_base/` in `C64-LLM` remains supported for manual editorial overrides or guidelines.
- `WikiKBAdapter` will merge `knowledge_base/` and `data/wiki/` seamlessly during FAISS vector store initialization.
