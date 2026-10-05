---
id: sta
type: entity
title: STA — Store Accumulator
aliases:
- STA — Store Accumulator
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/sta.md
  sha256: 2647234d68b4a95498da37c60120e2f6ed6ea4d7dc5353c4181592e4b24389a5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-sta
---

# STA — Store Accumulator



# STA — STA — Store Accumulator

## Panoramica
L'istruzione `STA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `A → M` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$81` | 2 | 6 | Standard |
| Zero Page | `$85` | 2 | 3 | Standard |
| Absolute | `$8D` | 3 | 4 | Standard |
| Zero Page Indirect Y-Indexed | `$91` | 2 | 6 | Standard |
| X-Indexed Zero Page | `$95` | 2 | 4 | Standard |
| Y-Indexed Absolute | `$99` | 3 | 5 | Standard |
| X-Indexed Absolute | `$9D` | 3 | 5 | Standard |

## Descrizione
Store Accumulator in Memory
     This instruction transfers the contents of the accumulator to memory.
     This instruction affects none of the flags in the processor status register and does not affect the accumulator.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-sta]]
