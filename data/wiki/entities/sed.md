---
id: sed
type: entity
title: SED — Set Decimal Flag
aliases:
- SED — Set Decimal Flag
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/sed.md
  sha256: af5d6a7e69ff838d8a878b65b26e530c611e1373aac2bb7ad3cfef312bbc0890
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-sed
---

# SED — Set Decimal Flag



# SED — SED — Set Decimal Flag

## Panoramica
L'istruzione `SED` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `flags` |
| Formula | `1 → D` |
| Flag alterati | `----1---` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$F8` | 1 | 2 | Standard |

## Descrizione
Set Decimal Mode
     This instruction sets the decimal mode flag D to a 1. This makes all subsequent ADC and SBC instructions operate as a decimal arithmetic operation.
     SED affects no registers in the microprocessor and no flags other than the decimal mode which is set to a 1.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-sed]]
