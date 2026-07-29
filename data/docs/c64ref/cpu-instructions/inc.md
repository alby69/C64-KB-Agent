---
title: INC — Increment Memory
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
- inc
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: INC
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Increment Memory By One
---

# INC — INC — Increment Memory

## Panoramica
L'istruzione `INC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `inc` |
| Formula | `M + 1 → M` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$E6` | 2 | 5 | Standard |
| Absolute | `$EE` | 3 | 6 | Standard |
| X-Indexed Zero Page | `$F6` | 2 | 6 | Standard |
| X-Indexed Absolute | `$FE` | 3 | 7 | Standard |

## Descrizione
Increment Memory By One
     This instruction adds 1 to the contents of the addressed memory location.
     The increment memory instruction does not affect any internal registers and does not affect the carry or overflow flags. If bit 7 is on as the result of the increment,N is set, otherwise it is reset; if the increment causes the result to become 0, the Z flag is set on, otherwise it is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*