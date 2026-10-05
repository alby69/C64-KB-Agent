---
id: src-bcs
type: source
title: 'Source Summary: BCS — Branch if Carry Set'
aliases:
- BCS — Branch if Carry Set
- bcs.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/bcs.md
  sha256: bd1cd950d213d774b8fb4e174e7f19e31e4f5fa478ba12a75adac77e9f0a1788
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BCS — Branch if Carry Set

**Raw Source File**: `data/docs/c64ref/cpu-instructions/bcs.md`
**SHA256**: `bd1cd950d213d774b8fb4e174e7f19e31e4f5fa478ba12a75adac77e9f0a1788`

## Summary



# BCS — BCS — Branch if Carry Set

## Panoramica
L'istruzione `BCS` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `bra` |
| Formula | `Branch on C = 1` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Relative | `$B0` | 2 | 2+t+p | Standard |

## Descrizione
Branch on Carry Set
     This instruc...
