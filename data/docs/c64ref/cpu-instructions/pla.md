---
title: PLA — Pull Accumulator
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
- pla
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: PLA
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Pull Accumulator From Stack
---

# PLA — PLA — Pull Accumulator

## Panoramica
L'istruzione `PLA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `stack` |
| Formula | `A↑` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$68` | 1 | 4 | Standard |

## Descrizione
Pull Accumulator From Stack
      This instruction adds 1 to the current value of the stack pointer and uses it to address the stack and loads the contents of the stack into the A register.
      The PLA instruction does not affect the carry or overflow flags. It sets N if the bit 7 is on in accumulator A as a result of instructions, otherwise it is reset. If accumulator A is zero as a result of the PLA, then the Z flag is set, otherwise it is reset. The PLA instruction changes content of the accumulator A to the contents of the memory location at stack register plus 1 and also increments the stack register.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*