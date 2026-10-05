---
id: shs
type: entity
title: SHS
aliases:
- SHS
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/shs.md
  sha256: 8e658b28e06984e5b4eb87a00e7d38daf974523a94a78ebc3b58006bd9049c89
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-shs
---

# SHS



# SHS — SHS

## Panoramica
L'istruzione `SHS` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `trans` |
| Formula | `A ∧ X → S, S ∧ (H + 1) → M ## Graham, groepaz: TAS` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Y-Indexed Absolute | `$9B` | 3 | 5 | Non documentata |

## Descrizione
Transfer Accumulator "AND" Index Register X to Stack Pointer then Store Stack Pointer "AND" Hi-Byte In Memory
     The undocumented SHS instruction performs a bit-by-bit AND operation of the value of the accumulator and the value of the index register X and stores the result in the stack pointer. It then performs a bit-by-bit AND operation of the resulting stack pointer and the upper 8 bits of the given address (ignoring the addressing mode's Y offset), plus 1, and transfers the result to the addressed memory location.
     No flags or registers in the microprocessor are affected by the store operation.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-shs]]
