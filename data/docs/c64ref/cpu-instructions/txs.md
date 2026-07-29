---
title: TXS — Transfer X to Stack Pointer
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
- txs
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: TXS
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Transfer Index X To Stack Pointer
---

# TXS — TXS — Transfer X to Stack Pointer

## Panoramica
L'istruzione `TXS` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `trans` |
| Formula | `X → S` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$9A` | 1 | 2 | Standard |

## Descrizione
Transfer Index X To Stack Pointer
     This instruction transfers the value in the index register X to the stack pointer.
     TXS changes only the stack pointer, making it equal to the content of the index register X. It does not affect any of the flags.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*