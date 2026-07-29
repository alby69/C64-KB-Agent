---
title: BVS — Branch if Overflow Set
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
- bvs
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: BVS
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Branch on Overflow Set
---

# BVS — BVS — Branch if Overflow Set

## Panoramica
L'istruzione `BVS` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `bra` |
| Formula | `Branch on V = 1` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Relative | `$70` | 2 | 2+t+p | Standard |

## Descrizione
Branch on Overflow Set
     This instruction tests the V flag and takes the conditional branch if V is on.
     BVS does not affect any flags or registers other than the program, counter and only when the overflow flag is set.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*