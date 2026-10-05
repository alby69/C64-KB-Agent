---
id: bvc
type: entity
title: BVC — Branch if Overflow Clear
aliases:
- BVC — Branch if Overflow Clear
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/bvc.md
  sha256: 4925f78354946cdbaf97e47f7f2cc61efcbefeb0fd30b61645e5fb555a846c65
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bvc
---

# BVC — Branch if Overflow Clear



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

## References
- Source: [[src-bvc]]
