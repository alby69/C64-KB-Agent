---
id: src-rra
type: source
title: 'Source Summary: RRA'
aliases:
- RRA
- rra.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/rra.md
  sha256: 3f66c646086c8ff285e2ca614b7d52c6b0cbdb6bfd0837fb26dfdfb14fa77913
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: RRA

**Raw Source File**: `data/docs/c64ref/cpu-instructions/rra.md`
**SHA256**: `3f66c646086c8ff285e2ca614b7d52c6b0cbdb6bfd0837fb26dfdfb14fa77913`

## Summary



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
| Zero Page | `$67` | 2 | 5 | Non...
