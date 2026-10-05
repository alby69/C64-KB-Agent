---
id: txa
type: entity
title: TXA — Transfer X to Accumulator
aliases:
- TXA — Transfer X to Accumulator
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/txa.md
  sha256: c97d380caa9ea4b4e53a65689890bd167e3ae3bdcde3eb844729ce92027fff24
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-txa
---

# TXA — Transfer X to Accumulator



# TXA — TXA — Transfer X to Accumulator

## Panoramica
L'istruzione `TXA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `trans` |
| Formula | `X → A` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$8A` | 1 | 2 | Standard |

## Descrizione
Transfer Index X To Accumulator
     This instruction moves the value that is in the index register X to the accumulator A without disturbing the content of the index register X.
     TXA does not affect any register other than the accumulator and does not affect the carry or overflow flag. If the result in A has bit 7 on, then the N flag is set, otherwise it is reset. If the resultant value in the accumulator is 0, then the Z flag is set, other­ wise it is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-txa]]
