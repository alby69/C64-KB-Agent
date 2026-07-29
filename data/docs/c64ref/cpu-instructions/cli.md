---
title: CLI — Clear Interrupt Disable
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
- cli
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: CLI
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Clear Interrupt Disable
---

# CLI — CLI — Clear Interrupt Disable

## Panoramica
L'istruzione `CLI` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `flags` |
| Formula | `0 → I` |
| Flag alterati | `-----0--` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$58` | 1 | 2 | Standard |

## Descrizione
Clear Interrupt Disable
     This instruction initializes the interrupt disable to a 0. This allows the microprocessor to receive interrupts.
     It affects no registers in the microprocessor and no flags other than the interrupt disable which is cleared.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*