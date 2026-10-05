---
id: src-bit
type: source
title: 'Source Summary: BIT — Bit Test'
aliases:
- BIT — Bit Test
- bit.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/bit.md
  sha256: aad96f95dcbd76a453244ad6b8a94b39de677a028ced2a1f7dfaa6b5644429cd
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BIT — Bit Test

**Raw Source File**: `data/docs/c64ref/cpu-instructions/bit.md`
**SHA256**: `aad96f95dcbd76a453244ad6b8a94b39de677a028ced2a1f7dfaa6b5644429cd`

## Summary



# BIT — BIT — Bit Test

## Panoramica
L'istruzione `BIT` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `logic` |
| Formula | `A ∧ M, M7 → N, M6 → V` |
| Flag alterati | `NV----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Zero Page | `$24` | 2 | 3 | Standard |
| Absolute | `$2C` | 3 | 4 | Standard |

## Descrizione
Tes...
