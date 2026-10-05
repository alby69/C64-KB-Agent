---
id: bvs
type: entity
title: BVS — Branch if Overflow Set
aliases:
- BVS — Branch if Overflow Set
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/bvs.md
  sha256: aa8609634791f8457ea7254e11e01a8c764e670b1e1e80957f65c1658e68679d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bvs
---

# BVS — Branch if Overflow Set



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

## References
- Source: [[src-bvs]]
