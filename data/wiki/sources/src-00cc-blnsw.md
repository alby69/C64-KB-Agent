---
id: src-00cc-blnsw
type: source
title: 'Source Summary: 0 = flash cursor'
aliases:
- 0 = flash cursor
- 00cc-blnsw.md
tags:
- memory-map
- zero-page
- rom-layout
- zero-page
sources:
- path: data/docs/c64ref/memory-map/00cc-blnsw.md
  sha256: 164fe6e092dd324172a944d7e08a610f57c59df00eef71adfe985517507d080d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 0 = flash cursor

**Raw Source File**: `data/docs/c64ref/memory-map/00cc-blnsw.md`
**SHA256**: `164fe6e092dd324172a944d7e08a610f57c59df00eef71adfe985517507d080d`

## Summary



# BLNSW — 0 = flash cursor ($00CC)

## Panoramica
Il registro o area di memoria BLNSW è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00CC` (`204` decimale)
- **Range**: `$00CC`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cursor blink enab

### Commodore-64-intern-Buch (Commodore)
Der Cursor wird ausgeschaltet, wenn
in dieser Speicherzelle ein größerer
Wert als Null steht.

### C64 P...
