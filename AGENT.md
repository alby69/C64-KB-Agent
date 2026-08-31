# AGENT.md — Multi-Agent Operational Guidelines & Command Protocol

This document defines the agent-agnostic operational contract for human engineers and automated LLM agents (e.g. Jules, Claude, Codex, Gemini, OpenCode) interacting with `alby69/C64-KB-Agent`.

---

## 1. Operating Principles

1. **Non-Destructive by Default**:
   - `data/docs/` (raw scraped Markdown), `data/dataset/` (JSONL/graph), and `data/sources/` (submodules) are **Layer 1 Raw Truth**.
   - Agents **MUST NEVER** overwrite, modify, or delete files in Layer 1.
   - All maintenance, synthesis, and compilation actions occur strictly within `data/wiki/` (Layer 2).

2. **Configuration-Driven**:
   - All paths, tag taxonomies, and project settings are governed by `config.toml`.

3. **Complete Source Provenance**:
   - Every compiled page in `data/wiki/` must declare its Layer 1 sources in frontmatter (`sources` list with relative path and SHA256 checksum).

4. **Contradiction Flagging**:
   - When conflicting technical facts are encountered (e.g., conflicting clock cycle counts or register behaviors), flag `status: "contradiction_flagged"` and document all claims in the `contradictions` list.

---

## 2. Command Protocol

Agents can execute operational commands via CLI (`c64-kb-agent`) or Python engine (`c64_kb_agent.engine`):

### Core Commands

| Command | Action | Implementation / Target |
|---|---|---|
| `compile` | Process raw Layer 1 docs into compiled Layer 2 wiki pages | `python -m scripts.migrate_wiki` / `WikiIngestor` |
| `ingest` | Ingest new or updated Layer 1 raw Markdown files | `c64-kb-agent engine ingest` |
| `reindex` | Rebuild FTS5 SQLite search index across docs and wiki | `c64-kb-agent rebuild-index` |
| `audit` | Run linter check for broken wikilinks, orphans, and invalid frontmatter | `c64-kb-agent engine lint` |
| `stats` | Calculate and update metrics across raw docs, dataset, and wiki | `python scripts/wiki_stats.py` |
| `validate` | Validate documents against JSON schemas (`v1`, `v2`, `wiki_page`) | `c64-kb-agent validate` |
| `serve` | Start FastAPI REST API server | `c64-kb-agent serve` |

---

## 3. Directory Structure Summary

```
C64-KB-Agent/
├── config.toml           # Single-source project configuration
├── AGENT.md              # Multi-agent operational contract
├── JULES.md              # Jules agent schema layer
├── ROADMAP.md            # LLM-Wiki Engine roadmap
├── SOURCES.md            # Inventory of knowledge sources
├── CONTRACT.md           # Cross-repo data contract
├── data/
│   ├── docs/             # Layer 1 Raw Scraped Markdown (Read-only)
│   ├── dataset/          # Layer 1 JSONL, search index DB, graph (Read-only)
│   ├── sources/          # Layer 1 Submodules (mist64/c64ref) (Read-only)
│   └── wiki/             # Layer 2 Compiled Wiki (LLM Maintained)
```
