---
id: src-inc
type: source
title: 'Source Summary: INC — Increment Memory'
aliases:
- INC — Increment Memory
- inc.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/inc.md
  sha256: d8d47fc8e88ef30c2eb1c60fec37f206059a800eabdbfb514b5516a0df7cc0cb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: INC — Increment Memory

**Raw Source File**: `data/docs/c64ref/cpu-instructions/inc.md`
**SHA256**: `d8d47fc8e88ef30c2eb1c60fec37f206059a800eabdbfb514b5516a0df7cc0cb`

## Summary



# INC — INC — Increment Memory

## Panoramica
L'istruzione `INC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `inc` |
| Formula | `M + 1 → M` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$E6` | 2 | 5 | Standard |
| Absolute | `$EE` | 3 | 6 | Standard |
| X-Indexed Zero Page | `...
