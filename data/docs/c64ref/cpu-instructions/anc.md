---
title: ANC
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
- anc
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: ANC
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: '"AND" Memory with Accumulator then Move Negative Flag to Carry Flag'
---

# ANC — ANC

## Panoramica
L'istruzione `ANC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `A ∧ M → A, N → C` |
| Flag alterati | `*-----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$0B` | 2 | 2 | Non documentata |
| Immediate | `$2B` | 2 | 2 | Non documentata |

## Descrizione
"AND" Memory with Accumulator then Move Negative Flag to Carry Flag
     The undocumented ANC instruction performs a bit-by-bit AND operation of the accumulator and memory and stores the result back in the accumulator.
     This instruction affects the accumulator; sets the zero flag if the result in the accumulator is 0, otherwise resets the zero flag; sets the negative flag and the carry flag if the result in the accumulator has bit 7 on, otherwise resets the negative flag and the carry flag.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*