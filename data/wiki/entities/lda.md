---
id: lda
type: entity
title: LDA — Load Accumulator
aliases:
- LDA — Load Accumulator
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/lda.md
  sha256: 3492457dc00d03571e0da890c499083b07087f37c30cc7e6b99e23c4505b7c0e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-lda
---

# LDA — Load Accumulator



# LDA — LDA — Load Accumulator

## Panoramica
L'istruzione `LDA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `M → A` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$A1` | 2 | 6 | Standard |
| Zero Page | `$A5` | 2 | 3 | Standard |
| Immediate | `$A9` | 2 | 2 | Standard |
| Absolute | `$AD` | 3 | 4 | Standard |
| Zero Page Indirect Y-Indexed | `$B1` | 2 | 5+p | Standard |
| X-Indexed Zero Page | `$B5` | 2 | 4 | Standard |
| Y-Indexed Absolute | `$B9` | 3 | 4+p | Standard |
| X-Indexed Absolute | `$BD` | 3 | 4+p | Standard |

## Descrizione
Load Accumulator with Memory
     When instruction LDA is executed by the microprocessor, data is transferred from memory to the accumulator and stored in the accumulator.
     LDA affects the contents of the accumulator, does not affect the carry or overflow flags; sets the zero flag if the accumulator is zero as a result of the LDA, otherwise resets the zero flag; sets the negative flag if bit 7 of the accumulator is a 1, other­ wise resets the negative flag.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-lda]]
