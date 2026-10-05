---
id: src-lax
type: source
title: 'Source Summary: LAX'
aliases:
- LAX
- lax.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/lax.md
  sha256: 50381cc9ed448f336358317f93d3f03ec7a78e25df2570b084f5b7796c88b423
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: LAX

**Raw Source File**: `data/docs/c64ref/cpu-instructions/lax.md`
**SHA256**: `50381cc9ed448f336358317f93d3f03ec7a78e25df2570b084f5b7796c88b423`

## Summary



# LAX — LAX

## Panoramica
L'istruzione `LAX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `M → A, X` |
| Flag alterati | `*-----*-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$A3` | 2 | 6 | Non documentata |
| Zero Page | `$A7` | 2 | 3 | Non documentata |
| Immediat...
