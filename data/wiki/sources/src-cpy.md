---
id: src-cpy
type: source
title: 'Source Summary: CPY — Compare Y Register'
aliases:
- CPY — Compare Y Register
- cpy.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/cpy.md
  sha256: 139ad2cdddee94339e37a057b7890addf87949f927dd253aaca45f6dccbca2ac
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: CPY — Compare Y Register

**Raw Source File**: `data/docs/c64ref/cpu-instructions/cpy.md`
**SHA256**: `139ad2cdddee94339e37a057b7890addf87949f927dd253aaca45f6dccbca2ac`

## Summary



# CPY — CPY — Compare Y Register

## Panoramica
L'istruzione `CPY` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `Y - M` |
| Flag alterati | `N-----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$C0` | 2 | 2 | Standard |
| Zero Page | `$C4` | 2 | 3 | Standard |
| Absolute | `$CC` | 3 |...
