---
title: LAS
source_url: https://github.com/mist64/c64ref/blob/main/src/6502/6502_reference.txt
category: reference
topics:
- cpu-instructions
- opcodes
- addressing-modes
difficulty: advanced
language: assembly
hardware:
- '6502'
related:
- las
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: LAS
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: '"AND" Memory with Stack Pointer'
---

# LAS — LAS

## Panoramica
L'istruzione `LAS` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `M ∧ S → A, X, S` |
| Flag alterati | `*-----*-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Y-Indexed Absolute | `$BB` | 3 | 4+p | Non documentata |

## Descrizione
"AND" Memory with Stack Pointer
     This undocumented instruction performs a bit-by-bit "AND" operation of the stack pointer and memory and stores the result back in the accumulator, the index register X and the stack pointer.
      The LAS instruction does not affect the carry or overflow flags. It sets N if the bit 7 of the result is on, otherwise it is reset. If the result is zero, then the Z flag is set, otherwise it is reset.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*