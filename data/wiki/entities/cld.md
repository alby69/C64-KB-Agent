---
id: cld
type: entity
title: CLD — Clear Decimal Mode
aliases:
- CLD — Clear Decimal Mode
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/cld.md
  sha256: 988f77f67a2eab3c54566c5d44ebe7b82e42c5ff2fb91eee5ed2f1910f87beb5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-cld
---

# CLD — Clear Decimal Mode



# CLD — CLD — Clear Decimal Mode

## Panoramica
L'istruzione `CLD` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `flags` |
| Formula | `0 → D` |
| Flag alterati | `----0---` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$D8` | 1 | 2 | Standard |

## Descrizione
Clear Decimal Mode
     This instruction sets the decimal mode flag to a 0. This all subsequent ADC and SBC instructions to operate as simple operations.
     CLD affects no registers in the microprocessor and no flags other than the decimal mode flag which is set to a 0.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-cld]]
