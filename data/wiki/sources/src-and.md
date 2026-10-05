---
id: src-and
type: source
title: 'Source Summary: AND — Logical AND'
aliases:
- AND — Logical AND
- and.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/and.md
  sha256: 33646570ad089116f232b9b9ed7a18ae73baeea0004d2d8c42baeaec77a2e07e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: AND — Logical AND

**Raw Source File**: `data/docs/c64ref/cpu-instructions/and.md`
**SHA256**: `33646570ad089116f232b9b9ed7a18ae73baeea0004d2d8c42baeaec77a2e07e`

## Summary



# AND — AND — Logical AND

## Panoramica
L'istruzione `AND` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `logic` |
| Formula | `A ∧ M → A` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$21` | 2 | 6 | Standard |
| Zero Page | `$25` | 2 | 3 | Standard |
| Immedi...
