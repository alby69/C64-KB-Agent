---
id: jam
type: entity
title: JAM
aliases:
- JAM
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/jam.md
  sha256: 84e461e00049c8eea2c77847800eac00c54de5643faa36f6e0d4df030c624f26
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-jam
---

# JAM



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

## References
- Source: [[src-jam]]
