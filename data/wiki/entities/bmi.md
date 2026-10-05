---
id: bmi
type: entity
title: BMI — Branch if Minus
aliases:
- BMI — Branch if Minus
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/bmi.md
  sha256: 06c8d1cd7aff3c6180fed1266759c7b1bd6dd818a7c14735cf4667cfa1a9a43a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bmi
---

# BMI — Branch if Minus



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
     This instruction takes the conditional branch if the N bit is set.
     BMI does not affect any of the flags or any other part of the machine other than the program counter and then only if the N bit is on.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bmi]]
