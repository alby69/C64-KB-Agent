---
id: xaa
type: entity
title: XAA
aliases:
- XAA
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/xaa.md
  sha256: 051f8f272448e82225d72ad966c351815a03c197ed7cd0c5b883ad4e15ad9a40
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-xaa
---

# XAA



# XAA — XAA

## Panoramica
L'istruzione `XAA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `(A ∨ V) ∧ X ∧ M → A        ## VICE, groepaz: ANE` |
| Flag alterati | `*-----*-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$8B` | 2 | 2 | Non documentata |

## Descrizione
Non-deterministic Operation of Accumulator, Index Register X, Memory and Bus Contents
     The operation of the undocumented XAA instruction depends on the individual microprocessor. On most machines, it performs a bit-by-bit AND operation of the following three operands: The first two are the index register X and memory.
     The third operand is the result of a bit-by-bit AND operation of the accumulator and a magic component. This magic component depends on the individual microprocessor and is usually one of $00, $EE, $EF, $FE and $FF, and may be influenced by the RDY pin, leftover contents of the data bus, the temperature of the microprocessor, the supplied voltage, and other factors.
     On some machines, additional bits of the result may be set or reset depending on non-deterministic factors.
     It then transfers the result to the accumulator.
     XAA does not affect the C or V flags; sets Z if the value loaded was zero, otherwise resets it; sets N if the result in bit 7 is a 1; otherwise N is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-xaa]]
