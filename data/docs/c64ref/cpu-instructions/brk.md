---
title: BRK — Force Interrupt
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
- brk
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: BRK
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Break Command
---

# BRK — BRK — Force Interrupt

## Panoramica
L'istruzione `BRK` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `ctrl` |
| Formula | `PC + 2↓, [FFFE] → PCL, [FFFF] → PCH` |
| Flag alterati | `-----1--` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$00` | 1 | 7 | Standard |

## Descrizione
Break Command
     The break command causes the microprocessor to go through an interrupt sequence under program control. This means that the program counter of the second byte after the BRK. is automatically stored on the stack along with the processor status at the beginning of the break instruction. The microprocessor then transfers control to the interrupt vector.
     Other than changing the program counter, the break instruction changes no values in either the registers or the flags.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*