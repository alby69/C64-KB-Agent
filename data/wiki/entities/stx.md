---
id: stx
type: entity
title: STX — Store X Register
aliases:
- STX — Store X Register
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/stx.md
  sha256: 98e43054fcdcaaa6dfe84b2ff6c68d514fd7c1131ba14a4e8422e1d4e8428b16
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-stx
---

# STX — Store X Register



# STX — STX — Store X Register

## Panoramica
L'istruzione `STX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `X → M` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$86` | 2 | 3 | Standard |
| Absolute | `$8E` | 3 | 4 | Standard |
| Y-Indexed Zero Page | `$96` | 2 | 4 | Standard |

## Descrizione
Store Index Register X In Memory
     Transfers value of X register to addressed memory location.
     No flags or registers in the microprocessor are affected by the store operation.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-stx]]
