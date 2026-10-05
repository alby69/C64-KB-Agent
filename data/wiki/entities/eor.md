---
id: eor
type: entity
title: EOR — Exclusive OR
aliases:
- EOR — Exclusive OR
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/eor.md
  sha256: 07554dcd8fd77d2efbcc1c22185fc7fde2f3eca8e6bb6926a632fd78e8abefb8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-eor
---

# EOR — Exclusive OR



# EOR — EOR — Exclusive OR

## Panoramica
L'istruzione `EOR` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `logic` |
| Formula | `A ⊻ M → A` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$41` | 2 | 6 | Standard |
| Zero Page | `$45` | 2 | 3 | Standard |
| Immediate | `$49` | 2 | 2 | Standard |
| Absolute | `$4D` | 3 | 4 | Standard |
| Zero Page Indirect Y-Indexed | `$51` | 2 | 5+p | Standard |
| X-Indexed Zero Page | `$55` | 2 | 4 | Standard |
| Y-Indexed Absolute | `$59` | 3 | 4+p | Standard |
| X-Indexed Absolute | `$5D` | 3 | 4+p | Standard |

## Descrizione
"Exclusive OR" Memory with Accumulator
     The EOR instruction transfers the memory and the accumulator to the adder which performs a binary "EXCLUSIVE OR" on a bit-by-bit basis and stores the result in the accumulator.
     This instruction affects the accumulator; sets the zero flag if the result in the accumulator is 0, otherwise resets the zero flag sets the negative flag if the result in the accumulator has bit 7 on, otherwise resets the negative flag.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-eor]]
