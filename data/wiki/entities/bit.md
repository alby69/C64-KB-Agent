---
id: bit
type: entity
title: BIT — Bit Test
aliases:
- BIT — Bit Test
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/bit.md
  sha256: aad96f95dcbd76a453244ad6b8a94b39de677a028ced2a1f7dfaa6b5644429cd
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bit
---

# BIT — Bit Test



# BIT — BIT — Bit Test

## Panoramica
L'istruzione `BIT` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `logic` |
| Formula | `A ∧ M, M7 → N, M6 → V` |
| Flag alterati | `NV----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$24` | 2 | 3 | Standard |
| Absolute | `$2C` | 3 | 4 | Standard |

## Descrizione
Test Bits in Memory with Accumulator
     This instruction performs an AND between a memory location and the accumulator but does not store the result of the AND into the accumulator.
     The bit instruction affects the N flag with N being set to the value of bit 7 of the memory being tested, the V flag with V being set equal to bit 6 of the memory being tested and Z being set by the result of the AND operation between the accumulator and the memory if the result is Zero, Z is reset otherwise. It does not affect the accumulator.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bit]]
