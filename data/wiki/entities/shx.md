---
id: shx
type: entity
title: SHX
aliases:
- SHX
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/shx.md
  sha256: 7719bae30e15a3e84368f26d37d7515cdccaa0d191227f1b9ff2307b4733cd87
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-shx
---

# SHX



# SHX — SHX

## Panoramica
L'istruzione `SHX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `X ∧ (H + 1) → M` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Y-Indexed Absolute | `$9E` | 3 | 5 | Non documentata |

## Descrizione
Store Index Register X "AND" Value
     The undocumented SHX instruction performs a bit-by-bit AND operation of the index register X and the upper 8 bits of the given address (ignoring the addressing mode's Y offset), plus 1. It then transfers the result to the addressed memory location.
     No flags or registers in the microprocessor are affected by the store operation.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-shx]]
