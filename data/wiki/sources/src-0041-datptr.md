---
id: src-0041-datptr
type: source
title: 'Source Summary: Current DATA address'
aliases:
- Current DATA address
- 0041-datptr.md
tags:
- memory-map
- zero-page
- rom-layout
- zero-page
sources:
- path: data/docs/c64ref/memory-map/0041-datptr.md
  sha256: 22b45939e1f0605b0960b76f542cb836cf2f1b91acd4ad1298d0b7de51545a9a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Current DATA address

**Raw Source File**: `data/docs/c64ref/memory-map/0041-datptr.md`
**SHA256**: `22b45939e1f0605b0960b76f542cb836cf2f1b91acd4ad1298d0b7de51545a9a`

## Summary



# DATPTR — Current DATA address ($0041)

## Panoramica
Il registro o area di memoria DATPTR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0041` (`65` decimale)
- **Range**: `$0041`-`$0042`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Initialized to point
at the zero in front of [TXTTAB]
by "RESTORE" which is called by "CLEARC".
updated by execution of a "READ".

### Commodore-64-int...
