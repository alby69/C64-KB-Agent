---
id: src-sax
type: source
title: 'Source Summary: SAX'
aliases:
- SAX
- sax.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/sax.md
  sha256: 1ef8330f2748deeda3463438a4033112b68d5699fdea01d9afeb97021c2a1687
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SAX

**Raw Source File**: `data/docs/c64ref/cpu-instructions/sax.md`
**SHA256**: `1ef8330f2748deeda3463438a4033112b68d5699fdea01d9afeb97021c2a1687`

## Summary



# SAX — SAX

## Panoramica
L'istruzione `SAX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `A ∧ X → M` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$83` | 2 | 6 | Non documentata |
| Zero Page | `$87` | 2 | 3 | Non documentata |
| Absolut...
