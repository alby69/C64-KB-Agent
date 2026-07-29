---
title: XAA
source_url: https://github.com/mist64/c64ref/blob/main/src/6502/6502_reference.txt
category: reference
topics:
- cpu-instructions
- opcodes
- addressing-modes
difficulty: advanced
language: assembly
hardware:
- '6502'
related:
- xaa
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: XAA
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Non-deterministic Operation of Accumulator, Index Register X, Memory
      and Bus ...
---

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