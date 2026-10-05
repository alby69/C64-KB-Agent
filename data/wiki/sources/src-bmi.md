---
id: src-bmi
type: source
title: 'Source Summary: BMI — Branch if Minus'
aliases:
- BMI — Branch if Minus
- bmi.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/bmi.md
  sha256: 06c8d1cd7aff3c6180fed1266759c7b1bd6dd818a7c14735cf4667cfa1a9a43a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BMI — Branch if Minus

**Raw Source File**: `data/docs/c64ref/cpu-instructions/bmi.md`
**SHA256**: `06c8d1cd7aff3c6180fed1266759c7b1bd6dd818a7c14735cf4667cfa1a9a43a`

## Summary



# BMI — BMI — Branch if Minus

## Panoramica
L'istruzione `BMI` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `bra` |
| Formula | `Branch on N = 1` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Relative | `$30` | 2 | 2+t+p | Standard |

## Descrizione
Branch on Result Minus
     This instruct...
