---
title: SHY
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
- shy
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: SHY
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Store Index Register Y "AND" Value
---

# SHY — SHY

## Panoramica
L'istruzione `SHY` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `Y ∧ (H + 1) → M` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Absolute | `$9C` | 3 | 5 | Non documentata |

## Descrizione
Store Index Register Y "AND" Value
     The undocumented SHY instruction performs a bit-by-bit AND operation of the index register Y and the upper 8 bits of the given address (ignoring the addressing mode's X offset), plus 1. It then transfers the result to the addressed memory location.
     No flags or registers in the microprocessor are affected by the store operation.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*