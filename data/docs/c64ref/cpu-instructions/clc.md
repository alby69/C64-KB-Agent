---
title: CLC — Clear Carry Flag
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
- adc
- clc
- rol
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: CLC
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Clear Carry Flag
---

# CLC — CLC — Clear Carry Flag

## Panoramica
L'istruzione `CLC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `flags` |
| Formula | `0 → C` |
| Flag alterati | `-------0` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$18` | 1 | 2 | Standard |

## Descrizione
Clear Carry Flag
     This instruction initializes the carry flag to a 0. This operation should normally precede an ADC loop. It is also useful when used with a ROL instruction to clear a bit in memory.
     This instruction affects no registers in the microprocessor and no flags other than the carry flag which is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*