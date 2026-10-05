---
id: src-0200-buf
type: source
title: 'Source Summary: Basic input buffer'
aliases:
- Basic input buffer
- 0200-buf.md
tags:
- memory-map
- zero-page
- rom-layout
sources:
- path: data/docs/c64ref/memory-map/0200-buf.md
  sha256: c1a47a1c38277f9e82f03ce78912ca0f33a3dbc87d562a66e617ba6cd8f1305a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Basic input buffer

**Raw Source File**: `data/docs/c64ref/memory-map/0200-buf.md`
**SHA256**: `c1a47a1c38277f9e82f03ce78912ca0f33a3dbc87d562a66e617ba6cd8f1305a`

## Summary



# BUF — Basic input buffer ($0200)

## Panoramica
Il registro o area di memoria BUF è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0200` (`512` decimale)
- **Range**: `$0200`-`$0258`
- **Dimensione**: `89 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Type-in stored here.
Direct statements execute out of
here. Remember "INPUT" smashes buf.
Must be on page zero
or assignment of string
values in direct state...
