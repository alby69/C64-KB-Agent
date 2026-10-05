---
id: src-arr
type: source
title: 'Source Summary: ARR'
aliases:
- ARR
- arr.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/arr.md
  sha256: cb9f25651d1f922b1b287c03c3b93f8acfa0b8b0293a33f07c08af65f2a1d17f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ARR

**Raw Source File**: `data/docs/c64ref/cpu-instructions/arr.md`
**SHA256**: `cb9f25651d1f922b1b287c03c3b93f8acfa0b8b0293a33f07c08af65f2a1d17f`

## Summary



# ARR — ARR

## Panoramica
L'istruzione `ARR` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `(A ∧ M) / 2 → A` |
| Flag alterati | `**----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$6B` | 2 | 2 | Non documentata |

## Descrizione
"AND" Accumulator then Rotate Right
     The undocume...
