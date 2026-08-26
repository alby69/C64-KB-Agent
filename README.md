# C64-KB-Agent — LLM-Wiki Knowledge Base Engine

[![CI Status](https://github.com/alby69/C64-KB-Agent/workflows/CI/badge.svg)](https://github.com/alby69/C64-KB-Agent/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](pyproject.toml)

`C64-KB-Agent` is the **LLM-Wiki Engine** for the Commodore 64 Intelligence SDK. It transitions the knowledge base from a passive document archive into an active, self-compounding, interlinked technical wiki maintained according to the **LLM-Wiki Pattern**.

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
   - `JULES.md`: Operational guidelines and strict non-destructive constraints for AI agents.
   - `schemas/wiki_page.schema.json`: JSON Schema for wiki page frontmatter validation.

---

## Directory Structure

```
C64-KB-Agent/
├── JULES.md                      # Layer 3 Agent schema & operational directives
├── ROADMAP.md                    # Multi-phase implementation roadmap
├── README.md                     # System architecture overview
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

### CLI Commands
```bash
# Check knowledge base status
c64-kb-agent status

# Validate document and wiki frontmatter schemas
c64-kb-agent validate

# Perform FTS5 search
c64-kb-agent search "SID 6581 filter"

# Start REST API server
c64-kb-agent serve --port 8000
```

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
