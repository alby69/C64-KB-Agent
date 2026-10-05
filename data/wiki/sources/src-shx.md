---
id: src-shx
type: source
title: 'Source Summary: SHX'
aliases:
- SHX
- shx.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/shx.md
  sha256: 7719bae30e15a3e84368f26d37d7515cdccaa0d191227f1b9ff2307b4733cd87
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SHX

**Raw Source File**: `data/docs/c64ref/cpu-instructions/shx.md`
**SHA256**: `7719bae30e15a3e84368f26d37d7515cdccaa0d191227f1b9ff2307b4733cd87`

## Summary



# SHX — SHX

## Panoramica
L'istruzione `SHX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `X ∧ (H + 1) → M` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Y-Indexed Absolute | `$9E` | 3 | 5 | Non documentata |

## Descrizione
Store Index Register X "AND" Value
     The u...
