---
id: clc
type: entity
title: CLC — Clear Carry Flag
aliases:
- CLC — Clear Carry Flag
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/clc.md
  sha256: cf0bb03ab7fe6a83ed2a33565a2327772c062f43fc8124b3d4375848d4caa24a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-clc
---

# CLC — Clear Carry Flag



# CLC — CLC — Clear Carry Flag

## Panoramica
L'istruzione `CLC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `flags` |
| Formula | `0 → C` |
| Flag alterati | `-------0` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$18` | 1 | 2 | Standard |

## Descrizione
Clear Carry Flag
     This instruction initializes the carry flag to a 0. This operation should normally precede an ADC loop. It is also useful when used with a ROL instruction to clear a bit in memory.
     This instruction affects no registers in the microprocessor and no flags other than the carry flag which is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-clc]]
