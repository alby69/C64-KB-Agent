---
title: LDY — Load Y Register
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
- ldy
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: LDY
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Load Index Register Y From Memory
---

# LDY — LDY — Load Y Register

## Panoramica
L'istruzione `LDY` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `M → Y` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$A0` | 2 | 2 | Standard |
| Zero Page | `$A4` | 2 | 3 | Standard |
| Absolute | `$AC` | 3 | 4 | Standard |
| X-Indexed Zero Page | `$B4` | 2 | 4 | Standard |
| X-Indexed Absolute | `$BC` | 3 | 4+p | Standard |

## Descrizione
Load Index Register Y From Memory
     Load the index register Y from memory.
     LDY does not affect the C or V flags, sets the N flag if the value loaded in bit 7 is a 1, otherwise resets N, sets Z flag if the loaded value is zero otherwise resets Z and only affects the Y register.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*