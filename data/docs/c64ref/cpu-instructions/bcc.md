---
title: BCC — Branch if Carry Clear
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
- bcc
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: BCC
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Branch on Carry Clear
---

# BCC — BCC — Branch if Carry Clear

## Panoramica
L'istruzione `BCC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `bra` |
| Formula | `Branch on C = 0` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Relative | `$90` | 2 | 2+t+p | Standard |

## Descrizione
Branch on Carry Clear
     This instruction tests the state of the carry bit and takes a conditional branch if the carry bit is reset.
     It affects no flags or registers other than the program counter and then only if the C flag is not on.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*