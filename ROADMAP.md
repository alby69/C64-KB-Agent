# C64-KB-Agent → LLM-Wiki Engine Roadmap

This document defines the multi-phase roadmap to transform `C64-KB-Agent` into an active **LLM-Wiki Engine** following the LLM-Wiki architectural pattern.

---

## Phase Summary

| Phase | Description | Status | Target Completion |
|---|---|---|---|
| **Fase 0** | Audit & Verification (Submodule status, inventory, schema baseline, `docs/AUDIT.md`) | **Completed** | 2026-08-26 |
| **Fase 1** | Wiki Structure & Schema Layer (`data/wiki/`, `schemas/wiki_page.schema.json`, `JULES.md`, `ROADMAP.md`) | **Completed** | 2026-08-26 |
| **Fase 2** | Initial Data Migration (Non-destructive wiki compilation from `data/docs/` to `data/wiki/`) | Pending | Week 2-3 |
| **Fase 3** | Core Engine Implementation (`engine/` ingestor, linker, synthesizer, linter, indexer, cli) | Pending | Week 3-4 |
| **Fase 4** | Post-Scrapy Automated Ingest (`.github/workflows/wiki-ingest.yml` & `wiki-lint.yml`) | Pending | Week 4-5 |
| **Fase 5** | C64-LLM Downstream Adapter Integration (`data/wiki/` FAISS indexing in C64-LLM) | Pending | Week 5-6 |
| **Fase 6** | Semantic Linting & Synthesis Refinement | Pending | Week 6-8 |
| **Fase 7** | Vector/BM25 Search Hybridization & Hardening | Pending | Week 8+ |

---

## Phase Details

### Fase 0 — Audit and Verification (Completed)
- Audit Git submodule setup for `data/sources/c64ref`.
- Document distribution of 1,878 Markdown files across 6 domains in `data/docs/`.
- Validate schema distribution (100% v1) and baseline test suite stability (54 passing tests).
- Output: `docs/AUDIT.md`.

### Fase 1 — Wiki Structure & Schema Layer (Completed)
- Create directory tree `data/wiki/{entities,concepts,topics,sources,synthesis,code}/`.
- Create `data/wiki/index.md` and `data/wiki/log.md`.
- Create `schemas/wiki_page.schema.json` for frontmatter validation.
- Create agent operational guidelines in `JULES.md`.
- Update `README.md` and `ROADMAP.md`.

### Fase 2 — Initial Data Migration (Next)
- Write non-destructive migration script processing `data/docs/` into initial `data/wiki/` pages.
- Priority processing order: `c64ref` → `codebase_c64_org` → `www_c64-wiki_com` → `elite_bbcelite_com`.

### Fase 3 — Core Engine Implementation
- Build Python modules in `engine/`:
  - `ingestor.py`: Ingest new Layer 1 raw docs and generate/update wiki pages.
  - `linker.py`: Maintain cross-links (`links_out`, Obsidian `[[slug]]` wiki-links).
  - `synthesizer.py`: Update aggregated topic/synthesis pages.
  - `linter.py`: Detect broken links, orphans, and flagged contradictions.
  - `indexer.py`: Update FTS5 search index to include `data/wiki/`.
  - `cli.py`: Unified engine CLI commands.

### Fase 4 — Automated Ingest Workflows
- Add GitHub Actions workflows (`.github/workflows/wiki-ingest.yml`, `wiki-lint.yml`).

### Fase 5 — C64-LLM Downstream Integration
- Adapt `C64-LLM` `KnowledgeBase` reader to consume `data/wiki/` instead of raw fragment chunks.

### Fase 6 & 7 — Advanced Refinement & Hardening
- Conflict resolution tooling, code snippet indexer, and search optimization.
