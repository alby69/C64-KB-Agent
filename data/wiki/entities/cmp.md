---
id: cmp
type: entity
title: CMP — Compare
aliases:
- CMP — Compare
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/cmp.md
  sha256: 4ff12b93a21a2ddc37c927f565ec38fa702a245ac798b36b27f32cee8597d367
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-cmp
---

# CMP — Compare



# CMP — CMP — Compare

## Panoramica
L'istruzione `CMP` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `A - M` |
| Flag alterati | `N-----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$C1` | 2 | 6 | Standard |
| Zero Page | `$C5` | 2 | 3 | Standard |
| Immediate | `$C9` | 2 | 2 | Standard |
| Absolute | `$CD` | 3 | 4 | Standard |
| Zero Page Indirect Y-Indexed | `$D1` | 2 | 5+p | Standard |
| X-Indexed Zero Page | `$D5` | 2 | 4 | Standard |
| Y-Indexed Absolute | `$D9` | 3 | 4+p | Standard |
| X-Indexed Absolute | `$DD` | 3 | 4+p | Standard |

## Descrizione
Compare Memory and Accumulator
     This instruction subtracts the contents of memory from the contents of the accumulator.
     The use of the CMP affects the following flags: Z flag is set on an equal comparison, reset otherwise; the N flag is set or reset by the result bit 7, the carry flag is set when the value in memory is less than or equal to the accumulator, reset when it is greater than the accumulator. The accumulator is not affected.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-cmp]]
