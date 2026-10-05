---
id: sre
type: entity
title: SRE
aliases:
- SRE
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/sre.md
  sha256: 856228a4f34c2b12f57ddccb218e205a4bd173e1512505a4222bd60e8e3d3d52
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-sre
---

# SRE



# SRE — SRE

## Panoramica
L'istruzione `SRE` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `M / 2 → M, A ⊻ M → A       ## Ormston: LSE` |
| Flag alterati | `*-----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$43` | 2 | 8 | Non documentata |
| Zero Page | `$47` | 2 | 5 | Non documentata |
| Absolute | `$4F` | 3 | 6 | Non documentata |
| Zero Page Indirect Y-Indexed | `$53` | 2 | 8 | Non documentata |
| X-Indexed Zero Page | `$57` | 2 | 6 | Non documentata |
| Y-Indexed Absolute | `$5B` | 3 | 7 | Non documentata |
| X-Indexed Absolute | `$5F` | 3 | 7 | Non documentata |

## Descrizione
Logical Shift Right then "Exclusive OR" Memory with Accumulator
     The undocumented SRE instruction shifts the specified memory location 1 bit to the right, with the higher bit of the result always being set to 0, and the low bit which is shifted out of the field being stored in the carry flag. It then performs a bit-by-bit "EXCLUSIVE OR" of the result and the value of the accumulator and stores the result in the accumulator.
     This instruction affects the accumulator. It does not affect the overflow flag. The negative flag is set if the accumulator result contains bit 7 on, otherwise the negative flag is reset. The Z flag is set if the result is 0 and reset otherwise. The carry is set equal to input bit 0.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-sre]]
