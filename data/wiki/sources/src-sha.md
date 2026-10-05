---
id: src-sha
type: source
title: 'Source Summary: SHA'
aliases:
- SHA
- sha.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/sha.md
  sha256: 58b2d84e8b625907fbe275dd9e7ce83fac96e2af57b383ca22b4410a2c80f2f6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SHA

**Raw Source File**: `data/docs/c64ref/cpu-instructions/sha.md`
**SHA256**: `58b2d84e8b625907fbe275dd9e7ce83fac96e2af57b383ca22b4410a2c80f2f6`

## Summary



# SHA — SHA

## Panoramica
L'istruzione `SHA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `A ∧ X ∧ V → M              ## Graham: AHX` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page Indirect Y-Indexed | `$93` | 2 | 6 | Non documentata |
| Y-Indexed Absolute | `$...
