---
id: dex
type: entity
title: DEX — Decrement X Register
aliases:
- DEX — Decrement X Register
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/dex.md
  sha256: b053b72fa38d42431beabd05380160d7bdd6b8396958cd96d4214a9ff1903014
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-dex
---

# DEX — Decrement X Register



# DEX — DEX — Decrement X Register

## Panoramica
L'istruzione `DEX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `inc` |
| Formula | `X - 1 → X` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$CA` | 1 | 2 | Standard |

## Descrizione
Decrement Index Register X By One
     This instruction subtracts one from the current value of the index register X and stores the result in the index register X.
     DEX does not affect the carry or overflow flag, it sets the N flag if it has bit 7 on as a result of the decrement, otherwise it resets the N flag; sets the Z flag if X is a 0 as a result of the decrement, otherwise it resets the Z flag.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-dex]]
