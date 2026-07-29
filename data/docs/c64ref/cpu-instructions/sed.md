---
title: SED — Set Decimal Flag
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
- sbc
- sed
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: SED
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Set Decimal Mode
---

# SED — SED — Set Decimal Flag

## Panoramica
L'istruzione `SED` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `flags` |
| Formula | `1 → D` |
| Flag alterati | `----1---` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$F8` | 1 | 2 | Standard |

## Descrizione
Set Decimal Mode
     This instruction sets the decimal mode flag D to a 1. This makes all subsequent ADC and SBC instructions operate as a decimal arithmetic operation.
     SED affects no registers in the microprocessor and no flags other than the decimal mode which is set to a 1.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*