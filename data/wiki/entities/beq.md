---
id: beq
type: entity
title: BEQ — Branch if Equal
aliases:
- BEQ — Branch if Equal
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/beq.md
  sha256: 279236ea50b3ee71a17afdffef35ff82ffdf441a53d52d62676ed99bf186b55c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-beq
---

# BEQ — Branch if Equal



# BEQ — BEQ — Branch if Equal

## Panoramica
L'istruzione `BEQ` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `bra` |
| Formula | `Branch on Z = 1` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Relative | `$F0` | 2 | 2+t+p | Standard |

## Descrizione
Branch on Result Zero
     This instruction could also be called "Branch on Equal."
     It takes a conditional branch whenever the Z flag is on or the previous result is equal to 0.
     BEQ does not affect any of the flags or registers other than the program counter and only then when the Z flag is set.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-beq]]
