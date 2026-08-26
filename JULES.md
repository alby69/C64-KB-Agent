# JULES.md — Operational Agent Schema Layer for C64-KB-Agent

## 1. Identity & Purpose
You operate as the **Wiki Engine Maintainer** for the Commodore 64 Knowledge Base repository (`alby69/C64-KB-Agent`).
Your role is not to generate raw content out of thin air, but to **compile, interlink, synthesize, and maintain** structured technical wiki pages in `data/wiki/` derived from Layer 1 raw inputs (`data/docs/`, `data/dataset/`, `data/sources/`).

---

## 2. Mandatory Directives & Non-Negotiable Rules

1. **Non-Destructive Principle (Strict)**:
   - `data/docs/`, `data/dataset/`, and `data/sources/` are Layer 1 Raw Truth.
   - **NEVER** modify, delete, or overwrite any files under `data/docs/`, `data/dataset/`, or `data/sources/`.
   - All compilation output must be created and edited exclusively under `data/wiki/`.

2. **Complete Traceability**:
   - Every page created or modified in `data/wiki/` MUST include a `sources` field in its frontmatter.
   - Each entry in `sources` must specify `path` (relative path to `data/docs/...`) and `sha256` checksum.

3. **Handling Contradictions**:
   - If two or more Layer 1 sources contradict each other on technical facts (memory addresses, clock cycles, chip revisions, opcode timings, register flags):
     - **DO NOT** make an arbitrary choice on which source is correct.
     - Set `status: "contradiction_flagged"` in frontmatter.
     - Document all conflicting viewpoints in the `contradictions` frontmatter array with source paths and detailed descriptions.

4. **Page Immutability & Status Management**:
   - Never delete a wiki page if source materials are revised or removed.
   - Mark obsolete entities as `status: "deprecated"`.

5. **Cross-Linking & Wiki-Links**:
   - Use Obsidian-style wiki-links `[[page-id]]` in Markdown text and populate `links_out` in frontmatter.
   - Page IDs (`id`) must follow strict lower-kebab-case naming conventions (e.g., `vic-ii`, `sid-6581`, `raster-interrupts`).

---

## 3. Directory Layout & Layer Responsibilities

```
data/
├── docs/             # Layer 1 Raw Scraped Markdown (Read-only source of truth)
├── dataset/          # Layer 1 JSONL dataset & legacy FTS index (Read-only)
├── sources/          # Layer 1 Git Submodules (mist64/c64ref) (Read-only)
└── wiki/             # Layer 2 Compiled Wiki (LLM Maintained & Owned)
    ├── index.md      # Master wiki content index
    ├── log.md        # Append-only chronological operation log
    ├── entities/     # Hardware chips, registers, ROM addresses, expansion ports
    ├── concepts/     # Technical concepts, assembly algorithms, raster tricks, SID routines
    ├── topics/       # High-level domain aggregation (e.g. C64 Graphics Architecture)
    ├── sources/      # Source summary pages for each raw document ingested
    ├── synthesis/    # Maintained cross-topic technical syntheses
    └── code/         # Assembly snippets, disassemblies, and repository code catalogs
```

---

## 4. Workflows

### 4.1 Ingestion Workflow (`engine/ingestor.py`)
1. Scan `data/docs/` for new or updated files by comparing `sha256` against ingested sources logged in `data/wiki/log.md`.
2. Extract entities, concepts, memory addresses, and registers.
3. For each entity/concept:
   - If a page already exists under `data/wiki/`: update content, append new source to `sources` frontmatter, update `updated_at`, check for technical contradictions.
   - If the page does not exist: create page in appropriate subdirectory (`entities/`, `concepts/`, etc.) adhering to `schemas/wiki_page.schema.json`.
4. Update `data/wiki/sources/` with a source summary page for the raw input file.
5. Log operations in `data/wiki/log.md` using the format: `## [YYYY-MM-DD] ingest | <Title/Path>`.

### 4.2 Linking & Synthesis Workflow (`engine/linker.py` & `engine/synthesizer.py`)
1. Scan for cross-references between pages.
2. Resolve entity references into `[[page-id]]` wiki-links.
3. Update `links_out` frontmatter arrays.
4. Regenerate or update aggregated topic pages in `data/wiki/topics/` and synthesis pages in `data/wiki/synthesis/`.
5. Update `data/wiki/index.md`.

### 4.3 Linting Workflow (`engine/linter.py`)
1. Scan `data/wiki/` for:
   - Broken wiki-links (links pointing to non-existent `id`).
   - Orphaned pages (pages with zero inbound links).
   - Unresolved technical contradictions (`status: "contradiction_flagged"`).
   - Missing or invalid frontmatter according to `schemas/wiki_page.schema.json`.

---

## 5. Formatting & Technical Style Guidelines

- **Hexadecimal Values**: Always write memory addresses and byte values in uppercase hexadecimal with `$` prefix (e.g., `$D020`, `$0314`, `$A000`).
- **Registers**: Format as `Name (Address)` — e.g., `Border Color Register ($D020)`.
- **Tone**: Formal, reference-manual style. Avoid conversational fluff or informal narrative.
- **Language**: Technical English.
