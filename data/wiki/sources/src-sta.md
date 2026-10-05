---
id: src-sta
type: source
title: 'Source Summary: STA — Store Accumulator'
aliases:
- STA — Store Accumulator
- sta.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/sta.md
  sha256: 2647234d68b4a95498da37c60120e2f6ed6ea4d7dc5353c4181592e4b24389a5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: STA — Store Accumulator

**Raw Source File**: `data/docs/c64ref/cpu-instructions/sta.md`
**SHA256**: `2647234d68b4a95498da37c60120e2f6ed6ea4d7dc5353c4181592e4b24389a5`

## Summary



# STA — STA — Store Accumulator

## Panoramica
L'istruzione `STA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `A → M` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$81` | 2 | 6 | Standard |
| Zero Page | `$85` | 2 | 3 | Standard |
| Absol...
