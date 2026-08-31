# C64-KB-Agent → LLM-Wiki Engine Roadmap

This document defines the multi-phase roadmap to transform `C64-KB-Agent` into an active **LLM-Wiki Engine** following the LLM-Wiki architectural pattern and wiki-forge convergence model.

---

## Phase Summary

| Phase | Description | Status | Target Completion |
|---|---|---|---|
| **Fase 0** | Audit & Verification (`docs/AUDIT.md`, `docs/DATA_CONTRACT_AUDIT.md`) | **Completed** | 2026-08-26 |
| **Fase 1** | Wiki Structure, Governance & Schema Layer (`config.toml`, `AGENT.md`, `JULES.md`, `SOURCES.md`, `schemas/wiki_page.schema.json`) | **Completed** | 2026-08-26 |
| **Fase 2** | Source Ingestion Converters (`scripts/conv2md.py`, `scripts/clip2md.py`) | **Completed** | 2026-08-26 |
| **Fase 3** | Metrics, Audit & Tooling (`wiki_stats.py`, `METRICS.md`, `Makefile`, `.pre-commit-config.yaml`) | **Completed** | 2026-08-26 |
| **Fase 4** | Initial Wiki Migration & Core Engine (`data/wiki/`, `engine/` modules, CLI) | **Completed** | 2026-08-26 |
| **Fase 5** | Post-Scrapy Automated Ingest (`.github/workflows/wiki-ingest.yml` & `wiki-lint.yml`) | **Completed** | 2026-08-26 |
| **Fase 6** | C64-LLM Downstream Adapter Integration (`data/wiki/` FAISS indexing in C64-LLM) | Pending | Week 5-6 |
| **Fase 7** | Semantic Linting & Search Hybridization | Pending | Week 6+ |

---

## Phase Details

### Fase 0 — Audit and Verification (Completed)
- Audit Git submodule setup for `data/sources/c64ref`.
- Document distribution of 1,878 Markdown files across 6 domains in `data/docs/`.
- Validate schema distribution and contract relationships.
- Output: `docs/AUDIT.md`, `docs/DATA_CONTRACT_AUDIT.md`.

### Fase 1 — Governance & Documentation Layer (Completed)
- Create `config.toml` for central project settings.
- Create multi-agent operational contract `AGENT.md` and `JULES.md`.
- Create `SOURCES.md` registering all scraped and manual knowledge sources.
- Create `schemas/wiki_page.schema.json` for frontmatter validation.

### Fase 2 — Ingestion Converters (Completed)
- Add `scripts/conv2md.py` for document conversion (PDF/EPUB/DOCX/MD/TXT) with YAML frontmatter.
- Add `scripts/clip2md.py` for web clipping into structured Markdown.

### Fase 3 — Metrics, Audit & Tooling (Completed)
- Add `scripts/wiki_stats.py` to aggregate stats and update `METRICS.md`.
- Add `Makefile` for developer operations (`stats`, `audit`, `reindex`, `test`, `help`).
- Add `.pre-commit-config.yaml` for automated formatting and lint checks.

### Fase 4 — Core Engine Implementation & Migration (Completed)
- Initial migration script (`scripts/migrate_wiki.py`) processing Layer 1 docs into Layer 2 wiki.
- Python engine modules in `c64_kb_agent/engine/`: `ingestor.py`, `linker.py`, `synthesizer.py`, `linter.py`, `indexer.py`, `cli.py`.

### Fase 5 — Automated Ingest Workflows (Completed)
- GitHub Actions workflows (`.github/workflows/wiki-ingest.yml`, `wiki-lint.yml`).

### Fase 6 — C64-LLM Downstream Adapter Integration
- Adapt `C64-LLM` `KnowledgeBase` reader to consume `data/wiki/` instead of raw fragment chunks (`docs/C64_LLM_INTEGRATION.md`).
