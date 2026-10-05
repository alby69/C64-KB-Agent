---
id: tya
type: entity
title: TYA — Transfer Y to Accumulator
aliases:
- TYA — Transfer Y to Accumulator
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/tya.md
  sha256: 4398235704de8b3acb2a181a8cf1e559ad797db2a6299f367db4078e0d987f7d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-tya
---

# TYA — Transfer Y to Accumulator



# TYA — TYA — Transfer Y to Accumulator

## Panoramica
L'istruzione `TYA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `trans` |
| Formula | `Y → A` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$98` | 1 | 2 | Standard |

## Descrizione
Transfer Index Y To Accumulator
     This instruction moves the value that is in the index register Y to accumulator A without disturbing the content of the register Y.
     TYA does not affect any other register other than the accumulator and does not affect the carry or overflow flag. If the result in the accumulator A has bit 7 on, the N flag is set, otherwise it is reset. If the resultant value in the accumulator A is 0, then the Z flag is set, otherwise it is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-tya]]
