# C64 Knowledge Base Agent

Componente centrale dell'ecosistema **[C64-Intelligence-SDK](https://github.com/alby69/C64-Intelligence-SDK)** per la gestione della Knowledge Base dedicata alla programmazione del Commodore 64.

## Architettura

```
[ C64-Scrapy ] ──► GitHub Actions ──► [ C64-KB-Agent ] ──► [ C64-LLM ]
     │                                      │
     │   docs/  (file .md)                  │  RAG & Query
     │   dataset/ (JSONL, indici)           │
     └──────────────────────────────────────┘
```

### Flusso Dati
1. **C64-Scrapy** estrae documentazione da fonti web e pusha i dati in questo repository tramite il workflow `scrape-and-sync.yml` (in C64-Scrapy).
2. **C64-KB-Agent** valida i dati tramite CI e contratti JSON Schema (`schemas/`), indicizza i documenti in SQLite FTS5 e fornisce la CLI di gestione.
3. **C64-LLM** consuma i documenti Markdown da `data/docs/` per la generazione degli indici vettoriali FAISS e RAG.

## Struttura

```
data/
├── docs/                          # File Markdown con frontmatter YAML (v1 / v2)
│   ├── c64ref/                    # Manuali e schede trasformati da mist64/c64ref
│   ├── codebase_c64_org/          # Codebase64 wiki
│   ├── elite_bbcelite_com/        # Documentazione Elite
│   ├── github_com/                # Repository GitHub
│   └── ...
├── dataset/                       # Dataset processati
│   ├── scraped_dataset.jsonl      # Record JSONL con ID SHA256
│   ├── knowledge_graph.json       # Grafo di conoscenza
│   ├── api_index.json             # Indice API
│   └── search_index.db            # Indice FTS5 SQLite (rigenerabile, ignorato da Git)
└── manifest.json                  # Manifest di tracciabilità del dataset
```

## Installazione e Uso CLI

Installare il pacchetto in modalità editable con le dipendenze di test:

```bash
pip install -e ".[test]"
```

Accedere ai comandi CLI tramite `python main.py` oppure con l'eseguibile `c64-kb-agent`:

```bash
# Stato della Knowledge Base
python main.py status

# Validazione contratto dati (schema v1 e v2)
python main.py validate

# Rigenerazione indice SQLite FTS5
python main.py rebuild-index

# Generazione manifest di tracciabilità
python scripts/generate_manifest.py
```

## Sviluppo e Submoduli

Il repository include il submodulo `data/sources/c64ref` (`mist64/c64ref`).

- **Per gli utenti SDK**: non è necessario clonare ricorsivamente il sub-submodulo a meno che non si debbano eseguire i cleaners c64ref (`git submodule update --init kb-agent` dall'SDK).
- **Per gli sviluppatori dei cleaners**: inizializzare il submodulo c64ref:
  ```bash
  git submodule update --init data/sources/c64ref
  ```
  Note: `.gitmodules` è configurato con `shallow = true` per un clone rapido e leggero.

## Aggiornamento Automatico

I dati vengono sincronizzati dal repository **C64-Scrapy** tramite il workflow `scrape-and-sync.yml` su quel repository. In questo repository, la CI (`.github/workflows/ci.yml`) esegue i test e la porta di validazione contratto (`python main.py validate`).
