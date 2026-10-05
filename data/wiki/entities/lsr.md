---
id: lsr
type: entity
title: LSR — Logical Shift Right
aliases:
- LSR — Logical Shift Right
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/lsr.md
  sha256: 18613753fa666f572a18c413f73861dd8b20cf1689b5944deb488aee5beaf23d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-lsr
---

# LSR — Logical Shift Right



# LSR — LSR — Logical Shift Right

## Panoramica
L'istruzione `LSR` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `shift` |
| Formula | `0 → /M7...M0/ → C` |
| Flag alterati | `0-----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$46` | 2 | 5 | Standard |
| Accumulator | `$4A` | 1 | 2 | Standard |
| Absolute | `$4E` | 3 | 6 | Standard |
| X-Indexed Zero Page | `$56` | 2 | 6 | Standard |
| X-Indexed Absolute | `$5E` | 3 | 7 | Standard |

## Descrizione
Logical Shift Right
     This instruction shifts either the accumulator or a specified memory location 1 bit to the right, with the higher bit of the result always being set to 0, and the low bit which is shifted out of the field being stored in the carry flag.
     The shift right instruction either affects the accumulator by shifting it right 1 or is a read/modify/write instruction which changes a specified memory location but does not affect any internal registers. The shift right does not affect the overflow flag. The N flag is always reset. The Z flag is set if the result of the shift is 0 and reset otherwise. The carry is set equal to bit 0 of the input.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-lsr]]
