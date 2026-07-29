---
title: LDA — Load Accumulator
source_url: https://github.com/mist64/c64ref/blob/main/src/6502/6502_reference.txt
category: reference
topics:
- cpu-instructions
- opcodes
- addressing-modes
difficulty: intermediate
language: assembly
hardware:
- '6502'
related:
- lda
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: LDA
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Load Accumulator with Memory
---

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