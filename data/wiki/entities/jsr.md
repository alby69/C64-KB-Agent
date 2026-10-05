---
id: jsr
type: entity
title: JSR — Jump to Subroutine
aliases:
- JSR — Jump to Subroutine
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/jsr.md
  sha256: 62cbedfc093c055abe2dc7a28025ec73f8d5924c5f76f6c1f3c99ffe9986e9fd
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-jsr
---

# JSR — Jump to Subroutine



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

## References
- Source: [[src-jsr]]
