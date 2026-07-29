---
title: SEC — Set Carry Flag
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
- rol
- sbc
- sec
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: SEC
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Set Carry Flag
---

# SEC — SEC — Set Carry Flag

## Panoramica
L'istruzione `SEC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `flags` |
| Formula | `1 → C` |
| Flag alterati | `-------1` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$38` | 1 | 2 | Standard |

## Descrizione
Set Carry Flag
     This instruction initializes the carry flag to a 1. This operation should normally precede a SBC loop. It is also useful when used with a ROL instruction to initialize a bit in memory to a 1.
     This instruction affects no registers in the microprocessor and no flags other than the carry flag which is set.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*