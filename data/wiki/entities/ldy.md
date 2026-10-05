---
id: ldy
type: entity
title: LDY — Load Y Register
aliases:
- LDY — Load Y Register
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/ldy.md
  sha256: efdb665c068522ddb695370654993a0e16f968e83c71aea9200448e0a8a26a1c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ldy
---

# LDY — Load Y Register



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

## References
- Source: [[src-ldy]]
