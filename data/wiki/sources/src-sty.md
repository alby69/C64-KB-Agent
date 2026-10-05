---
id: src-sty
type: source
title: 'Source Summary: STY — Store Y Register'
aliases:
- STY — Store Y Register
- sty.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/sty.md
  sha256: 27bee50f4dd44d9b63b4e137665e7bf81827155037d20a6354a7fa05713f5ee2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: STY — Store Y Register

**Raw Source File**: `data/docs/c64ref/cpu-instructions/sty.md`
**SHA256**: `27bee50f4dd44d9b63b4e137665e7bf81827155037d20a6354a7fa05713f5ee2`

## Summary



# STY — STY — Store Y Register

## Panoramica
L'istruzione `STY` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `Y → M` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$84` | 2 | 3 | Standard |
| Absolute | `$8C` | 3 | 4 | Standard |
| X-Indexed Zero Page | `$94...
