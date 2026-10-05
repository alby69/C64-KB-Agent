---
id: asl
type: entity
title: ASL — Arithmetic Shift Left
aliases:
- ASL — Arithmetic Shift Left
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/asl.md
  sha256: 9ca2d2dc72914c8dca80ba42b059a4d840ecb21f529e4d3ae8534ff556d381c9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-asl
---

# ASL — Arithmetic Shift Left



# ASL — ASL — Arithmetic Shift Left

## Panoramica
L'istruzione `ASL` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `shift` |
| Formula | `C ← /M7...M0/ ← 0` |
| Flag alterati | `N-----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$06` | 2 | 5 | Standard |
| Accumulator | `$0A` | 1 | 2 | Standard |
| Absolute | `$0E` | 3 | 6 | Standard |
| X-Indexed Zero Page | `$16` | 2 | 6 | Standard |
| X-Indexed Absolute | `$1E` | 3 | 7 | Standard |

## Descrizione
Arithmetic Shift Left
     The shift left instruction shifts either the accumulator or the address memory location 1 bit to the left, with the bit 0 always being set to 0 and the input bit 7 being stored in the carry flag. ASL either shifts the accumulator left 1 bit or is a read/modify/write instruction that affects only memory.
     The instruction does not affect the overflow bit, sets N equal to the result bit 7 (bit 6 in the input), sets Z flag if the result is equal to 0, otherwise resets Z and stores the input bit 7 in the carry flag.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-asl]]
