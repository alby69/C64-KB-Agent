---
id: src-ora
type: source
title: 'Source Summary: ORA — Logical OR'
aliases:
- ORA — Logical OR
- ora.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/ora.md
  sha256: 81d6e5df30ccab4d3da3fb764b6b43b40f94f37912ba4427c92ac2a9819fb540
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ORA — Logical OR

**Raw Source File**: `data/docs/c64ref/cpu-instructions/ora.md`
**SHA256**: `81d6e5df30ccab4d3da3fb764b6b43b40f94f37912ba4427c92ac2a9819fb540`

## Summary



# ORA — ORA — Logical OR

## Panoramica
L'istruzione `ORA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `logic` |
| Formula | `A ∨ M → A` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$01` | 2 | 6 | Standard |
| Zero Page | `$05` | 2 | 3 | Standard |
| Immedia...
