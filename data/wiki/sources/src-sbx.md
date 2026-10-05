---
id: src-sbx
type: source
title: 'Source Summary: SBX'
aliases:
- SBX
- sbx.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/sbx.md
  sha256: 955badecd4b396104c7209477d9d3ca9931040135f3b9481643f39f5cd789f0c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SBX

**Raw Source File**: `data/docs/c64ref/cpu-instructions/sbx.md`
**SHA256**: `955badecd4b396104c7209477d9d3ca9931040135f3b9481643f39f5cd789f0c`

## Summary



# SBX — SBX

## Panoramica
L'istruzione `SBX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `(A ∧ X) - M → X            ## Graham: AXS` |
| Flag alterati | `*-----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$CB` | 2 | 2 | Non documentata |

## Descrizione
Subtract Memory from Accumu...
