---
id: tax
type: entity
title: TAX — Transfer Accumulator to X
aliases:
- TAX — Transfer Accumulator to X
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/tax.md
  sha256: 8c13ba0d02b4994cb747834ef3504f43254428b0007a6c3d5111f66106c8d221
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-tax
---

# TAX — Transfer Accumulator to X



# TAX — TAX — Transfer Accumulator to X

## Panoramica
L'istruzione `TAX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `trans` |
| Formula | `A → X` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$AA` | 1 | 2 | Standard |

## Descrizione
Transfer Accumulator To Index X
     This instruction takes the value from accumulator A and transfers or loads it into the index register X without disturbing the content of the accumulator A.
     TAX only affects the index register X, does not affect the carry or overflow flags. The N flag is set if the resultant value in the index register X has bit 7 on, otherwise N is reset. The Z bit is set if the content of the register X is 0 as a result of the operation, otherwise it is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-tax]]
