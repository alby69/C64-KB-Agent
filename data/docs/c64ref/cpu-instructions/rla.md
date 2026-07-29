---
title: RLA
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
- rla
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: RLA
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Rotate Left then "AND" with Accumulator
---

# RLA — RLA

## Panoramica
L'istruzione `RLA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `C ← /M7...M0/ ← C, A ∧ M → A` |
| Flag alterati | `*-----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$23` | 2 | 8 | Non documentata |
| Zero Page | `$27` | 2 | 5 | Non documentata |
| Absolute | `$2F` | 3 | 6 | Non documentata |
| Zero Page Indirect Y-Indexed | `$33` | 2 | 8 | Non documentata |
| X-Indexed Zero Page | `$37` | 2 | 6 | Non documentata |
| Y-Indexed Absolute | `$3B` | 3 | 7 | Non documentata |
| X-Indexed Absolute | `$3F` | 3 | 7 | Non documentata |

## Descrizione
Rotate Left then "AND" with Accumulator
     The undocumented RLA instruction shifts the addressed memory left 1 bit, with the input carry being stored in bit 0 and with the input bit 7 being stored in the carry flags. It then performs a bit-by-bit AND operation of the result and the value of the accumulator and stores the result back in the accumulator.
     This instruction affects the accumulator; sets the zero flag if the result in the accumulator is 0, otherwise resets the zero flag; sets the negative flag if the result in the accumulator has bit 7 on, otherwise resets the negative flag.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*