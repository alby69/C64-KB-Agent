---
id: src-0292-autodn
type: source
title: 'Source Summary: 0 = scroll enable'
aliases:
- 0 = scroll enable
- 0292-autodn.md
tags:
- memory-map
- zero-page
- rom-layout
sources:
- path: data/docs/c64ref/memory-map/0292-autodn.md
  sha256: 672b8527afa5839c7b64b0f75ac926e63a08bac08d52653f36f603d85ca79bb6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 0 = scroll enable

**Raw Source File**: `data/docs/c64ref/memory-map/0292-autodn.md`
**SHA256**: `672b8527afa5839c7b64b0f75ac926e63a08bac08d52653f36f603d85ca79bb6`

## Summary



# AUTODN — 0 = scroll enable ($0292)

## Panoramica
Il registro o area di memoria AUTODN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0292` (`658` decimale)
- **Range**: `$0292`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Auto scroll down flag(=0 on,<>0 off)

### Commodore-64-intern-Buch (Commodore)
Wenn in dieser Speicherzelle eine 0
steht, setzt der Scroll-Vorgang ein.
Bei einem...
