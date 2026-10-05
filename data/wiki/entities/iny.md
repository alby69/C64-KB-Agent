---
id: iny
type: entity
title: INY — Increment Y Register
aliases:
- INY — Increment Y Register
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/iny.md
  sha256: aafdb4773966f20571acc9b4b674bc3ca5c6eab6daf1051f3c8d5feaf9369064
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-iny
---

# INY — Increment Y Register



# INY — INY — Increment Y Register

## Panoramica
L'istruzione `INY` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `inc` |
| Formula | `Y + 1 → Y` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$C8` | 1 | 2 | Standard |

## Descrizione
Increment Index Register Y By One
     Increment Y increments or adds one to the current value in the Y register, storing the result in the Y register. As in the case of INX the primary application is to step thru a set of values using the Y register.
     The INY does not affect the carry or overflow flags, sets the N flag if the result of the increment has a one in bit 7, otherwise resets N, sets Z if as a result of the increment the Y register is zero otherwise resets the Z flag.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-iny]]
