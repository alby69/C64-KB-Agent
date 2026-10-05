---
id: ldx
type: entity
title: LDX — Load X Register
aliases:
- LDX — Load X Register
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/ldx.md
  sha256: 924c9d9a2ec39ba90390841b387c26f634277b3c92a946415ec5870b2de34d30
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ldx
---

# LDX — Load X Register



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

## References
- Source: [[src-ldx]]
