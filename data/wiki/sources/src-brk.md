---
id: src-brk
type: source
title: 'Source Summary: BRK — Force Interrupt'
aliases:
- BRK — Force Interrupt
- brk.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/brk.md
  sha256: 8745337f390fce2d845060ebb072d618679a6ddd00f0eca9bf63d95b6bf84168
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BRK — Force Interrupt

**Raw Source File**: `data/docs/c64ref/cpu-instructions/brk.md`
**SHA256**: `8745337f390fce2d845060ebb072d618679a6ddd00f0eca9bf63d95b6bf84168`

## Summary



# BRK — BRK — Force Interrupt

## Panoramica
L'istruzione `BRK` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `ctrl` |
| Formula | `PC + 2↓, [FFFE] → PCL, [FFFF] → PCH` |
| Flag alterati | `-----1--` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$00` | 1 | 7 | Standard |

## Descrizione
Break Command
     The br...
