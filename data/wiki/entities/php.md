---
id: php
type: entity
title: PHP — Push Processor Status
aliases:
- PHP — Push Processor Status
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/php.md
  sha256: 9a295f07aa9c33b3c47237633a2d50206552a946b5b13ded180a7e3e4f4bc374
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-php
---

# PHP — Push Processor Status



# PHP — PHP — Push Processor Status

## Panoramica
L'istruzione `PHP` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `stack` |
| Formula | `P↓` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$08` | 1 | 3 | Standard |

## Descrizione
Push Processor Status On Stack
     This instruction transfers the contents of the processor status register unchanged to the stack, as governed by the stack pointer.
     The PHP instruction affects no registers or flags in the microprocessor.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-php]]
