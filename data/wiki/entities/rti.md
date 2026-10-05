---
id: rti
type: entity
title: RTI — Return from Interrupt
aliases:
- RTI — Return from Interrupt
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/rti.md
  sha256: 333609a19bcb99c6a35bc1e225e365236eaf9f820817aaf9dd82d62997605ca8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-rti
---

# RTI — Return from Interrupt



# RTI — RTI — Return from Interrupt

## Panoramica
L'istruzione `RTI` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `ctrl` |
| Formula | `P↑ PC↑` |
| Flag alterati | `NV--DIZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$40` | 1 | 6 | Standard |

## Descrizione
Return From Interrupt
     This instruction transfers from the stack into the microprocessor the processor status and the program counter location for the instruction which was interrupted. By virtue of the interrupt having stored this data before executing the instruction and the fact that the RTI reinitializes the microprocessor to the same state as when it was interrupted, the combination of interrupt plus RTI allows truly reentrant coding.
     The RTI instruction reinitializes all flags to the position to the point they were at the time the interrupt was taken and sets the program counter back to its pre-interrupt state. It affects no other registers in the microprocessor.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-rti]]
