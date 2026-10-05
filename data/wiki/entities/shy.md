---
id: shy
type: entity
title: SHY
aliases:
- SHY
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/shy.md
  sha256: 26322f0d2b32ec0bb2a1c89304d7bbcdbc10036de63db99d0dd35b4c835100aa
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-shy
---

# SHY



# SHY — SHY

## Panoramica
L'istruzione `SHY` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `Y ∧ (H + 1) → M` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Absolute | `$9C` | 3 | 5 | Non documentata |

## Descrizione
Store Index Register Y "AND" Value
     The undocumented SHY instruction performs a bit-by-bit AND operation of the index register Y and the upper 8 bits of the given address (ignoring the addressing mode's X offset), plus 1. It then transfers the result to the addressed memory location.
     No flags or registers in the microprocessor are affected by the store operation.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-shy]]
