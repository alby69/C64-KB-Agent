---
id: asr
type: entity
title: ASR
aliases:
- ASR
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/asr.md
  sha256: f6be1562308cbdb6c7f8e479f7f332c5ca29df7daa1a6d18a3bb9fcd9cb42164
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-asr
---

# ASR



# ASR — ASR

## Panoramica
L'istruzione `ASR` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `(A ∧ M) / 2 → A            ## Ormston, groepaz: ALR` |
| Flag alterati | `0-----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$4B` | 2 | 2 | Non documentata |

## Descrizione
"AND" then Logical Shift Right
     The undocumented ASR instruction performs a bit-by-bit AND operation of the accumulator and memory, then shifts the accumulator 1 bit to the right, with the higher bit of the result always being set to 0, and the low bit which is shifted out of the field being stored in the carry flag.
     This instruction affects the accumulator. It does not affect the overflow flag. The N flag is always reset. The Z flag is set if the result of the shift is 0 and reset otherwise. The carry is set equal to bit 0 of the result of the "AND" operation.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-asr]]
