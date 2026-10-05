---
id: plp
type: entity
title: PLP — Pull Processor Status
aliases:
- PLP — Pull Processor Status
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/plp.md
  sha256: ea16dcd1b60d7f1ff9d80a9554899d6e3cd4c3cc284d983f173b5dd57e4c0dc0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-plp
---

# PLP — Pull Processor Status



# PLP — PLP — Pull Processor Status

## Panoramica
L'istruzione `PLP` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `stack` |
| Formula | `P↑` |
| Flag alterati | `NV--DIZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$28` | 1 | 4 | Standard |

## Descrizione
Pull Processor Status From Stack
     This instruction transfers the next value on the stack to the Processor Status register, thereby changing all of the flags and setting the mode switches to the values from the stack.
     The PLP instruction affects no registers in the processor other than the status register. This instruction could affect all flags in the status register.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-plp]]
