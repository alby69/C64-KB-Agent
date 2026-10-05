---
id: las
type: entity
title: LAS
aliases:
- LAS
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/las.md
  sha256: d86005d52f3eca913c093a81000de501831449a9158355d4b9f3c9443fdde32b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-las
---

# LAS



# LAS — LAS

## Panoramica
L'istruzione `LAS` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `M ∧ S → A, X, S` |
| Flag alterati | `*-----*-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Y-Indexed Absolute | `$BB` | 3 | 4+p | Non documentata |

## Descrizione
"AND" Memory with Stack Pointer
     This undocumented instruction performs a bit-by-bit "AND" operation of the stack pointer and memory and stores the result back in the accumulator, the index register X and the stack pointer.
      The LAS instruction does not affect the carry or overflow flags. It sets N if the bit 7 of the result is on, otherwise it is reset. If the result is zero, then the Z flag is set, otherwise it is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-las]]
