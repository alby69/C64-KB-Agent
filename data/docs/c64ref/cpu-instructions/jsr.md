---
title: JSR — Jump to Subroutine
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
- jsr
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: JSR
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Jump To Subroutine
---

# JSR — JSR — Jump to Subroutine

## Panoramica
L'istruzione `JSR` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `ctrl` |
| Formula | `PC + 2↓, [PC + 1] → PCL, [PC + 2] → PCH` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Absolute | `$20` | 3 | 6 | Standard |

## Descrizione
Jump To Subroutine
     This instruction transfers control of the program counter to a subroutine location but leaves a return pointer on the stack to allow the user to return to perform the next instruction in the main program after the subroutine is complete. To accomplish this, JSR instruction stores the program counter address which points to the last byte of the jump instruction onto the stack using the stack pointer. The stack byte contains the program count high first, followed by program count low. The JSR then transfers the addresses following the jump instruction to the program counter low and the program counter high, thereby directing the program to begin at that new address.
      The JSR instruction affects no flags, causes the stack pointer to be decremented by 2 and substitutes new values into the program counter low and the program counter high.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*