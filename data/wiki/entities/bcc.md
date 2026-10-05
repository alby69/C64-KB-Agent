---
id: bcc
type: entity
title: BCC — Branch if Carry Clear
aliases:
- BCC — Branch if Carry Clear
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/bcc.md
  sha256: 12a22c60df7549870afe5ae5ff2e0ea13821d646545617b21795635ae7c3d9a7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bcc
---

# BCC — Branch if Carry Clear



# BCC — BCC — Branch if Carry Clear

## Panoramica
L'istruzione `BCC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `bra` |
| Formula | `Branch on C = 0` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Relative | `$90` | 2 | 2+t+p | Standard |

## Descrizione
Branch on Carry Clear
     This instruction tests the state of the carry bit and takes a conditional branch if the carry bit is reset.
     It affects no flags or registers other than the program counter and then only if the C flag is not on.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bcc]]
