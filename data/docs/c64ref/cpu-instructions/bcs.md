---
title: BCS — Branch if Carry Set
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
- bcs
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: BCS
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Branch on Carry Set
---

# BCS — BCS — Branch if Carry Set

## Panoramica
L'istruzione `BCS` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `bra` |
| Formula | `Branch on C = 1` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Relative | `$B0` | 2 | 2+t+p | Standard |

## Descrizione
Branch on Carry Set
     This instruction takes the conditional branch if the carry flag is on.
     BCS does not affect any of the flags or registers except for the program counter and only then if the carry flag is on.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*