# SOURCES.md — Knowledge Base Source Registry

This document registers all primary Layer 1 technical knowledge sources ingested and indexed by `C64-KB-Agent`.

---

## 1. Automated Scraped Sources (`data/docs/`)

| Source Key | Domain / Subdirectory | Description | Primary Content Type | File Count |
|---|---|---|---|---|
| `c64ref` | `data/docs/c64ref/` | Hardware IO map, ROM disassembly (BASIC/KERNAL), 6502 Opcodes | Disassembly & Hardware Spec | 1,112 |
| `codebase64` | `data/docs/codebase_c64_org/` | Community routines, algorithms, raster tricks, assembly guides | Tutorials & Code Snippets | 436 |
| `bbcelite` | `data/docs/elite_bbcelite_com/` | Technical breakdown and source commentary for C64 Elite | Game Engine & Assembly | 218 |
| `github` | `data/docs/github_com/` | C64 open-source tool repositories and technical documentation | Code & Reference | 57 |
| `sta` | `data/docs/sta_c64_org/` | Hardware reference, cartridge port diagrams, expansion specs | Hardware Reference | 36 |
| `dustlayer` | `data/docs/dustlayer_com/` | Assembly tutorials and demoscene coding guides | Machine Code Tutorials | 18 |

---

## 2. Git Submodules (`data/sources/`)

| Submodule Path | Repository URL | Target Commit / Branch | Cleaned Output Path |
|---|---|---|---|
| `data/sources/c64ref` | `https://github.com/mist64/c64ref.git` | `7cae8b9` (`master`) | `data/docs/c64ref/` |

---

## 3. Ingest Converters (`scripts/`)

For manual or ad-hoc ingestion outside `C64-Scrapy`:
- `scripts/conv2md.py`: Converts local documents (PDF, EPUB, DOCX, TXT, MD) into structured Markdown with frontmatter.
- `scripts/clip2md.py`: Extracts web pages directly into Markdown with frontmatter.
