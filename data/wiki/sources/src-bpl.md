---
id: src-bpl
type: source
title: 'Source Summary: BPL — Branch if Plus'
aliases:
- BPL — Branch if Plus
- bpl.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/bpl.md
  sha256: 246dd3bd189c28094640de2ad61d268c7f18f937615ec8cb916afbdbe6a5ce23
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BPL — Branch if Plus

**Raw Source File**: `data/docs/c64ref/cpu-instructions/bpl.md`
**SHA256**: `246dd3bd189c28094640de2ad61d268c7f18f937615ec8cb916afbdbe6a5ce23`

## Summary



# BPL — BPL — Branch if Plus

## Panoramica
L'istruzione `BPL` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `bra` |
| Formula | `Branch on N = 0` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Relative | `$10` | 2 | 2+t+p | Standard |

## Descrizione
Branch on Result Plus
     This instructio...
