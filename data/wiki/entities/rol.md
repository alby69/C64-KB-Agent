---
id: rol
type: entity
title: ROL — Rotate Left
aliases:
- ROL — Rotate Left
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/rol.md
  sha256: 300a7ccd6663fef799ba4461701740b6f9b5a645140235ddfd7272492e50a75a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-rol
---

# ROL — Rotate Left



# ROL — ROL — Rotate Left

## Panoramica
L'istruzione `ROL` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `shift` |
| Formula | `C ← /M7...M0/ ← C` |
| Flag alterati | `N-----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$26` | 2 | 5 | Standard |
| Accumulator | `$2A` | 1 | 2 | Standard |
| Absolute | `$2E` | 3 | 6 | Standard |
| X-Indexed Zero Page | `$36` | 2 | 6 | Standard |
| X-Indexed Absolute | `$3E` | 3 | 7 | Standard |

## Descrizione
Rotate Left
     The rotate left instruction shifts either the accumulator or addressed memory left 1 bit, with the input carry being stored in bit 0 and with the input bit 7 being stored in the carry flags.
     The ROL instruction either shifts the accumulator left 1 bit and stores the carry in accumulator bit 0 or does not affect the internal registers at all. The ROL instruction sets carry equal to the input bit 7, sets N equal to the input bit 6 , sets the Z flag if the result of the rotate is 0, otherwise it resets Z and does not affect the overflow flag at all.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-rol]]
