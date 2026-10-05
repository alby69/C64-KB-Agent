---
id: src-0010-subflg
type: source
title: 'Source Summary: Subscript/FNx flag'
aliases:
- Subscript/FNx flag
- 0010-subflg.md
tags:
- memory-map
- zero-page
- rom-layout
- zero-page
sources:
- path: data/docs/c64ref/memory-map/0010-subflg.md
  sha256: 6ebb7a66f8e1ced936ab39f4e4890fff4c4d0b0afc71cef7917f9c917f97389b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Subscript/FNx flag

**Raw Source File**: `data/docs/c64ref/memory-map/0010-subflg.md`
**SHA256**: `6ebb7a66f8e1ced936ab39f4e4890fff4c4d0b0afc71cef7917f9c917f97389b`

## Summary



# SUBFLG — Subscript/FNx flag ($0010)

## Panoramica
Il registro o area di memoria SUBFLG è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0010` (`16` decimale)
- **Range**: `$0010`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
"FOR" and user-defined function
pointer fetching turn
this on before calling "PTRGET"
so arrays won't be detected.
"STKINI" and "PTRGET" clear it.
Also disallows...
