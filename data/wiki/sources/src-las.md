---
id: src-las
type: source
title: 'Source Summary: LAS'
aliases:
- LAS
- las.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/las.md
  sha256: d86005d52f3eca913c093a81000de501831449a9158355d4b9f3c9443fdde32b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: LAS

**Raw Source File**: `data/docs/c64ref/cpu-instructions/las.md`
**SHA256**: `d86005d52f3eca913c093a81000de501831449a9158355d4b9f3c9443fdde32b`

## Summary



# LAS — LAS

## Panoramica
L'istruzione `LAS` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `M ∧ S → A, X, S` |
| Flag alterati | `*-----*-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Y-Indexed Absolute | `$BB` | 3 | 4+p | Non documentata |

## Descrizione
"AND" Memory with Stack Pointer
     This u...
