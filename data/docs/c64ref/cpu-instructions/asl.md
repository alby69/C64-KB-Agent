---
title: ASL — Arithmetic Shift Left
source_url: https://github.com/mist64/c64ref/blob/main/src/6502/6502_reference.txt
category: reference
topics:
- cpu-instructions
- opcodes
- addressing-modes
difficulty: intermediate
language: assembly
hardware:
- '6502'
related:
- asl
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: ASL
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Arithmetic Shift Left
---

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