---
id: rra
type: entity
title: RRA
aliases:
- RRA
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/rra.md
  sha256: 3f66c646086c8ff285e2ca614b7d52c6b0cbdb6bfd0837fb26dfdfb14fa77913
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-rra
---

# RRA



# RRA — RRA

## Panoramica
L'istruzione `RRA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `C → /M7...M0/ → C, A + M + C → A` |
| Flag alterati | `**----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$63` | 2 | 8 | Non documentata |
| Zero Page | `$67` | 2 | 5 | Non documentata |
| Absolute | `$6F` | 3 | 6 | Non documentata |
| Zero Page Indirect Y-Indexed | `$73` | 2 | 8 | Non documentata |
| X-Indexed Zero Page | `$77` | 2 | 6 | Non documentata |
| Y-Indexed Absolute | `$7B` | 3 | 7 | Non documentata |
| X-Indexed Absolute | `$7F` | 3 | 7 | Non documentata |

## Descrizione
Rotate Right and Add Memory to Accumulator
     The undocumented RRA instruction shifts the addressed memory right 1 bit with bit 0 shifted into the carry and carry shifted into bit 7. It then adds the result and generated carry to the value of the accumulator and stores the result in the accumulator.
     This instruction affects the accumulator; sets the carry flag when the sum of a binary add exceeds 255 or when the sum of a decimal add exceeds 99, otherwise carry is reset. The overflow flag is set when the sign or bit 7 is changed due to the result exceeding +127 or -128, otherwise overflow is reset. The negative flag is set if the accumulator result contains bit 7 on, otherwise the negative flag is reset. The zero flag is set if the accumulator result is 0, otherwise the zero flag is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-rra]]
