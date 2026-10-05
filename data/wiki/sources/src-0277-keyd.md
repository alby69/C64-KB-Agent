---
id: src-0277-keyd
type: source
title: 'Source Summary: Keybd buffer'
aliases:
- Keybd buffer
- 0277-keyd.md
tags:
- memory-map
- zero-page
- rom-layout
sources:
- path: data/docs/c64ref/memory-map/0277-keyd.md
  sha256: 3168c1416fe7e10df39ebc16ceb339badc15bf620a84fe2717fe2e599f0f7008
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Keybd buffer

**Raw Source File**: `data/docs/c64ref/memory-map/0277-keyd.md`
**SHA256**: `3168c1416fe7e10df39ebc16ceb339badc15bf620a84fe2717fe2e599f0f7008`

## Summary



# KEYD — Keybd buffer ($0277)

## Panoramica
Il registro o area di memoria KEYD è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0277` (`631` decimale)
- **Range**: `$0277`-`$0280`
- **Dimensione**: `10 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
IRQ keyboard buffer

### Commodore-64-intern-Buch (Commodore)
Hier werden die Tastencodes zwischengespeichert,
die nicht sofort vom
Betriebssystem weiterverarbei...
