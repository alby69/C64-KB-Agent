---
id: src-xaa
type: source
title: 'Source Summary: XAA'
aliases:
- XAA
- xaa.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/xaa.md
  sha256: 051f8f272448e82225d72ad966c351815a03c197ed7cd0c5b883ad4e15ad9a40
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: XAA

**Raw Source File**: `data/docs/c64ref/cpu-instructions/xaa.md`
**SHA256**: `051f8f272448e82225d72ad966c351815a03c197ed7cd0c5b883ad4e15ad9a40`

## Summary



# XAA — XAA

## Panoramica
L'istruzione `XAA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `(A ∨ V) ∧ X ∧ M → A        ## VICE, groepaz: ANE` |
| Flag alterati | `*-----*-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$8B` | 2 | 2 | Non documentata |

## Descrizione
Non-deterministic Op...
