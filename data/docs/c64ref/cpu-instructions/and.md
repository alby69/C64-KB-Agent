---
title: AND — Logical AND
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
related: []
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: AND
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: '"AND" Memory with Accumulator'
---

# AND — AND — Logical AND

## Panoramica
L'istruzione `AND` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `logic` |
| Formula | `A ∧ M → A` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$21` | 2 | 6 | Standard |
| Zero Page | `$25` | 2 | 3 | Standard |
| Immediate | `$29` | 2 | 2 | Standard |
| Absolute | `$2D` | 3 | 4 | Standard |
| Zero Page Indirect Y-Indexed | `$31` | 2 | 5+p | Standard |
| X-Indexed Zero Page | `$35` | 2 | 4 | Standard |
| Y-Indexed Absolute | `$39` | 3 | 4+p | Standard |
| X-Indexed Absolute | `$3D` | 3 | 4+p | Standard |

## Descrizione
"AND" Memory with Accumulator
     The AND instruction transfer the accumulator and memory to the adder which performs a bit-by-bit AND operation and stores the result back in the accumulator.
     This instruction affects the accumulator; sets the zero flag if the result in the accumulator is 0, otherwise resets the zero flag; sets the negative flag if the result in the accumulator has bit 7 on, otherwise resets the negative flag.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*