---
id: src-0013-channl
type: source
title: 'Source Summary: Current I/O prompt flag'
aliases:
- Current I/O prompt flag
- 0013-channl.md
tags:
- memory-map
- zero-page
- rom-layout
- zero-page
sources:
- path: data/docs/c64ref/memory-map/0013-channl.md
  sha256: f3d3de2497bd1e5fbece1d77718fa7a5e91655e0e47ebaeec049d05e36aa26eb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Current I/O prompt flag

**Raw Source File**: `data/docs/c64ref/memory-map/0013-channl.md`
**SHA256**: `f3d3de2497bd1e5fbece1d77718fa7a5e91655e0e47ebaeec049d05e36aa26eb`

## Summary



# CHANNL — Current I/O prompt flag ($0013)

## Panoramica
Il registro o area di memoria CHANNL è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0013` (`19` decimale)
- **Range**: `$0013`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Holds channel number

### Commodore-64-intern-Buch (Commodore)
Die Speicherzelle $0013 wird als Zeiger
für die Peripheriegeräte wie Tastatur,
Datasette, RS2...
