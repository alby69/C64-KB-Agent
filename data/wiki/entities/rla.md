---
id: rla
type: entity
title: RLA
aliases:
- RLA
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/rla.md
  sha256: 33eeb1780e9c152ab820fdad312d209323acef51db4b84c3a54cf8f7d774c3c1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-rla
---

# RLA



# RLA — RLA

## Panoramica
L'istruzione `RLA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `C ← /M7...M0/ ← C, A ∧ M → A` |
| Flag alterati | `*-----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$23` | 2 | 8 | Non documentata |
| Zero Page | `$27` | 2 | 5 | Non documentata |
| Absolute | `$2F` | 3 | 6 | Non documentata |
| Zero Page Indirect Y-Indexed | `$33` | 2 | 8 | Non documentata |
| X-Indexed Zero Page | `$37` | 2 | 6 | Non documentata |
| Y-Indexed Absolute | `$3B` | 3 | 7 | Non documentata |
| X-Indexed Absolute | `$3F` | 3 | 7 | Non documentata |

## Descrizione
Rotate Left then "AND" with Accumulator
     The undocumented RLA instruction shifts the addressed memory left 1 bit, with the input carry being stored in bit 0 and with the input bit 7 being stored in the carry flags. It then performs a bit-by-bit AND operation of the result and the value of the accumulator and stores the result back in the accumulator.
     This instruction affects the accumulator; sets the zero flag if the result in the accumulator is 0, otherwise resets the zero flag; sets the negative flag if the result in the accumulator has bit 7 on, otherwise resets the negative flag.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-rla]]
