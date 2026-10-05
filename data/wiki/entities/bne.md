---
id: bne
type: entity
title: BNE — Branch if Not Equal
aliases:
- BNE — Branch if Not Equal
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/bne.md
  sha256: 981816751a832bb529092035f138f0a4e2f11371912d0b8d164e9575a04862c3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bne
---

# BNE — Branch if Not Equal



# BNE — BNE — Branch if Not Equal

## Panoramica
L'istruzione `BNE` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `bra` |
| Formula | `Branch on Z = 0` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Relative | `$D0` | 2 | 2+t+p | Standard |

## Descrizione
Branch on Result Not Zero
     This instruction could also be called "Branch on Not Equal." It tests the Z flag and takes the conditional branch if the Z flag is not on, indicating that the previous result was not zero.
     BNE does not affect any of the flags or registers other than the program counter and only then if the Z flag is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bne]]
