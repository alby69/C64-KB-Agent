---
title: NOP — No Operation
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
- nop
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: NOP
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: ''
---

# NOP — NOP — No Operation

## Panoramica
L'istruzione `NOP` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `nop` |
| Formula | `No operation` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$04` | 2 | 3 | Non documentata |
| Absolute | `$0C` | 3 | 4 | Non documentata |
| X-Indexed Zero Page | `$14` | 2 | 4 | Non documentata |
| Implied | `$1A` | 1 | 2 | Non documentata |
| X-Indexed Absolute | `$1C` | 3 | 4+p | Non documentata |
| X-Indexed Zero Page | `$34` | 2 | 4 | Non documentata |
| Implied | `$3A` | 1 | 2 | Non documentata |
| X-Indexed Absolute | `$3C` | 3 | 4+p | Non documentata |
| Zero Page | `$44` | 2 | 3 | Non documentata |
| X-Indexed Zero Page | `$54` | 2 | 4 | Non documentata |
| Implied | `$5A` | 1 | 2 | Non documentata |
| X-Indexed Absolute | `$5C` | 3 | 4+p | Non documentata |
| Zero Page | `$64` | 2 | 3 | Non documentata |
| X-Indexed Zero Page | `$74` | 2 | 4 | Non documentata |
| Implied | `$7A` | 1 | 2 | Non documentata |
| X-Indexed Absolute | `$7C` | 3 | 4+p | Non documentata |
| Immediate | `$80` | 2 | 2 | Non documentata |
| Immediate | `$82` | 2 | 2 | Non documentata |
| Immediate | `$89` | 2 | 2 | Non documentata |
| Immediate | `$C2` | 2 | 2 | Non documentata |
| X-Indexed Zero Page | `$D4` | 2 | 4 | Non documentata |
| Implied | `$DA` | 1 | 2 | Non documentata |
| X-Indexed Absolute | `$DC` | 3 | 4+p | Non documentata |
| Immediate | `$E2` | 2 | 2 | Non documentata |
| Implied | `$EA` | 1 | 2 | Standard |
| X-Indexed Zero Page | `$F4` | 2 | 4 | Non documentata |
| Implied | `$FA` | 1 | 2 | Non documentata |
| X-Indexed Absolute | `$FC` | 3 | 4+p | Non documentata |

## Descrizione


---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*