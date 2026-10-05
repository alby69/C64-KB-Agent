---
id: anc
type: entity
title: ANC
aliases:
- ANC
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/anc.md
  sha256: 4e411f46b27fd57a58fe94ce2545f5f5b26b2d9e7a9e94a3a44e1ffcdb1e9b54
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-anc
---

# ANC



# ANC — ANC

## Panoramica
L'istruzione `ANC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `A ∧ M → A, N → C` |
| Flag alterati | `*-----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$0B` | 2 | 2 | Non documentata |
| Immediate | `$2B` | 2 | 2 | Non documentata |

## Descrizione
"AND" Memory with Accumulator then Move Negative Flag to Carry Flag
     The undocumented ANC instruction performs a bit-by-bit AND operation of the accumulator and memory and stores the result back in the accumulator.
     This instruction affects the accumulator; sets the zero flag if the result in the accumulator is 0, otherwise resets the zero flag; sets the negative flag and the carry flag if the result in the accumulator has bit 7 on, otherwise resets the negative flag and the carry flag.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-anc]]
