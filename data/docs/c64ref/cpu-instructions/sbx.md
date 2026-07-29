---
title: SBX
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
- sbx
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: SBX
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Subtract Memory from Accumulator "AND" Index Register X
---

# SBX — SBX

## Panoramica
L'istruzione `SBX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `(A ∧ X) - M → X            ## Graham: AXS` |
| Flag alterati | `*-----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$CB` | 2 | 2 | Non documentata |

## Descrizione
Subtract Memory from Accumulator "AND" Index Register X
     This undocumented instruction performs a bit-by-bit "AND" of the value of the accumulator and the index register X and subtracts the value of memory from this result, using two's complement arithmetic, and stores the result in the index register X.
     This instruction affects the index register X. The carry flag is set if the result is greater than or equal to 0. The carry flag is reset when the result is less than 0, indicating a borrow. The negative flag is set if the result in index register X has bit 7 on, otherwise it is reset. The Z flag is set if the result in index register X is 0, otherwise it is reset. The over­flow flag not affected at all.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*