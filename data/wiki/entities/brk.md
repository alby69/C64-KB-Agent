---
id: brk
type: entity
title: BRK — Force Interrupt
aliases:
- BRK — Force Interrupt
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/brk.md
  sha256: 8745337f390fce2d845060ebb072d618679a6ddd00f0eca9bf63d95b6bf84168
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-brk
---

# BRK — Force Interrupt



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

## References
- Source: [[src-brk]]
