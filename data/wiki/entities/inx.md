---
id: inx
type: entity
title: INX — Increment X Register
aliases:
- INX — Increment X Register
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/inx.md
  sha256: a98c9cf5bd2ccbc6a685060fe6a04cb25d469b0837866b8937bf12731e5c1d8a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-inx
---

# INX — Increment X Register



# INX — INX — Increment X Register

## Panoramica
L'istruzione `INX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `inc` |
| Formula | `X + 1 → X` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$E8` | 1 | 2 | Standard |

## Descrizione
Increment Index Register X By One
     Increment X adds 1 to the current value of the X register. This is an 8-bit increment which does not affect the carry operation, therefore, if the value of X before the increment was FF, the resulting value is 00.
     INX does not affect the carry or overflow flags; it sets the N flag if the result of the increment has a one in bit 7, otherwise resets N; sets the Z flag if the result of the increment is 0, otherwise it resets the Z flag.
     INX does not affect any other register other than the X register.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-inx]]
