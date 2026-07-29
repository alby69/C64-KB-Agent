---
title: CLV — Clear Overflow Flag
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
- clv
scraped_at: '2026-07-29'
c64ref:
  module: '6502'
  source_files:
  - 6502_reference.txt
  address: null
  symbol: CLV
  sources:
  - name: 6502 Reference
    author: MOS Technology
    description: Clear Overflow Flag
---

# CLV — CLV — Clear Overflow Flag

## Panoramica
L'istruzione `CLV` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `flags` |
| Formula | `0 → V` |
| Flag alterati | `-0------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$B8` | 1 | 2 | Standard |

## Descrizione
Clear Overflow Flag
     This instruction clears the overflow flag to a 0. This command is used in conjunction with the set overflow pin which can change the state of the overflow flag with an external signal.
     CLV affects no registers in the microprocessor and no flags other than the overflow flag which is set to a 0.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*