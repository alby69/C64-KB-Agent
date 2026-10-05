---
id: cpx
type: entity
title: CPX — Compare X Register
aliases:
- CPX — Compare X Register
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/cpx.md
  sha256: 1193524ebdfa713acbc38cf4e89ae6fb80a62a9239d3c7d6e23d258f975dfc1c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-cpx
---

# CPX — Compare X Register



# CPX — CPX — Compare X Register

## Panoramica
L'istruzione `CPX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `X - M` |
| Flag alterati | `N-----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$E0` | 2 | 2 | Standard |
| Zero Page | `$E4` | 2 | 3 | Standard |
| Absolute | `$EC` | 3 | 4 | Standard |

## Descrizione
Compare Index Register X To Memory
     This instruction subtracts the value of the addressed memory location from the content of index register X using the adder but does not store the result; therefore, its only use is to set the N, Z and C flags to allow for comparison between the index register X and the value in memory.
     The CPX instruction does not affect any register in the machine; it also does not affect the overflow flag. It causes the carry to be set on if the absolute value of the index register X is equal to or greater than the data from memory. If the value of the memory is greater than the content of the index register X, carry is reset. If the results of the subtraction contain a bit 7, then the N flag is set, if not, it is reset. If the value in memory is equal to the value in index register X, the Z flag is set, otherwise it is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-cpx]]
