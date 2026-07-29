---
title: PHP — Push Processor Status
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
- php
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: PHP
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Push Processor Status On Stack
---

# PHP — PHP — Push Processor Status

## Panoramica
L'istruzione `PHP` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `stack` |
| Formula | `P↓` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$08` | 1 | 3 | Standard |

## Descrizione
Push Processor Status On Stack
     This instruction transfers the contents of the processor status register unchanged to the stack, as governed by the stack pointer.
     The PHP instruction affects no registers or flags in the microprocessor.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*