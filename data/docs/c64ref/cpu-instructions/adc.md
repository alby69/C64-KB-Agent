---
title: ADC — Add with Carry
source_url: https://github.com/mist64/c64ref/blob/main/src/6502/6502_reference.txt
category: reference
topics:
- cpu-instructions
- opcodes
- addressing-modes
difficulty: intermediate
language: assembly
hardware:
- '6502'
related:
- adc
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: ADC
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Add Memory to Accumulator with Carry
---

# ADC — ADC — Add with Carry

## Panoramica
L'istruzione `ADC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `A + M + C → A, C` |
| Flag alterati | `NV----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$61` | 2 | 6 | Standard |
| Zero Page | `$65` | 2 | 3 | Standard |
| Immediate | `$69` | 2 | 2 | Standard |
| Absolute | `$6D` | 3 | 4 | Standard |
| Zero Page Indirect Y-Indexed | `$71` | 2 | 5+p | Standard |
| X-Indexed Zero Page | `$75` | 2 | 4 | Standard |
| Y-Indexed Absolute | `$79` | 3 | 4+p | Standard |
| X-Indexed Absolute | `$7D` | 3 | 4+p | Standard |

## Descrizione
Add Memory to Accumulator with Carry
     This instruction adds the value of memory and carry from the previous operation to the value of the accumulator and stores the result in the accumulator.
     This instruction affects the accumulator; sets the carry flag when the sum of a binary add exceeds 255 or when the sum of a decimal add exceeds 99, otherwise carry is reset. The overflow flag is set when the sign or bit 7 is changed due to the result exceeding +127 or -128, otherwise overflow is reset. The negative flag is set if the accumulator result contains bit 7 on, otherwise the negative flag is reset. The zero flag is set if the accumulator result is 0, otherwise the zero flag is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*