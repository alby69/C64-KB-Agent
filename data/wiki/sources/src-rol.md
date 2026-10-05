---
id: src-rol
type: source
title: 'Source Summary: ROL — Rotate Left'
aliases:
- ROL — Rotate Left
- rol.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/rol.md
  sha256: 300a7ccd6663fef799ba4461701740b6f9b5a645140235ddfd7272492e50a75a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ROL — Rotate Left

**Raw Source File**: `data/docs/c64ref/cpu-instructions/rol.md`
**SHA256**: `300a7ccd6663fef799ba4461701740b6f9b5a645140235ddfd7272492e50a75a`

## Summary



# ROL — ROL — Rotate Left

## Panoramica
L'istruzione `ROL` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `shift` |
| Formula | `C ← /M7...M0/ ← C` |
| Flag alterati | `N-----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$26` | 2 | 5 | Standard |
| Accumulator | `$2A` | 1 | 2 | Standard |
| Absolute | `$2E...
