---
id: src-028f-keylog
type: source
title: 'Source Summary: Keyboard table setup pointer'
aliases:
- Keyboard table setup pointer
- 028f-keylog.md
tags:
- memory-map
- zero-page
- rom-layout
sources:
- path: data/docs/c64ref/memory-map/028f-keylog.md
  sha256: 3f942c78105c538d6b14b249314873336b14f0c9ab522aef989a0d070e2e026c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Keyboard table setup pointer

**Raw Source File**: `data/docs/c64ref/memory-map/028f-keylog.md`
**SHA256**: `3f942c78105c538d6b14b249314873336b14f0c9ab522aef989a0d070e2e026c`

## Summary



# KEYLOG — Keyboard table setup pointer ($028F)

## Panoramica
Il registro o area di memoria KEYLOG è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$028F` (`655` decimale)
- **Range**: `$028F`-`$0290`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Indirect for keyboard table setup

### Commodore-64-intern-Buch (Commodore)
Hier steht ein Zeiger, der auf die
Betriebssystemroutine für die T...
