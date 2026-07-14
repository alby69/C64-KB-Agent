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
1. **C64-Scrapy** estrae documentazione da fonti web (codebase64, bbcelite, c64wiki, archive.org, github)
2. **GitHub Actions** esegue lo scraping automaticamente e pusha i dati in questo repo
3. **C64-KB-Agent** consuma i dati per costruire la Knowledge Base

## Struttura

```
data/
├── docs/                          # File Markdown con frontmatter YAML
│   ├── elite_bbcelite_com/        # Documentazione Elite
│   ├── codebase_c64_org/          # Codebase64 wiki
│   ├── www_c64-wiki_com/          # C64 Wiki
│   ├── archive_org/               # Manuali e libri
│   └── github_com/                # Repository GitHub
└── dataset/                       # Dataset processati
    ├── scraped_dataset.jsonl      # Record JSONL con ID SHA256
    ├── knowledge_graph.json       # Grafo di conoscenza
    ├── api_index.json             # Indice API
    └── search_index.db            # Indice di ricerca SQLite FTS5
```

## Aggiornamento Automatico

I dati vengono aggiornati automaticamente tramite GitHub Actions:
- **Trigger manuale**: dalla tab "Actions" → "Scrape and Sync"
- **Cron settimanale**: ogni lunedì alle 06:00 UTC

Per eseguire manualmente:
```bash
# Da C64-Scrapy
python main.py --all --index
# Poi copiare docs_c64/ → data/docs/ e dataset_c64/ → data/dataset/
```

## Integrazione

Questo modulo viene consumato da **C64-LLM** per:
- **RAG (Retrieval-Augmented Generation)**: Query alla Knowledge Base
- **Chunking semantico & Embedding vettoriali**
- **Deduplicazione intelligente** (basata su ID SHA256)
