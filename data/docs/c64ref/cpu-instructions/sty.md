---
title: STY — Store Y Register
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
- sty
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: STY
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Store Index Register Y In Memory
---

# STY — STY — Store Y Register

## Panoramica
L'istruzione `STY` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `Y → M` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$84` | 2 | 3 | Standard |
| Absolute | `$8C` | 3 | 4 | Standard |
| X-Indexed Zero Page | `$94` | 2 | 4 | Standard |

## Descrizione
Store Index Register Y In Memory
     Transfer the value of the Y register to the addressed memory location.
     STY does not affect any flags or registers in the microprocessor.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*