# C64-KB-Agent — LLM-Wiki Knowledge Base Engine

[![CI Status](https://github.com/alby69/C64-KB-Agent/workflows/CI/badge.svg)](https://github.com/alby69/C64-KB-Agent/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](pyproject.toml)

`C64-KB-Agent` is the **LLM-Wiki Engine** for the Commodore 64 Intelligence SDK. It transitions the knowledge base from a passive document archive into an active, self-compounding, interlinked technical wiki maintained according to the **LLM-Wiki Pattern** and harmonized with the **wiki-forge** architecture.

---

## Governance & Documentation

- **[config.toml](config.toml)**: Central configuration file for paths, i18n, agent guidelines, and tag taxonomy.
- **[AGENT.md](AGENT.md)**: Agent-agnostic multi-agent operational contract and command protocol.
- **[JULES.md](JULES.md)**: Operational agent schema layer for Google Jules and automated maintainers.
- **[ROADMAP.md](ROADMAP.md)**: Multi-phase implementation roadmap and progress dashboard.
- **[SOURCES.md](SOURCES.md)**: Knowledge base source registry for automated scrapers and manual converters.
- **[CONTRACT.md](CONTRACT.md)**: Cross-repository data contract specification for the SDK.
- **[METRICS.md](METRICS.md)**: Knowledge base statistics and index metrics dashboard.
- **[docs/DATA_CONTRACT_AUDIT.md](docs/DATA_CONTRACT_AUDIT.md)**: Audit of active data contracts and downstream integration adapters.

---

## Ecosystem Architecture

```
[ C64-Scrapy ] ──────► [ C64-KB-Agent ] ──────► [ C64-LLM ]
 (Raw Extraction)     (LLM-Wiki Engine)       (RAG / Coding Assistant)
       │                      │
       │ raw .md / jsonl      │ data/wiki/ (compiled, interlinked)
       └──────────────────────┘ index.md + log.md
```

---

## 3-Layer Knowledge Architecture

1. **Layer 1 — Raw Sources (Immutable Truth)**:
   - `data/docs/`: Processed Markdown with YAML frontmatter from `C64-Scrapy`.
   - `data/dataset/`: SQLite FTS5 `search_index.db`, `scraped_dataset.jsonl`, `knowledge_graph.json`.
   - `data/sources/c64ref`: Git submodule pointing to raw upstream reference files (`mist64/c64ref`).

2. **Layer 2 — The Wiki (Compiled Knowledge)**:
   - `data/wiki/`: Maintained by the LLM Engine with full back-traceability to Layer 1.
   - Subdirectories: `entities/`, `concepts/`, `topics/`, `sources/`, `synthesis/`, `code/`.
   - Indexing & Audit: `data/wiki/index.md` (content-oriented catalog) and `data/wiki/log.md` (append-only operation log).

3. **Layer 3 — The Schema (Agent Guidelines)**:
   - `config.toml` & `AGENT.md`: Operational configuration and guidelines for AI agents.
   - `JULES.md`: Directives and strict non-destructive constraints for Google Jules.
   - `schemas/wiki_page.schema.json`: JSON Schema for wiki page frontmatter validation.

---

## Directory Structure

```
C64-KB-Agent/
├── config.toml                   # Central project configuration
├── AGENT.md                      # Multi-agent operational contract
├── JULES.md                      # Layer 3 Agent schema & operational directives
├── ROADMAP.md                    # Multi-phase implementation roadmap
├── SOURCES.md                    # Registry of primary knowledge sources
├── CONTRACT.md                   # Ecosystem data contract specification
├── METRICS.md                    # Automated metrics dashboard
├── Makefile                      # Developer operational targets
├── cleaners/                     # Raw c64ref transformation cleaners
├── data/
│   ├── docs/                     # Layer 1 raw Markdown files (Read-only)
│   ├── dataset/                  # Layer 1 JSONL & FTS search index (Read-only)
│   ├── sources/c64ref/           # Layer 1 Git submodule (mist64/c64ref)
│   └── wiki/                     # Layer 2 Compiled Wiki (Engine-managed)
│       ├── index.md
│       ├── log.md
│       ├── entities/
│       ├── concepts/
│       ├── topics/
│       ├── sources/
│       ├── synthesis/
│       └── code/
├── schemas/                      # JSON Schemas (document v1/v2, wiki_page, dataset, manifest)
├── c64_kb_agent/                 # Python package (CLI, Search Engine, Server, Validators)
└── tests/                        # Pytest suite
```

---

## Quick Start

### Installation
```bash
git clone --recursive https://github.com/alby69/C64-KB-Agent.git
cd C64-KB-Agent
pip install -e ".[serve,test,dev]"
```

### Development Commands
```bash
# Calculate metrics and update METRICS.md
make stats

# Run linter and wiki link audit
make audit

# Rebuild search index
make reindex

# Check knowledge base status via CLI
c64-kb-agent status

# Validate document and wiki frontmatter schemas
c64-kb-agent validate

# Start REST API server
c64-kb-agent serve --port 8000
```

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
