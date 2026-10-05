---
id: lax
type: entity
title: LAX
aliases:
- LAX
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/lax.md
  sha256: 50381cc9ed448f336358317f93d3f03ec7a78e25df2570b084f5b7796c88b423
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-lax
---

# LAX



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

## References
- Source: [[src-lax]]
