---
id: src-jsr
type: source
title: 'Source Summary: JSR — Jump to Subroutine'
aliases:
- JSR — Jump to Subroutine
- jsr.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/jsr.md
  sha256: 62cbedfc093c055abe2dc7a28025ec73f8d5924c5f76f6c1f3c99ffe9986e9fd
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: JSR — Jump to Subroutine

**Raw Source File**: `data/docs/c64ref/cpu-instructions/jsr.md`
**SHA256**: `62cbedfc093c055abe2dc7a28025ec73f8d5924c5f76f6c1f3c99ffe9986e9fd`

## Summary



# JSR — JSR — Jump to Subroutine

## Panoramica
L'istruzione `JSR` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `ctrl` |
| Formula | `PC + 2↓, [PC + 1] → PCL, [PC + 2] → PCH` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Absolute | `$20` | 3 | 6 | Standard |

## Descrizione
Jump To Subroutin...
