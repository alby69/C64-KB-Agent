---
id: inc
type: entity
title: INC — Increment Memory
aliases:
- INC — Increment Memory
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/inc.md
  sha256: d8d47fc8e88ef30c2eb1c60fec37f206059a800eabdbfb514b5516a0df7cc0cb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-inc
---

# INC — Increment Memory



# INC — INC — Increment Memory

## Panoramica
L'istruzione `INC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `inc` |
| Formula | `M + 1 → M` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$E6` | 2 | 5 | Standard |
| Absolute | `$EE` | 3 | 6 | Standard |
| X-Indexed Zero Page | `$F6` | 2 | 6 | Standard |
| X-Indexed Absolute | `$FE` | 3 | 7 | Standard |

## Descrizione
Increment Memory By One
     This instruction adds 1 to the contents of the addressed memory location.
     The increment memory instruction does not affect any internal registers and does not affect the carry or overflow flags. If bit 7 is on as the result of the increment,N is set, otherwise it is reset; if the increment causes the result to become 0, the Z flag is set on, otherwise it is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-inc]]
