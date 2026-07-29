---
title: SHA
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
- sha
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: SHA
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Store Accumulator "AND" Index Register X "AND" Value
---

# SHA — SHA

## Panoramica
L'istruzione `SHA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `A ∧ X ∧ V → M              ## Graham: AHX` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page Indirect Y-Indexed | `$93` | 2 | 6 | Non documentata |
| Y-Indexed Absolute | `$9F` | 3 | 5 | Non documentata |

## Descrizione
Store Accumulator "AND" Index Register X "AND" Value
     The undocumented SHA instruction performs a bit-by-bit AND operation of the following three operands: The first two are the accumulator and the index register X.
     The third operand depends on the addressing mode. In the zero page indirect Y-indexed case, the third operand is the data in memory at the given zero page address (ignoring the addressing mode's Y offset) plus 1. In the Y-indexed absolute case, it is the upper 8 bits of the given address (ignoring the addressing mode's Y offset), plus 1.
     It then transfers the result to the addressed memory location.
     No flags or registers in the microprocessor are affected by the store operation.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*