---
title: JAM
source_url: https://github.com/mist64/c64ref/blob/main/src/6502/6502_reference.txt
category: reference
topics:
- cpu-instructions
- opcodes
- addressing-modes
difficulty: advanced
language: assembly
hardware:
- '6502'
related:
- fce2-reset
- jam
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: JAM
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Halt the CPU
---

# JAM — JAM

## Panoramica
L'istruzione `JAM` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `kil` |
| Formula | `Stop execution             ## Ormston: HLT; Graham: KIL` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$02` | 1 | X | Non documentata |
| Implied | `$12` | 1 | X | Non documentata |
| Implied | `$22` | 1 | X | Non documentata |
| Implied | `$32` | 1 | X | Non documentata |
| Implied | `$42` | 1 | X | Non documentata |
| Implied | `$52` | 1 | X | Non documentata |
| Implied | `$62` | 1 | X | Non documentata |
| Implied | `$72` | 1 | X | Non documentata |
| Implied | `$92` | 1 | X | Non documentata |
| Implied | `$B2` | 1 | X | Non documentata |
| Implied | `$D2` | 1 | X | Non documentata |
| Implied | `$F2` | 1 | X | Non documentata |

## Descrizione
Halt the CPU
     This undocumented instruction stops execution. The microprocessor will not fetch further instructions, and will neither handle IRQs nor NMIs. It will handle a RESET though.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*