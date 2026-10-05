---
id: src-dey
type: source
title: 'Source Summary: DEY — Decrement Y Register'
aliases:
- DEY — Decrement Y Register
- dey.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/dey.md
  sha256: 2bc337e5f72c533c7c0f5475d1674a8cfab32b5398cc5aea4c83c478c7b85da5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: DEY — Decrement Y Register

**Raw Source File**: `data/docs/c64ref/cpu-instructions/dey.md`
**SHA256**: `2bc337e5f72c533c7c0f5475d1674a8cfab32b5398cc5aea4c83c478c7b85da5`

## Summary



# DEY — DEY — Decrement Y Register

## Panoramica
L'istruzione `DEY` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `inc` |
| Formula | `Y - 1 → Y` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$88` | 1 | 2 | Standard |

## Descrizione
Decrement Index Register Y By One
     This ins...
