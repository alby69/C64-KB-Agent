---
title: LAX
source_url: https://github.com/mist64/c64ref/blob/main/src/6502/6502_reference.txt
category: reference
topics:
- cpu-instructions
- opcodes
- addressing-modes
difficulty: advanced
language: assembly
hardware:
- '6502'
related:
- lax
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: LAX
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Load Accumulator and Index Register X From Memory
---

# LAX — LAX

## Panoramica
L'istruzione `LAX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `M → A, X` |
| Flag alterati | `*-----*-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$A3` | 2 | 6 | Non documentata |
| Zero Page | `$A7` | 2 | 3 | Non documentata |
| Immediate | `$AB` | 2 | 2 | Non documentata |
| Absolute | `$AF` | 3 | 4 | Non documentata |
| Zero Page Indirect Y-Indexed | `$B3` | 2 | 5+p | Non documentata |
| Y-Indexed Zero Page | `$B7` | 2 | 4 | Non documentata |
| Y-Indexed Absolute | `$BF` | 3 | 4+p | Non documentata |

## Descrizione
Load Accumulator and Index Register X From Memory
     The undocumented LAX instruction loads the accumulator and the index register X from memory.
     LAX does not affect the C or V flags; sets Z if the value loaded was zero, otherwise resets it; sets N if the value loaded in bit 7 is a 1; otherwise N is reset, and affects only the X register.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*