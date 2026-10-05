---
id: src-asl
type: source
title: 'Source Summary: ASL — Arithmetic Shift Left'
aliases:
- ASL — Arithmetic Shift Left
- asl.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/asl.md
  sha256: 9ca2d2dc72914c8dca80ba42b059a4d840ecb21f529e4d3ae8534ff556d381c9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ASL — Arithmetic Shift Left

**Raw Source File**: `data/docs/c64ref/cpu-instructions/asl.md`
**SHA256**: `9ca2d2dc72914c8dca80ba42b059a4d840ecb21f529e4d3ae8534ff556d381c9`

## Summary



# ASL — ASL — Arithmetic Shift Left

## Panoramica
L'istruzione `ASL` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `shift` |
| Formula | `C ← /M7...M0/ ← 0` |
| Flag alterati | `N-----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$06` | 2 | 5 | Standard |
| Accumulator | `$0A` | 1 | 2 | Standard |
| Absol...
