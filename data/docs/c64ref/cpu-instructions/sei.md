---
title: SEI — Set Interrupt Disable
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
- sei
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: SEI
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Set Interrupt Disable
---

# SEI — SEI — Set Interrupt Disable

## Panoramica
L'istruzione `SEI` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `flags` |
| Formula | `1 → I` |
| Flag alterati | `-----1--` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$78` | 1 | 2 | Standard |

## Descrizione
Set Interrupt Disable
     This instruction initializes the interrupt disable to a 1. It is used to mask interrupt requests during system reset operations and during interrupt commands.
     It affects no registers in the microprocessor and no flags other than the interrupt disable which is set.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*