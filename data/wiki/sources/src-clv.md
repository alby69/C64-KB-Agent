---
id: src-clv
type: source
title: 'Source Summary: CLV — Clear Overflow Flag'
aliases:
- CLV — Clear Overflow Flag
- clv.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/clv.md
  sha256: 868eeb6a4a4d21e23a6bbb7699d8572ee3cd36c88b6df31cf5d63e319681418e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: CLV — Clear Overflow Flag

**Raw Source File**: `data/docs/c64ref/cpu-instructions/clv.md`
**SHA256**: `868eeb6a4a4d21e23a6bbb7699d8572ee3cd36c88b6df31cf5d63e319681418e`

## Summary



# CLV — CLV — Clear Overflow Flag

## Panoramica
L'istruzione `CLV` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `flags` |
| Formula | `0 → V` |
| Flag alterati | `-0------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$B8` | 1 | 2 | Standard |

## Descrizione
Clear Overflow Flag
     This instruction clears t...
