# Changelog

Tutte le modifiche rilevanti di questo progetto saranno documentate in questo file.
Formato basato su [Keep a Changelog](https://keepachangelog.com/it/1.1.0/) e [Semantic Versioning](https://semver.org/).

## [1.1.0] - 2026-08-26

### Aggiunto
- Configuratore `config.toml` con sezioni `[project]`, `[paths]`, `[i18n]`, `[agent]`, e `[tags]`.
- Contratto operativo multi-agente `AGENT.md` integrato con `JULES.md`.
- Registro delle fonti `SOURCES.md` per tracciare i domini web, i submoduli e i converter di ingestione.
- Report di audit contratti dati `docs/DATA_CONTRACT_AUDIT.md`.
- Script di conversione locale e web clipping `scripts/conv2md.py` e `scripts/clip2md.py` con test in `tests/test_ingest_converters.py`.
- Script di aggregazione metriche `scripts/wiki_stats.py` e dashboard `METRICS.md` con test in `tests/test_wiki_stats.py`.
- Target operativi in `Makefile` (`stats`, `audit`, `reindex`, `test`, `serve`, `validate`, `format`, `lint`).
- Configurazione pre-commit `.pre-commit-config.yaml`.

### Modificato
- Aggiornata la documentazione in `README.md` e `ROADMAP.md` per riflettere l'allineamento con l'architettura `wiki-forge`.

## [1.0.0] - 2026-08-26

### Aggiunto
- Entry point CLI `main.py` con comandi `status`, `validate` e `rebuild-index`.
- Modulo di validazione `kbvalidate.py` per verificate file Markdown e dataset JSONL rispetto agli schemi JSON.
- GitHub Actions CI workflow (`.github/workflows/ci.yml`) con test e gate di validazione contratti.
- Schema v2 dei documenti (`schemas/document.schema.v2.json`) con supporto per l'alias opzionale `tags`.
- Schema manifest (`schemas/manifest.schema.json`) e script di generazione `scripts/generate_manifest.py` (`data/manifest.json`).
- Manifest plugin (`plugin.yaml`) per l'integrazione dichiarativa nell'SDK.

### Modificato
- Rimosso `data/dataset/search_index.db` dal tracciamento Git e aggiunto a `.gitignore`.
- Snellite le dipendenze in `pyproject.toml` e `requirements.txt` rimuovendo pacchetti inutilizzati (`fastapi`, `uvicorn`, `sentence-transformers`, `faiss-cpu`, `pydantic`).
- Configurato submodulo `data/sources/c64ref` in `.gitmodules` con `shallow = true`.
- Aggiornata la documentazione in `README.md`, `CONTRACT.md` e `SECURITY.md`.
