---
id: src-ldx
type: source
title: 'Source Summary: LDX — Load X Register'
aliases:
- LDX — Load X Register
- ldx.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/ldx.md
  sha256: 924c9d9a2ec39ba90390841b387c26f634277b3c92a946415ec5870b2de34d30
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: LDX — Load X Register

**Raw Source File**: `data/docs/c64ref/cpu-instructions/ldx.md`
**SHA256**: `924c9d9a2ec39ba90390841b387c26f634277b3c92a946415ec5870b2de34d30`

## Summary



# LDX — LDX — Load X Register

## Panoramica
L'istruzione `LDX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `M → X` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$A2` | 2 | 2 | Standard |
| Zero Page | `$A6` | 2 | 3 | Standard |
| Absolute | `$AE` | 3 | 4 |...
