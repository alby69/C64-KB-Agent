---
id: src-shs
type: source
title: 'Source Summary: SHS'
aliases:
- SHS
- shs.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/shs.md
  sha256: 8e658b28e06984e5b4eb87a00e7d38daf974523a94a78ebc3b58006bd9049c89
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SHS

**Raw Source File**: `data/docs/c64ref/cpu-instructions/shs.md`
**SHA256**: `8e658b28e06984e5b4eb87a00e7d38daf974523a94a78ebc3b58006bd9049c89`

## Summary



# SHS — SHS

## Panoramica
L'istruzione `SHS` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `trans` |
| Formula | `A ∧ X → S, S ∧ (H + 1) → M ## Graham, groepaz: TAS` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Y-Indexed Absolute | `$9B` | 3 | 5 | Non documentata |

## Descrizione
Transfer ...
