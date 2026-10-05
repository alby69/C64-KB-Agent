---
id: rts
type: entity
title: RTS — Return from Subroutine
aliases:
- RTS — Return from Subroutine
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/rts.md
  sha256: ba1435af35a83eaa1c0882c5c84d490854e9678eff4e21ea16224623526e76bc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-rts
---

# RTS — Return from Subroutine



# RTS — RTS — Return from Subroutine

## Panoramica
L'istruzione `RTS` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `ctrl` |
| Formula | `PC↑, PC + 1 → PC` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$60` | 1 | 6 | Standard |

## Descrizione
Return From Subroutine
      This instruction loads the program count low and program count high from the stack into the program counter and increments the program counter so that it points to the instruction following the JSR. The stack pointer is adjusted by incrementing it twice.
      The RTS instruction does not affect any flags and affects only PCL and PCH.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-rts]]
