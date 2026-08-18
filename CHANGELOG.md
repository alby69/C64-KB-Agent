# Changelog

Tutte le modifiche rilevanti di questo progetto saranno documentate in questo file.
Formato basato su [Keep a Changelog](https://keepachangelog.com/it/1.1.0/) e [Semantic Versioning](https://semver.org/).

## [Unreleased]

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
