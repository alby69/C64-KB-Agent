---
id: tsx
type: entity
title: TSX — Transfer Stack Pointer to X
aliases:
- TSX — Transfer Stack Pointer to X
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/tsx.md
  sha256: f2f3df46ff9a82523337505a172054f87f9c8ebe8beb144f0824372eb4768e9c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-tsx
---

# TSX — Transfer Stack Pointer to X



# TSX — TSX — Transfer Stack Pointer to X

## Panoramica
L'istruzione `TSX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `trans` |
| Formula | `S → X` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$BA` | 1 | 2 | Standard |

## Descrizione
Transfer Stack Pointer To Index X
     This instruction transfers the value in the stack pointer to the index register X.
     TSX does not affect the carry or overflow flags. It sets N if bit 7 is on in index X as a result of the instruction, otherwise it is reset. If index X is zero as a result of the TSX, the Z flag is set, other­ wise it is reset. TSX changes the value of index X, making it equal to the content of the stack pointer.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-tsx]]
