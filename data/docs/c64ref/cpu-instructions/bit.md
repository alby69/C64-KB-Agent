---
title: BIT — Bit Test
source_url: https://github.com/mist64/c64ref/blob/main/src/6502/6502_reference.txt
category: reference
topics:
- cpu-instructions
- opcodes
- addressing-modes
difficulty: intermediate
language: assembly
hardware:
- '6502'
related:
- bit
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: BIT
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Test Bits in Memory with Accumulator
---

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