---
id: src-0031-strend
type: source
title: 'Source Summary: Pointer : End-of-Arrays'
aliases:
- 'Pointer : End-of-Arrays'
- 0031-strend.md
tags:
- memory-map
- zero-page
- rom-layout
- zero-page
sources:
- path: data/docs/c64ref/memory-map/0031-strend.md
  sha256: 28451fa0bde57869628a3b0e25c03aea9272c5d777c860f42812f40cfdb8af5e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Pointer : End-of-Arrays

**Raw Source File**: `data/docs/c64ref/memory-map/0031-strend.md`
**SHA256**: `28451fa0bde57869628a3b0e25c03aea9272c5d777c860f42812f40cfdb8af5e`

## Summary



# STREND — Pointer : End-of-Arrays ($0031)

## Panoramica
Il registro o area di memoria STREND è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0031` (`49` decimale)
- **Range**: `$0031`-`$0032`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Increased whenever a new array
or simple variable is encountered.
set to [VARTAB] by "CLEARC".

### Commodore-64-intern-Buch (Commodore)
Diese beide...
