---
title: SBC — Subtract with Carry
source_url: https://github.com/mist64/c64ref/blob/main/src/6502/6502_reference.txt
category: reference
topics:
- cpu-instructions
- opcodes
- addressing-modes
difficulty: advanced
language: assembly
hardware:
- '6502'
related:
- sbc
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: SBC
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Subtract Memory from Accumulator with Borrow
---

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