---
id: src-dcp
type: source
title: 'Source Summary: DCP'
aliases:
- DCP
- dcp.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/dcp.md
  sha256: c4a99bb1249a061c6c1db7b66d7ec761e8c7e7d9459c0da904cb9a112616a73a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: DCP

**Raw Source File**: `data/docs/c64ref/cpu-instructions/dcp.md`
**SHA256**: `c4a99bb1249a061c6c1db7b66d7ec761e8c7e7d9459c0da904cb9a112616a73a`

## Summary



# DCP — DCP

## Panoramica
L'istruzione `DCP` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `M - 1 → M, A - M           ## Ormston: DCM` |
| Flag alterati | `*-----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$C3` | 2 | 8 | Non documentata |
| Zero Page | `$C7` | 2...
