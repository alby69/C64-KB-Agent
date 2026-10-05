---
id: pha
type: entity
title: PHA — Push Accumulator
aliases:
- PHA — Push Accumulator
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/pha.md
  sha256: 05b32d61528b729244c5001db85015576d7a034faf938d8570fbf973d23a26a1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-pha
---

# PHA — Push Accumulator



# PHA — PHA — Push Accumulator

## Panoramica
L'istruzione `PHA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `stack` |
| Formula | `A↓` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$48` | 1 | 3 | Standard |

## Descrizione
Push Accumulator On Stack
      This instruction transfers the current value of the accumulator to the next location on the stack, automatically decrementing the stack to point to the next empty location.
      The Push A instruction only affects the stack pointer register which is decremented by 1 as a result of the operation. It affects no flags.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-pha]]
