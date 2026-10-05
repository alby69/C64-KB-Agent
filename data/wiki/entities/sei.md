---
id: sei
type: entity
title: SEI — Set Interrupt Disable
aliases:
- SEI — Set Interrupt Disable
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/sei.md
  sha256: 8c226f6172896f3405530079f78ee69535dfa6ef203391bc23ecf0f162ff80f4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-sei
---

# SEI — Set Interrupt Disable



# SEI — SEI — Set Interrupt Disable

## Panoramica
L'istruzione `SEI` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `flags` |
| Formula | `1 → I` |
| Flag alterati | `-----1--` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$78` | 1 | 2 | Standard |

## Descrizione
Set Interrupt Disable
     This instruction initializes the interrupt disable to a 1. It is used to mask interrupt requests during system reset operations and during interrupt commands.
     It affects no registers in the microprocessor and no flags other than the interrupt disable which is set.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-sei]]
