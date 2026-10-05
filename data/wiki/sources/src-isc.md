---
id: src-isc
type: source
title: 'Source Summary: ISC'
aliases:
- ISC
- isc.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/isc.md
  sha256: 3d6bd1cc5646340c9598076320b6a93400c74b59aa35b26202a9d6530cb60a6a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ISC

**Raw Source File**: `data/docs/c64ref/cpu-instructions/isc.md`
**SHA256**: `3d6bd1cc5646340c9598076320b6a93400c74b59aa35b26202a9d6530cb60a6a`

## Summary



# ISC — ISC

## Panoramica
L'istruzione `ISC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `M + 1 → M, A - M → A       ## Ormston: INS; VICE: ISB` |
| Flag alterati | `**----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$E3` | 2 | 8 | Non documentata |
| Zero Page ...
