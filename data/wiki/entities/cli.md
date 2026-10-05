---
id: cli
type: entity
title: CLI — Clear Interrupt Disable
aliases:
- CLI — Clear Interrupt Disable
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/cli.md
  sha256: 1e2dae905c6662c89dfd447f2a20e04528b062778c4b2594aa5823dbecaccaeb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-cli
---

# CLI — Clear Interrupt Disable



# CLI — CLI — Clear Interrupt Disable

## Panoramica
L'istruzione `CLI` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `flags` |
| Formula | `0 → I` |
| Flag alterati | `-----0--` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$58` | 1 | 2 | Standard |

## Descrizione
Clear Interrupt Disable
     This instruction initializes the interrupt disable to a 0. This allows the microprocessor to receive interrupts.
     It affects no registers in the microprocessor and no flags other than the interrupt disable which is cleared.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-cli]]
