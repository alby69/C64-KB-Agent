---
id: bpl
type: entity
title: BPL — Branch if Plus
aliases:
- BPL — Branch if Plus
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/bpl.md
  sha256: 246dd3bd189c28094640de2ad61d268c7f18f937615ec8cb916afbdbe6a5ce23
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bpl
---

# BPL — Branch if Plus



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

## References
- Source: [[src-bpl]]
