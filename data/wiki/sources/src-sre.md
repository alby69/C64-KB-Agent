---
id: src-sre
type: source
title: 'Source Summary: SRE'
aliases:
- SRE
- sre.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/sre.md
  sha256: 856228a4f34c2b12f57ddccb218e205a4bd173e1512505a4222bd60e8e3d3d52
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SRE

**Raw Source File**: `data/docs/c64ref/cpu-instructions/sre.md`
**SHA256**: `856228a4f34c2b12f57ddccb218e205a4bd173e1512505a4222bd60e8e3d3d52`

## Summary



# SRE — SRE

## Panoramica
L'istruzione `SRE` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `M / 2 → M, A ⊻ M → A       ## Ormston: LSE` |
| Flag alterati | `*-----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$43` | 2 | 8 | Non documentata |
| Zero Page | `$47` | 2...
