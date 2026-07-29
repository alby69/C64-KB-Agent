---
title: TYA — Transfer Y to Accumulator
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
- tya
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: TYA
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Transfer Index Y To Accumulator
---

# TYA — TYA — Transfer Y to Accumulator

## Panoramica
L'istruzione `TYA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `trans` |
| Formula | `Y → A` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$98` | 1 | 2 | Standard |

## Descrizione
Transfer Index Y To Accumulator
     This instruction moves the value that is in the index register Y to accumulator A without disturbing the content of the register Y.
     TYA does not affect any other register other than the accumulator and does not affect the carry or overflow flag. If the result in the accumulator A has bit 7 on, the N flag is set, otherwise it is reset. If the resultant value in the accumulator A is 0, then the Z flag is set, otherwise it is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*