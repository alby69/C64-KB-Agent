---
id: tay
type: entity
title: TAY — Transfer Accumulator to Y
aliases:
- TAY — Transfer Accumulator to Y
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/tay.md
  sha256: 873f69d52f4c0270e7dbfaf43dc7d85233cc0cf91fcccf9d3e8420ac8fcf0821
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-tay
---

# TAY — Transfer Accumulator to Y



# TAY — TAY — Transfer Accumulator to Y

## Panoramica
L'istruzione `TAY` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `trans` |
| Formula | `A → Y` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$A8` | 1 | 2 | Standard |

## Descrizione
Transfer Accumulator To Index Y
     This instruction moves the value of the accumulator into index register Y without affecting the accumulator.
     TAY instruction only affects the Y register and does not affect either the carry or overflow flags. If the index register Y has bit 7 on, then N is set, otherwise it is reset. If the content of the index register Y equals 0 as a result of the operation, Z is set on, otherwise it is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-tay]]
