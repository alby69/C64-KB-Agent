---
title: BMI — Branch if Minus
source_url: https://github.com/mist64/c64ref/blob/main/src/6502/6502_reference.txt
category: reference
topics:
- cpu-instructions
- opcodes
- addressing-modes
difficulty: intermediate
language: assembly
hardware:
- '6502'
related:
- bmi
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: BMI
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Branch on Result Minus
---

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