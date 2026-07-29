---
title: SAX
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
- sax
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: SAX
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Store Accumulator "AND" Index Register X in Memory
---

# SAX — SAX

## Panoramica
L'istruzione `SAX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `A ∧ X → M` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$83` | 2 | 6 | Non documentata |
| Zero Page | `$87` | 2 | 3 | Non documentata |
| Absolute | `$8F` | 3 | 4 | Non documentata |
| Y-Indexed Zero Page | `$97` | 2 | 4 | Non documentata |

## Descrizione
Store Accumulator "AND" Index Register X in Memory
     The undocumented SAX instruction performs a bit-by-bit AND operation of the value of the accumulator and the value of the index register X and stores the result in memory.
     No flags or registers in the microprocessor are affected by the store operation.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*