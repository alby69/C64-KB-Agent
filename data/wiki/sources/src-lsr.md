---
id: src-lsr
type: source
title: 'Source Summary: LSR — Logical Shift Right'
aliases:
- LSR — Logical Shift Right
- lsr.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/lsr.md
  sha256: 18613753fa666f572a18c413f73861dd8b20cf1689b5944deb488aee5beaf23d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: LSR — Logical Shift Right

**Raw Source File**: `data/docs/c64ref/cpu-instructions/lsr.md`
**SHA256**: `18613753fa666f572a18c413f73861dd8b20cf1689b5944deb488aee5beaf23d`

## Summary



# LSR — LSR — Logical Shift Right

## Panoramica
L'istruzione `LSR` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `shift` |
| Formula | `0 → /M7...M0/ → C` |
| Flag alterati | `0-----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$46` | 2 | 5 | Standard |
| Accumulator | `$4A` | 1 | 2 | Standard |
| Absolut...
