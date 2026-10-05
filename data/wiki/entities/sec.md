---
id: sec
type: entity
title: SEC — Set Carry Flag
aliases:
- SEC — Set Carry Flag
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/sec.md
  sha256: 7757b8491a94ea35bb902325cceb3af2c05fbe9b50f842f014d6df994cc70fb2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-sec
---

# SEC — Set Carry Flag



# SEC — SEC — Set Carry Flag

## Panoramica
L'istruzione `SEC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `flags` |
| Formula | `1 → C` |
| Flag alterati | `-------1` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$38` | 1 | 2 | Standard |

## Descrizione
Set Carry Flag
     This instruction initializes the carry flag to a 1. This operation should normally precede a SBC loop. It is also useful when used with a ROL instruction to initialize a bit in memory to a 1.
     This instruction affects no registers in the microprocessor and no flags other than the carry flag which is set.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-sec]]
