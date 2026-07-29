---
title: DEC — Decrement Memory
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
- dec
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: DEC
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Decrement Memory By One
---

# DEC — DEC — Decrement Memory

## Panoramica
L'istruzione `DEC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `inc` |
| Formula | `M - 1 → M` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$C6` | 2 | 5 | Standard |
| Absolute | `$CE` | 3 | 6 | Standard |
| X-Indexed Zero Page | `$D6` | 2 | 6 | Standard |
| X-Indexed Absolute | `$DE` | 3 | 7 | Standard |

## Descrizione
Decrement Memory By One
     This instruction subtracts 1, in two's complement, from the contents of the addressed memory location.
     The decrement instruction does not affect any internal register in the microprocessor. It does not affect the carry or overflow flags. If bit 7 is on as a result of the decrement, then the N flag is set, otherwise it is reset. If the result of the decrement is 0, the Z flag is set, other­wise it is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*