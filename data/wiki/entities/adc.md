---
id: adc
type: entity
title: ADC — Add with Carry
aliases:
- ADC — Add with Carry
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/adc.md
  sha256: 19f5d2454399b924a6ba593b02ae0bf8ad0d6ca734f9a0e93ad4191e93aa86a2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-adc
---

# ADC — Add with Carry



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

## References
- Source: [[src-adc]]
