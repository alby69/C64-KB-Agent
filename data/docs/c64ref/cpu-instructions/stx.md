---
title: STX — Store X Register
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
- stx
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: STX
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Store Index Register X In Memory
---

# STX — STX — Store X Register

## Panoramica
L'istruzione `STX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `X → M` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$86` | 2 | 3 | Standard |
| Absolute | `$8E` | 3 | 4 | Standard |
| Y-Indexed Zero Page | `$96` | 2 | 4 | Standard |

## Descrizione
Store Index Register X In Memory
     Transfers value of X register to addressed memory location.
     No flags or registers in the microprocessor are affected by the store operation.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*