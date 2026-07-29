---
title: CLD — Clear Decimal Mode
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
- adc
- cld
- sbc
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: CLD
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Clear Decimal Mode
---

# CLD — CLD — Clear Decimal Mode

## Panoramica
L'istruzione `CLD` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `flags` |
| Formula | `0 → D` |
| Flag alterati | `----0---` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$D8` | 1 | 2 | Standard |

## Descrizione
Clear Decimal Mode
     This instruction sets the decimal mode flag to a 0. This all subsequent ADC and SBC instructions to operate as simple operations.
     CLD affects no registers in the microprocessor and no flags other than the decimal mode flag which is set to a 0.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*