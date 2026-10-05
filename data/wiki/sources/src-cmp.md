---
id: src-cmp
type: source
title: 'Source Summary: CMP — Compare'
aliases:
- CMP — Compare
- cmp.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/cmp.md
  sha256: 4ff12b93a21a2ddc37c927f565ec38fa702a245ac798b36b27f32cee8597d367
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: CMP — Compare

**Raw Source File**: `data/docs/c64ref/cpu-instructions/cmp.md`
**SHA256**: `4ff12b93a21a2ddc37c927f565ec38fa702a245ac798b36b27f32cee8597d367`

## Summary



# CMP — CMP — Compare

## Panoramica
L'istruzione `CMP` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `A - M` |
| Flag alterati | `N-----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$C1` | 2 | 6 | Standard |
| Zero Page | `$C5` | 2 | 3 | Standard |
| Immediate | `$...
