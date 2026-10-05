---
id: src-bvc
type: source
title: 'Source Summary: BVC — Branch if Overflow Clear'
aliases:
- BVC — Branch if Overflow Clear
- bvc.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/bvc.md
  sha256: 4925f78354946cdbaf97e47f7f2cc61efcbefeb0fd30b61645e5fb555a846c65
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BVC — Branch if Overflow Clear

**Raw Source File**: `data/docs/c64ref/cpu-instructions/bvc.md`
**SHA256**: `4925f78354946cdbaf97e47f7f2cc61efcbefeb0fd30b61645e5fb555a846c65`

## Summary



# BVC — BVC — Branch if Overflow Clear

## Panoramica
L'istruzione `BVC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `bra` |
| Formula | `Branch on V = 0` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Relative | `$50` | 2 | 2+t+p | Standard |

## Descrizione
Branch on Overflow Clear
     Th...
