---
title: RRA
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
- rra
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: RRA
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Rotate Right and Add Memory to Accumulator
---

# RRA — RRA

## Panoramica
L'istruzione `RRA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `C → /M7...M0/ → C, A + M + C → A` |
| Flag alterati | `**----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$63` | 2 | 8 | Non documentata |
| Zero Page | `$67` | 2 | 5 | Non documentata |
| Absolute | `$6F` | 3 | 6 | Non documentata |
| Zero Page Indirect Y-Indexed | `$73` | 2 | 8 | Non documentata |
| X-Indexed Zero Page | `$77` | 2 | 6 | Non documentata |
| Y-Indexed Absolute | `$7B` | 3 | 7 | Non documentata |
| X-Indexed Absolute | `$7F` | 3 | 7 | Non documentata |

## Descrizione
Rotate Right and Add Memory to Accumulator
     The undocumented RRA instruction shifts the addressed memory right 1 bit with bit 0 shifted into the carry and carry shifted into bit 7. It then adds the result and generated carry to the value of the accumulator and stores the result in the accumulator.
     This instruction affects the accumulator; sets the carry flag when the sum of a binary add exceeds 255 or when the sum of a decimal add exceeds 99, otherwise carry is reset. The overflow flag is set when the sign or bit 7 is changed due to the result exceeding +127 or -128, otherwise overflow is reset. The negative flag is set if the accumulator result contains bit 7 on, otherwise the negative flag is reset. The zero flag is set if the accumulator result is 0, otherwise the zero flag is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*