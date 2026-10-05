---
id: clv
type: entity
title: CLV — Clear Overflow Flag
aliases:
- CLV — Clear Overflow Flag
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/clv.md
  sha256: 868eeb6a4a4d21e23a6bbb7699d8572ee3cd36c88b6df31cf5d63e319681418e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-clv
---

# CLV — Clear Overflow Flag



# CLV — CLV — Clear Overflow Flag

## Panoramica
L'istruzione `CLV` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `flags` |
| Formula | `0 → V` |
| Flag alterati | `-0------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$B8` | 1 | 2 | Standard |

## Descrizione
Clear Overflow Flag
     This instruction clears the overflow flag to a 0. This command is used in conjunction with the set overflow pin which can change the state of the overflow flag with an external signal.
     CLV affects no registers in the microprocessor and no flags other than the overflow flag which is set to a 0.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-clv]]
