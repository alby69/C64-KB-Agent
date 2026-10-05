---
id: src-ror
type: source
title: 'Source Summary: ROR — Rotate Right'
aliases:
- ROR — Rotate Right
- ror.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/ror.md
  sha256: 2a7f364aa3605a23139532ac196362be7f90a582d49ee6272c235367456ec828
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ROR — Rotate Right

**Raw Source File**: `data/docs/c64ref/cpu-instructions/ror.md`
**SHA256**: `2a7f364aa3605a23139532ac196362be7f90a582d49ee6272c235367456ec828`

## Summary



# ROR — ROR — Rotate Right

## Panoramica
L'istruzione `ROR` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `shift` |
| Formula | `C → /M7...M0/ → C` |
| Flag alterati | `N-----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$66` | 2 | 5 | Standard |
| Accumulator | `$6A` | 1 | 2 | Standard |
| Absolute | `$6...
