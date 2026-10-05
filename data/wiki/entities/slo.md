---
id: slo
type: entity
title: SLO
aliases:
- SLO
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/slo.md
  sha256: 32f0f5b77c432f7896278784ad2e514d3cd0d4319502de72b2a59aeb9cfca088
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-slo
---

# SLO



# SLO — SLO

## Panoramica
L'istruzione `SLO` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `M * 2 → M, A ∨ M → A       ## Ormston: ASO` |
| Flag alterati | `*-----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$03` | 2 | 8 | Non documentata |
| Zero Page | `$07` | 2 | 5 | Non documentata |
| Absolute | `$0F` | 3 | 6 | Non documentata |
| Zero Page Indirect Y-Indexed | `$13` | 2 | 8 | Non documentata |
| X-Indexed Zero Page | `$17` | 2 | 6 | Non documentata |
| Y-Indexed Absolute | `$1B` | 3 | 7 | Non documentata |
| X-Indexed Absolute | `$1F` | 3 | 7 | Non documentata |

## Descrizione
Arithmetic Shift Left then "OR" Memory with Accumulator
     The undocumented SLO instruction shifts the address memory location 1 bit to the left, with the bit 0 always being set to 0 and the bit 7 output always being contained in the carry flag. It then performs a bit-by-bit "OR" operation on the result and the accumulator and stores the result in the accumulator.
     The negative flag is set if the accumulator result contains bit 7 on, otherwise the negative flag is reset. It sets Z flag if the result is equal to 0, otherwise resets Z and stores the input bit 7 in the carry flag.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-slo]]
