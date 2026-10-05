---
id: src-shy
type: source
title: 'Source Summary: SHY'
aliases:
- SHY
- shy.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/shy.md
  sha256: 26322f0d2b32ec0bb2a1c89304d7bbcdbc10036de63db99d0dd35b4c835100aa
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SHY

**Raw Source File**: `data/docs/c64ref/cpu-instructions/shy.md`
**SHA256**: `26322f0d2b32ec0bb2a1c89304d7bbcdbc10036de63db99d0dd35b4c835100aa`

## Summary



# SHY — SHY

## Panoramica
L'istruzione `SHY` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `Y ∧ (H + 1) → M` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Absolute | `$9C` | 3 | 5 | Non documentata |

## Descrizione
Store Index Register Y "AND" Value
     The u...
