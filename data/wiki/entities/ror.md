---
id: ror
type: entity
title: ROR — Rotate Right
aliases:
- ROR — Rotate Right
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/ror.md
  sha256: 2a7f364aa3605a23139532ac196362be7f90a582d49ee6272c235367456ec828
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ror
---

# ROR — Rotate Right



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

## References
- Source: [[src-ror]]
