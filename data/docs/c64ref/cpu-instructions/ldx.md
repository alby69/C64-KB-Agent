---
title: LDX — Load X Register
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
- ldx
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: LDX
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Load Index Register X From Memory
---

# LDX — LDX — Load X Register

## Panoramica
L'istruzione `LDX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `M → X` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$A2` | 2 | 2 | Standard |
| Zero Page | `$A6` | 2 | 3 | Standard |
| Absolute | `$AE` | 3 | 4 | Standard |
| Y-Indexed Zero Page | `$B6` | 2 | 4 | Standard |
| Y-Indexed Absolute | `$BE` | 3 | 4+p | Standard |

## Descrizione
Load Index Register X From Memory
     Load the index register X from memory.
     LDX does not affect the C or V flags; sets Z if the value loaded was zero, otherwise resets it; sets N if the value loaded in bit 7 is a 1; otherwise N is reset, and affects only the X register.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*