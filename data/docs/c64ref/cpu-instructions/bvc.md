---
title: BVC — Branch if Overflow Clear
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
- bvc
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: BVC
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Branch on Overflow Clear
---

# BVC — BVC — Branch if Overflow Clear

## Panoramica
L'istruzione `BVC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `bra` |
| Formula | `Branch on V = 0` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Relative | `$50` | 2 | 2+t+p | Standard |

## Descrizione
Branch on Overflow Clear
     This instruction tests the status of the V flag and takes the conditional branch if the flag is not set.
     BVC does not affect any of the flags and registers other than the program counter and only when the overflow flag is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*