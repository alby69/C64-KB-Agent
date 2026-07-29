---
title: ROR — Rotate Right
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
- ror
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: ROR
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Rotate Right
---

# ROR — ROR — Rotate Right

## Panoramica
L'istruzione `ROR` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `shift` |
| Formula | `C → /M7...M0/ → C` |
| Flag alterati | `N-----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$66` | 2 | 5 | Standard |
| Accumulator | `$6A` | 1 | 2 | Standard |
| Absolute | `$6E` | 3 | 6 | Standard |
| X-Indexed Zero Page | `$76` | 2 | 6 | Standard |
| X-Indexed Absolute | `$7E` | 3 | 7 | Standard |

## Descrizione
Rotate Right
     The rotate right instruction shifts either the accumulator or addressed memory right 1 bit with bit 0 shifted into the carry and carry shifted into bit 7.
     The ROR instruction either shifts the accumulator right 1 bit and stores the carry in accumulator bit 7 or does not affect the internal registers at all. The ROR instruction sets carry equal to input bit 0, sets N equal to the input carry and sets the Z flag if the result of the rotate is 0; otherwise it resets Z and does not affect the overflow flag at all.
     (Available on Microprocessors after June, 1976)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*