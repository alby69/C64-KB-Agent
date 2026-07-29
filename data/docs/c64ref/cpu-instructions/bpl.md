---
title: BPL — Branch if Plus
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
- bpl
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: BPL
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Branch on Result Plus
---

# BPL — BPL — Branch if Plus

## Panoramica
L'istruzione `BPL` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `bra` |
| Formula | `Branch on N = 0` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Relative | `$10` | 2 | 2+t+p | Standard |

## Descrizione
Branch on Result Plus
     This instruction is the complementary branch to branch on result minus. It is a conditional branch which takes the branch when the N bit is reset (0). BPL is used to test if the previous result bit 7 was off (0) and branch on result minus is used to determine if the previous result was minus or bit 7 was on (1).
     The instruction affects no flags or other registers other than the P counter and only affects the P counter when the N bit is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*