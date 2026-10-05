---
id: dey
type: entity
title: DEY — Decrement Y Register
aliases:
- DEY — Decrement Y Register
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/dey.md
  sha256: 2bc337e5f72c533c7c0f5475d1674a8cfab32b5398cc5aea4c83c478c7b85da5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-dey
---

# DEY — Decrement Y Register



# DEY — DEY — Decrement Y Register

## Panoramica
L'istruzione `DEY` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `inc` |
| Formula | `Y - 1 → Y` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$88` | 1 | 2 | Standard |

## Descrizione
Decrement Index Register Y By One
     This instruction subtracts one from the current value in the index register Y and stores the result into the index register Y. The result does not affect or consider carry so that the value in the index register Y is decremented to 0 and then through 0 to FF.
     Decrement Y does not affect the carry or overflow flags; if the Y register contains bit 7 on as a result of the decrement the N flag is set, otherwise the N flag is reset. If the Y register is 0 as a result of the decrement, the Z flag is set otherwise the Z flag is reset. This instruction only affects the index register Y.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-dey]]
