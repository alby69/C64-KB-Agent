---
title: SHS
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
- shs
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: SHS
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Transfer Accumulator "AND" Index Register X to Stack Pointer then
      Store Stack...
---

# SHS — SHS

## Panoramica
L'istruzione `SHS` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `trans` |
| Formula | `A ∧ X → S, S ∧ (H + 1) → M ## Graham, groepaz: TAS` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Y-Indexed Absolute | `$9B` | 3 | 5 | Non documentata |

## Descrizione
Transfer Accumulator "AND" Index Register X to Stack Pointer then Store Stack Pointer "AND" Hi-Byte In Memory
     The undocumented SHS instruction performs a bit-by-bit AND operation of the value of the accumulator and the value of the index register X and stores the result in the stack pointer. It then performs a bit-by-bit AND operation of the resulting stack pointer and the upper 8 bits of the given address (ignoring the addressing mode's Y offset), plus 1, and transfers the result to the addressed memory location.
     No flags or registers in the microprocessor are affected by the store operation.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*