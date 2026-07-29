---
title: PLP — Pull Processor Status
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
- plp
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: PLP
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Pull Processor Status From Stack
---

# PLP — PLP — Pull Processor Status

## Panoramica
L'istruzione `PLP` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `stack` |
| Formula | `P↑` |
| Flag alterati | `NV--DIZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$28` | 1 | 4 | Standard |

## Descrizione
Pull Processor Status From Stack
     This instruction transfers the next value on the stack to the Processor Status register, thereby changing all of the flags and setting the mode switches to the values from the stack.
     The PLP instruction affects no registers in the processor other than the status register. This instruction could affect all flags in the status register.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*