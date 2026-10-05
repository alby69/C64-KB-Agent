---
id: cpy
type: entity
title: CPY — Compare Y Register
aliases:
- CPY — Compare Y Register
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/cpy.md
  sha256: 139ad2cdddee94339e37a057b7890addf87949f927dd253aaca45f6dccbca2ac
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-cpy
---

# CPY — Compare Y Register



# CPY — CPY — Compare Y Register

## Panoramica
L'istruzione `CPY` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `Y - M` |
| Flag alterati | `N-----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$C0` | 2 | 2 | Standard |
| Zero Page | `$C4` | 2 | 3 | Standard |
| Absolute | `$CC` | 3 | 4 | Standard |

## Descrizione
Compare Index Register Y To Memory
     This instruction performs a two's complement subtraction between the index register Y and the specified memory location. The results of the subtraction are not stored anywhere. The instruction is strictly used to set the flags.
     CPY affects no registers in the microprocessor and also does not affect the overflow flag. If the value in the index register Y is equal to or greater than the value in the memory, the carry flag will be set, otherwise it will be cleared. If the results of the subtraction contain bit 7 on the N bit will be set, otherwise it will be cleared. If the value in the index register Y and the value in the memory are equal, the zero flag will be set, otherwise it will be cleared.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-cpy]]
