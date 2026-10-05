---
id: src-d405
type: source
title: 'Source Summary: Voice 1 Envelope (ADSR) Control'
aliases:
- Voice 1 Envelope (ADSR) Control
- d405.md
tags:
- io-map
- sid-registers
sources:
- path: data/docs/c64ref/io-map/sid/d405.md
  sha256: 929579105ff304b6c8a343c9cc5628bd76c3bf1827a0cdbef42aee850dc94026
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Voice 1 Envelope (ADSR) Control

**Raw Source File**: `data/docs/c64ref/io-map/sid/d405.md`
**SHA256**: `929579105ff304b6c8a343c9cc5628bd76c3bf1827a0cdbef42aee850dc94026`

## Summary



# $D405 — Voice 1 Envelope (ADSR) Control ($D405)

## Panoramica
Il registro o area di memoria $D405 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D405` (`54277` decimale)
- **Range**: `$D405`-`$D406`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7-4  Select Attack Cycle Duration: 0-15
3-0  Select Decay Cycle Duration: 0-15

### Mapping the Commodore 64 (Sheldon Leemon)
When a note is ...
