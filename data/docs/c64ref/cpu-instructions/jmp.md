---
title: JMP — Jump
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
- jmp
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: JMP
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: JMP Indirect
---

# JMP — JMP — Jump

## Panoramica
L'istruzione `JMP` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `ctrl` |
| Formula | `[PC + 1] → PCL, [PC + 2] → PCH` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Absolute | `$4C` | 3 | 3 | Standard |
| Absolute Indirect | `$6C` | 3 | 5 | Standard |

## Descrizione
JMP Indirect
     This instruction establishes a new value for the program counter.
     It affects only the program counter in the microprocessor and affects no flags in the status register.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*