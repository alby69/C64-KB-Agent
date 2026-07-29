---
title: BEQ — Branch if Equal
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
- beq
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: BEQ
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Branch on Result Zero
---

# BEQ — BEQ — Branch if Equal

## Panoramica
L'istruzione `BEQ` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `bra` |
| Formula | `Branch on Z = 1` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Relative | `$F0` | 2 | 2+t+p | Standard |

## Descrizione
Branch on Result Zero
     This instruction could also be called "Branch on Equal."
     It takes a conditional branch whenever the Z flag is on or the previous result is equal to 0.
     BEQ does not affect any of the flags or registers other than the program counter and only then when the Z flag is set.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*