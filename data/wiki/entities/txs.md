---
id: txs
type: entity
title: TXS — Transfer X to Stack Pointer
aliases:
- TXS — Transfer X to Stack Pointer
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/txs.md
  sha256: 77a3f7238eaa0b15bba173ade5423835b342caf52bc3bd6f6fd6ef791ce93759
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-txs
---

# TXS — Transfer X to Stack Pointer



# TXS — TXS — Transfer X to Stack Pointer

## Panoramica
L'istruzione `TXS` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `trans` |
| Formula | `X → S` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$9A` | 1 | 2 | Standard |

## Descrizione
Transfer Index X To Stack Pointer
     This instruction transfers the value in the index register X to the stack pointer.
     TXS changes only the stack pointer, making it equal to the content of the index register X. It does not affect any of the flags.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-txs]]
