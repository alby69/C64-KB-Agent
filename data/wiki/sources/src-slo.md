---
id: src-slo
type: source
title: 'Source Summary: SLO'
aliases:
- SLO
- slo.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/slo.md
  sha256: 32f0f5b77c432f7896278784ad2e514d3cd0d4319502de72b2a59aeb9cfca088
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SLO

**Raw Source File**: `data/docs/c64ref/cpu-instructions/slo.md`
**SHA256**: `32f0f5b77c432f7896278784ad2e514d3cd0d4319502de72b2a59aeb9cfca088`

## Summary



# SLO — SLO

## Panoramica
L'istruzione `SLO` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `M * 2 → M, A ∨ M → A       ## Ormston: ASO` |
| Flag alterati | `*-----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$03` | 2 | 8 | Non documentata |
| Zero Page | `$07` | 2...
