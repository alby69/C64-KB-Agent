# Contratto dati — C64-KB-Agent

Questo repository è il **titolare del contratto dati** dell'ecosistema C64-Intelligence-SDK. Il contratto vive qui come artefatto condiviso (JSON Schema in `schemas/`) e non prevede **nessun import di codice Python** tra i repository coinvolti: si comunica solo tramite file la cui struttura è versionata e testabile.

## Versione dello schema

Ogni schema in `schemas/` ha campo `$id` e `description` che riportano la versione. I documenti Markdown possono dichiarare `schema_version` nel frontmatter; **se assente si assume `1`** (transizione indolore tra versioni, vedi test `TestSchemaVersioning`).

## Contratto 1 — Scrapy → KB-Agent

**Produttore**: `C64-Scrapy` · **Consumatore**: `C64-KB-Agent` · **Versione schema**: 1

Artefatti e schema di riferimento:

| Artefatto | Percorso | Schema |
|---|---|---|
| Documenti Markdown (frontmatter YAML) | `data/docs/**/*.md` | `schemas/document.schema.json` |
| Dataset JSONL | `data/dataset/scraped_dataset.jsonl` | `schemas/dataset.schema.json` |
| Knowledge graph | `data/dataset/knowledge_graph.json` | `schemas/knowledge_graph.schema.json` |
| API index | `data/dataset/api_index.json` | `schemas/api_index.schema.json` |

Campi obbligatori del frontmatter: `title`, `source_url`, `category` (`reference`/`tutorial`/`manual`/`tool`/`source-code`/`deep-dive`), `topics`, `difficulty` (`beginner`/`intermediate`/`advanced`), `language` (`assembly`/`basic`/`mixed`/`none`), `hardware`, `related`, `scraped_at` (ISO date).

Validazione: il produttore valida i documenti generati **prima** del push (`scraper/tests/test_dataset_contract.py`); il consumatore **rifiuta** i documenti non conformi invece di indicizzarli (`kb-agent/tests/test_schemas.py`). Entrambi usano `jsonschema`.

## Contratto 2 — KB-Agent → C64-LLM

**Produttore**: `C64-KB-Agent` · **Consumatore**: `C64-LLM` · **Versione schema**: 1

`C64-LLM` (`core/agent/knowledge_base.py`) costruisce il proprio indice FAISS leggendo **i documenti Markdown dal filesystem condiviso** (`data/docs/`), tramite `frontmatter.load`. Il contratto è quindi:

- **Percorso atteso**: `data/docs/**/*.md` (frontmatter YAML + body Markdown);
- **Formato**: come da `schemas/document.schema.json`;
- **Indice**: `C64-LLM` genera localmente `index.faiss` + `docstore.pkl` (`data/vectorstore/`) dal contenuto dei documenti — nessun file FAISS viene scambiato tra i due repository.

### Divergenza nota (da risolvere)

`C64-LLM` legge nel metadata il campo **`tags`** (`post.metadata.get("tags")`), mentre il frontmatter prodotto da `C64-Scrapy` usa **`topics`** (e `hardware`/`related`). Fino a che il consumatore non allinea il campo, i tag dei documenti indicizzati non vengono propagati. Opzione di risoluzione: aggiungere `tags` come alias di `topics` nello schema v2, oppure allineare `knowledge_base.py` a leggere `topics`.

## Contratto 3 — submodule → SDK (manifest plugin)

Descritto in `ARCHITECTURE.md` (§ Definizione di plugin) e in `docs/adr/0001-pinning-e-manifest-plugin.md`. I manifest `plugin.json` sono il solo punto di contatto dichiarativo tra l'SDK e i submodule.