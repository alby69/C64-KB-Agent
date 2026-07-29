---
title: STA — Store Accumulator
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
related:
- sta
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: STA
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Store Accumulator in Memory
---

# STA — STA — Store Accumulator

## Panoramica
L'istruzione `STA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `A → M` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$81` | 2 | 6 | Standard |
| Zero Page | `$85` | 2 | 3 | Standard |
| Absolute | `$8D` | 3 | 4 | Standard |
| Zero Page Indirect Y-Indexed | `$91` | 2 | 6 | Standard |
| X-Indexed Zero Page | `$95` | 2 | 4 | Standard |
| Y-Indexed Absolute | `$99` | 3 | 5 | Standard |
| X-Indexed Absolute | `$9D` | 3 | 5 | Standard |

## Descrizione
Store Accumulator in Memory
     This instruction transfers the contents of the accumulator to memory.
     This instruction affects none of the flags in the processor status register and does not affect the accumulator.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*