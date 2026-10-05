---
id: nop
type: entity
title: NOP — No Operation
aliases:
- NOP — No Operation
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/nop.md
  sha256: d4b56e95c79251f46a47c4c1ae27f99e7c6426369cb1a6e384a23f89af065018
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-nop
---

# NOP — No Operation



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

## References
- Source: [[src-nop]]
