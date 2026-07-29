---
title: ISC
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
- isc
- sbc
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: ISC
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Increment Memory By One then SBC then Subtract Memory from Accumulator
      with B...
---

# ISC — ISC

## Panoramica
L'istruzione `ISC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `M + 1 → M, A - M → A       ## Ormston: INS; VICE: ISB` |
| Flag alterati | `**----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$E3` | 2 | 8 | Non documentata |
| Zero Page | `$E7` | 2 | 5 | Non documentata |
| Absolute | `$EF` | 3 | 6 | Non documentata |
| Zero Page Indirect Y-Indexed | `$F3` | 2 | 8 | Non documentata |
| X-Indexed Zero Page | `$F7` | 2 | 6 | Non documentata |
| Y-Indexed Absolute | `$FB` | 3 | 7 | Non documentata |
| X-Indexed Absolute | `$FF` | 3 | 7 | Non documentata |

## Descrizione
Increment Memory By One then SBC then Subtract Memory from Accumulator with Borrow
     This undocumented instruction adds 1 to the contents of the addressed memory location. It then subtracts the value of the result in memory and borrow from the value of the accumulator, using two's complement arithmetic, and stores the result in the accumulator.
     This instruction affects the accumulator. The carry flag is set if the result is greater than or equal to 0. The carry flag is reset when the result is less than 0, indicating a borrow. The over­flow flag is set when the result exceeds +127 or -127, otherwise it is reset. The negative flag is set if the result in the accumulator has bit 7 on, otherwise it is reset. The Z flag is set if the result in the accumulator is 0, otherwise it is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*