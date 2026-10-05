---
id: src-0011-inpflg
type: source
title: 'Source Summary: 0 = INPUT; $40 = GET; $98 = READ'
aliases:
- 0 = INPUT; $40 = GET; $98 = READ
- 0011-inpflg.md
tags:
- memory-map
- zero-page
- rom-layout
- zero-page
sources:
- path: data/docs/c64ref/memory-map/0011-inpflg.md
  sha256: e4e7fdbedc0f81488cc41e021d5ade4822a5dec578e686b72536234f9cfe168f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 0 = INPUT; $40 = GET; $98 = READ

**Raw Source File**: `data/docs/c64ref/memory-map/0011-inpflg.md`
**SHA256**: `e4e7fdbedc0f81488cc41e021d5ade4822a5dec578e686b72536234f9cfe168f`

## Summary



# INPFLG — 0 = INPUT; $40 = GET; $98 = READ ($0011)

## Panoramica
Il registro o area di memoria INPFLG è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0011` (`17` decimale)
- **Range**: `$0011`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Flags whether we are doing "INPUT" or "READ"

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle gibt an, in welche
Routine der BASIC-Int...
