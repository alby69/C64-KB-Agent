# Contratto dati — C64-KB-Agent

Questo repository è il **titolare del contratto dati** dell'ecosistema C64-Intelligence-SDK. Il contratto vive qui come artefatto condiviso (JSON Schema in `schemas/`) e non prevede **nessun import di codice Python** tra i repository coinvolti: si comunica solo tramite file la cui struttura è versionata e testabile.

## Versione dello schema

Ogni schema in `schemas/` ha campo `$id` e `description` che riportano la versione. I documenti Markdown possono dichiarare `schema_version` nel frontmatter; **se assente si assume `1`** (transizione indolore tra versioni, vedi test `TestSchemaVersioning`).

## Contratto 1 — Scrapy → KB-Agent

**Produttore**: `C64-Scrapy` · **Consumatore**: `C64-KB-Agent` · **Versione schema**: 1 e 2

Artefatti e schema di riferimento:

| Artefatto | Percorso | Schema |
|---|---|---|
| Documenti Markdown v1 (frontmatter YAML) | `data/docs/**/*.md` | `schemas/document.schema.json` |
| Documenti Markdown v2 (frontmatter YAML) | `data/docs/**/*.md` | `schemas/document.schema.v2.json` |
| Dataset JSONL | `data/dataset/scraped_dataset.jsonl` | `schemas/dataset.schema.json` |
| Knowledge graph | `data/dataset/knowledge_graph.json` | `schemas/knowledge_graph.schema.json` |
| API index | `data/dataset/api_index.json` | `schemas/api_index.schema.json` |
| Manifest tracciabilità | `data/manifest.json` | `schemas/manifest.schema.json` |

Campi obbligatori del frontmatter: `title`, `source_url`, `category` (`reference`/`tutorial`/`manual`/`tool`/`source-code`/`deep-dive`), `topics`, `difficulty` (`beginner`/`intermediate`/`advanced`), `language` (`assembly`/`basic`/`mixed`/`none`), `hardware`, `related`, `scraped_at` (ISO date).

Validazione: il produttore valida i documenti generati **prima** del push (`scraper/tests/test_dataset_contract.py`); il consumatore **rifiuta** i documenti non conformi invece di indicizzarli (`kb-agent/tests/test_schemas.py`). Entrambi usano `jsonschema`.

### Versione 2 (Schema v2)

Lo schema v2 (`schemas/document.schema.v2.json`) introduce la compatibilità con i consumatori che leggono il campo `tags`:
- `schema_version: 2` è obbligatorio se si specifica lo schema v2;
- `tags`: campo opzionale (array di stringhe) definito come alias di `topics`;
- I documenti v1 esistenti rimangono validi a tempo indeterminato.

## Contratto 1-bis — Manifest di tracciabilità (`data/manifest.json`)

Generato dallo script `scripts/generate_manifest.py` e validato contro `schemas/manifest.schema.json`.
Contiene:
- `generated_at`: timestamp ISO 8601 UTC di generazione;
- `documents`: conteggio totale e breakdown per directory sorgente;
- `dataset_files`: dimensione in byte e checksum SHA256 di ciascun artefatto dataset;
- `producer` (opzionale): nome del produttore e commit SHA sorgente.

## Contratto 2 — KB-Agent → C64-LLM

**Produttore**: `C64-KB-Agent` · **Consumatore**: `C64-LLM` · **Versione schema**: 1 e 2

`C64-LLM` (`core/agent/knowledge_base.py`) costruisce il proprio indice FAISS leggendo **i documenti Markdown dal filesystem condiviso** (`data/docs/`), tramite `frontmatter.load`. Il contratto è quindi:

- **Percorso atteso**: `data/docs/**/*.md` (frontmatter YAML + body Markdown);
- **Formato**: come da `schemas/document.schema.json` o `schemas/document.schema.v2.json`;
- **Indice**: `C64-LLM` genera localmente `index.faiss` + `docstore.pkl` (`data/vectorstore/`) dal contenuto dei documenti — nessun file FAISS viene scambiato tra i due repository.

## Contratto 3 — submodule → SDK (manifest plugin)

Descritto in `ARCHITECTURE.md` (§ Definizione di plugin) e in `docs/adr/0001-pinning-e-manifest-plugin.md`.

Punti di contatto dichiarativi:
- `plugin.yaml` (in questo repository): manifest **standalone** di auto-descrizione del submodulo (`sdk_api_version: "1"`), che dichiara capabilities, entry point CLI e requisiti Python per l'esecuzione indipendente.
- `plugins/knowledge/plugin.json` (nel repository SDK): manifest consumato dall'SDK per l'integrazione ed esecuzione comandi nell'ecosistema ADR-0001.

I due file non vanno fusi: sono punti di contatto dichiarativi distinti e indipendenti.
