---
id: sty
type: entity
title: STY — Store Y Register
aliases:
- STY — Store Y Register
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/sty.md
  sha256: 27bee50f4dd44d9b63b4e137665e7bf81827155037d20a6354a7fa05713f5ee2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-sty
---

# STY — Store Y Register



# STY — STY — Store Y Register

## Panoramica
L'istruzione `STY` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `Y → M` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$84` | 2 | 3 | Standard |
| Absolute | `$8C` | 3 | 4 | Standard |
| X-Indexed Zero Page | `$94` | 2 | 4 | Standard |

## Descrizione
Store Index Register Y In Memory
     Transfer the value of the Y register to the addressed memory location.
     STY does not affect any flags or registers in the microprocessor.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-sty]]
