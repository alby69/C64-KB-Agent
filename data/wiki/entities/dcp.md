---
id: dcp
type: entity
title: DCP
aliases:
- DCP
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/dcp.md
  sha256: c4a99bb1249a061c6c1db7b66d7ec761e8c7e7d9459c0da904cb9a112616a73a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-dcp
---

# DCP



# DCP — DCP

## Panoramica
L'istruzione `DCP` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `M - 1 → M, A - M           ## Ormston: DCM` |
| Flag alterati | `*-----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$C3` | 2 | 8 | Non documentata |
| Zero Page | `$C7` | 2 | 5 | Non documentata |
| Absolute | `$CF` | 3 | 6 | Non documentata |
| Zero Page Indirect Y-Indexed | `$D3` | 2 | 8 | Non documentata |
| X-Indexed Zero Page | `$D7` | 2 | 6 | Non documentata |
| Y-Indexed Absolute | `$DB` | 3 | 7 | Non documentata |
| X-Indexed Absolute | `$DF` | 3 | 7 | Non documentata |

## Descrizione
Decrement Memory By One then Compare with Accumulator
     This undocumented instruction subtracts 1, in two's complement, from the contents of the addressed memory location. It then subtracts the contents of memory from the contents of the accumulator.
     The DCP instruction does not affect any internal register in the microprocessor. It does not affect the overflow flag. Z flag is set on an equal comparison, reset otherwise; the N flag is set or reset by the result bit 7, the carry flag is set when the result in memory is less than or equal to the accumulator, reset when it is greater than the accumulator.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-dcp]]
