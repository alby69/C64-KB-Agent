---
id: pla
type: entity
title: PLA — Pull Accumulator
aliases:
- PLA — Pull Accumulator
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/pla.md
  sha256: 5dc327742f60506bb5eda29da02744223181c9917b1c0976964e91a631282c80
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-pla
---

# PLA — Pull Accumulator



# PLA — PLA — Pull Accumulator

## Panoramica
L'istruzione `PLA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `stack` |
| Formula | `A↑` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$68` | 1 | 4 | Standard |

## Descrizione
Pull Accumulator From Stack
      This instruction adds 1 to the current value of the stack pointer and uses it to address the stack and loads the contents of the stack into the A register.
      The PLA instruction does not affect the carry or overflow flags. It sets N if the bit 7 is on in accumulator A as a result of instructions, otherwise it is reset. If accumulator A is zero as a result of the PLA, then the Z flag is set, otherwise it is reset. The PLA instruction changes content of the accumulator A to the contents of the memory location at stack register plus 1 and also increments the stack register.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-pla]]
