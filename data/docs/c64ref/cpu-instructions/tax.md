---
title: TAX — Transfer Accumulator to X
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
- tax
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: TAX
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Transfer Accumulator To Index X
---

# TAX — TAX — Transfer Accumulator to X

## Panoramica
L'istruzione `TAX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `trans` |
| Formula | `A → X` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$AA` | 1 | 2 | Standard |

## Descrizione
Transfer Accumulator To Index X
     This instruction takes the value from accumulator A and transfers or loads it into the index register X without disturbing the content of the accumulator A.
     TAX only affects the index register X, does not affect the carry or overflow flags. The N flag is set if the resultant value in the index register X has bit 7 on, otherwise N is reset. The Z bit is set if the content of the register X is 0 as a result of the operation, otherwise it is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*