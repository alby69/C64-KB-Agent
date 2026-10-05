---
id: src-dec
type: source
title: 'Source Summary: DEC — Decrement Memory'
aliases:
- DEC — Decrement Memory
- dec.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/dec.md
  sha256: cfec6407523e62d8352d1e8ea6f648f254b11231316b15971013a0a35bf017b3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: DEC — Decrement Memory

**Raw Source File**: `data/docs/c64ref/cpu-instructions/dec.md`
**SHA256**: `cfec6407523e62d8352d1e8ea6f648f254b11231316b15971013a0a35bf017b3`

## Summary



# DEC — DEC — Decrement Memory

## Panoramica
L'istruzione `DEC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `inc` |
| Formula | `M - 1 → M` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$C6` | 2 | 5 | Standard |
| Absolute | `$CE` | 3 | 6 | Standard |
| X-Indexed Zero Page | `...
