---
id: src-stx
type: source
title: 'Source Summary: STX — Store X Register'
aliases:
- STX — Store X Register
- stx.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/stx.md
  sha256: 98e43054fcdcaaa6dfe84b2ff6c68d514fd7c1131ba14a4e8422e1d4e8428b16
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: STX — Store X Register

**Raw Source File**: `data/docs/c64ref/cpu-instructions/stx.md`
**SHA256**: `98e43054fcdcaaa6dfe84b2ff6c68d514fd7c1131ba14a4e8422e1d4e8428b16`

## Summary



# STX — STX — Store X Register

## Panoramica
L'istruzione `STX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `X → M` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$86` | 2 | 3 | Standard |
| Absolute | `$8E` | 3 | 4 | Standard |
| Y-Indexed Zero Page | `$96...
