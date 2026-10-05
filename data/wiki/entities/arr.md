---
id: arr
type: entity
title: ARR
aliases:
- ARR
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/arr.md
  sha256: cb9f25651d1f922b1b287c03c3b93f8acfa0b8b0293a33f07c08af65f2a1d17f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-arr
---

# ARR



# ARR — ARR

## Panoramica
L'istruzione `ARR` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `(A ∧ M) / 2 → A` |
| Flag alterati | `**----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$6B` | 2 | 2 | Non documentata |

## Descrizione
"AND" Accumulator then Rotate Right
     The undocumented ARR instruction performs a bit-by-bit "AND" operation of the accumulator and memory, then shifts the result right 1 bit with bit 0 shifted into the carry and carry shifted into bit 7. It then stores the result back in the accumulator.
     If bit 7 of the result is on, then the N flag is set, otherwise it is reset. The instruction sets the Z flag if the result is 0; otherwise it resets Z.
     The V and C flags depends on the Decimal Mode Flag:
     In decimal mode, the V flag is set if bit 6 is different than the original data's bit 6, otherwise the V flag is reset. The C flag is set if (operand & 0xF0) + (operand & 0x10) is greater than 0x50, otherwise the C flag is reset.
     In binary mode, the V flag is set if bit 6 of the result is different than bit 5 of the result, otherwise the V flag is reset. The C flag is set if the result in the accumulator has bit 6 on, otherwise it is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-arr]]
