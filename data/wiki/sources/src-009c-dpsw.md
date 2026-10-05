---
id: src-009c-dpsw
type: source
title: 'Source Summary: Byte-received flag'
aliases:
- Byte-received flag
- 009c-dpsw.md
tags:
- memory-map
- zero-page
- rom-layout
- zero-page
sources:
- path: data/docs/c64ref/memory-map/009c-dpsw.md
  sha256: 4548e9c1100bdb2b37b7a6b82797f92d3efb854f0d26f4849e64f4a4b8cfb94e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Byte-received flag

**Raw Source File**: `data/docs/c64ref/memory-map/009c-dpsw.md`
**SHA256**: `4548e9c1100bdb2b37b7a6b82797f92d3efb854f0d26f4849e64f4a4b8cfb94e`

## Summary



# DPSW — Byte-received flag ($009C)

## Panoramica
Il registro o area di memoria DPSW è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$009C` (`156` decimale)
- **Range**: `$009C`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette: if NZ then expecting LL/L combination that ends a byte

### Commodore-64-intern-Buch (Commodore)
Hier wird festgelegt, ob das gelesene
Byte die Quersumme ...
