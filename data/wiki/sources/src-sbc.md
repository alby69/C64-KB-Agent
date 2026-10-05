---
id: src-sbc
type: source
title: 'Source Summary: SBC — Subtract with Carry'
aliases:
- SBC — Subtract with Carry
- sbc.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/sbc.md
  sha256: 56f0491e239adafa981ff5b2a8e052068a6f76f165dc9bdb51090442f83da65f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SBC — Subtract with Carry

**Raw Source File**: `data/docs/c64ref/cpu-instructions/sbc.md`
**SHA256**: `56f0491e239adafa981ff5b2a8e052068a6f76f165dc9bdb51090442f83da65f`

## Summary



# SBC — SBC — Subtract with Carry

## Panoramica
L'istruzione `SBC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `A - M - ~C → A` |
| Flag alterati | `NV----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$E1` | 2 | 6 | Standard |
| Zero Page | `$E5` | 2 | 3 | Standa...
