---
id: sax
type: entity
title: SAX
aliases:
- SAX
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/sax.md
  sha256: 1ef8330f2748deeda3463438a4033112b68d5699fdea01d9afeb97021c2a1687
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-sax
---

# SAX



# SAX — SAX

## Panoramica
L'istruzione `SAX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `A ∧ X → M` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$83` | 2 | 6 | Non documentata |
| Zero Page | `$87` | 2 | 3 | Non documentata |
| Absolute | `$8F` | 3 | 4 | Non documentata |
| Y-Indexed Zero Page | `$97` | 2 | 4 | Non documentata |

## Descrizione
Store Accumulator "AND" Index Register X in Memory
     The undocumented SAX instruction performs a bit-by-bit AND operation of the value of the accumulator and the value of the index register X and stores the result in memory.
     No flags or registers in the microprocessor are affected by the store operation.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-sax]]
