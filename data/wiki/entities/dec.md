---
id: dec
type: entity
title: DEC — Decrement Memory
aliases:
- DEC — Decrement Memory
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/dec.md
  sha256: cfec6407523e62d8352d1e8ea6f648f254b11231316b15971013a0a35bf017b3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-dec
---

# DEC — Decrement Memory



# DEC — DEC — Decrement Memory

## Panoramica
L'istruzione `DEC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `inc` |
| Formula | `M - 1 → M` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$C6` | 2 | 5 | Standard |
| Absolute | `$CE` | 3 | 6 | Standard |
| X-Indexed Zero Page | `$D6` | 2 | 6 | Standard |
| X-Indexed Absolute | `$DE` | 3 | 7 | Standard |

## Descrizione
Decrement Memory By One
     This instruction subtracts 1, in two's complement, from the contents of the addressed memory location.
     The decrement instruction does not affect any internal register in the microprocessor. It does not affect the carry or overflow flags. If bit 7 is on as a result of the decrement, then the N flag is set, otherwise it is reset. If the result of the decrement is 0, the Z flag is set, other­wise it is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-dec]]
