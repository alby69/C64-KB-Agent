---
id: sbc
type: entity
title: SBC — Subtract with Carry
aliases:
- SBC — Subtract with Carry
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/sbc.md
  sha256: 56f0491e239adafa981ff5b2a8e052068a6f76f165dc9bdb51090442f83da65f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-sbc
---

# SBC — Subtract with Carry



# SBC — SBC — Subtract with Carry

## Panoramica
L'istruzione `SBC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `A - M - ~C → A` |
| Flag alterati | `NV----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$E1` | 2 | 6 | Standard |
| Zero Page | `$E5` | 2 | 3 | Standard |
| Immediate | `$E9` | 2 | 2 | Standard |
| Immediate | `$EB` | 2 | 2 | Non documentata |
| Absolute | `$ED` | 3 | 4 | Standard |
| Zero Page Indirect Y-Indexed | `$F1` | 2 | 5+p | Standard |
| X-Indexed Zero Page | `$F5` | 2 | 4 | Standard |
| Y-Indexed Absolute | `$F9` | 3 | 4+p | Standard |
| X-Indexed Absolute | `$FD` | 3 | 4+p | Standard |

## Descrizione
Subtract Memory from Accumulator with Borrow
     This instruction subtracts the value of memory and borrow from the value of the accumulator, using two's complement arithmetic, and stores the result in the accumulator. Borrow is defined as the carry flag complemented; therefore, a resultant carry flag indicates that a borrow has not occurred.
     This instruction affects the accumulator. The carry flag is set if the result is greater than or equal to 0. The carry flag is reset when the result is less than 0, indicating a borrow. The over­flow flag is set when the result exceeds +127 or -127, otherwise it is reset. The negative flag is set if the result in the accumulator has bit 7 on, otherwise it is reset. The Z flag is set if the result in the accumulator is 0, otherwise it is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-sbc]]
