---
id: src-cpx
type: source
title: 'Source Summary: CPX — Compare X Register'
aliases:
- CPX — Compare X Register
- cpx.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/cpx.md
  sha256: 1193524ebdfa713acbc38cf4e89ae6fb80a62a9239d3c7d6e23d258f975dfc1c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: CPX — Compare X Register

**Raw Source File**: `data/docs/c64ref/cpu-instructions/cpx.md`
**SHA256**: `1193524ebdfa713acbc38cf4e89ae6fb80a62a9239d3c7d6e23d258f975dfc1c`

## Summary



# CPX — CPX — Compare X Register

## Panoramica
L'istruzione `CPX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `X - M` |
| Flag alterati | `N-----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$E0` | 2 | 2 | Standard |
| Zero Page | `$E4` | 2 | 3 | Standard |
| Absolute | `$EC` | 3 |...
