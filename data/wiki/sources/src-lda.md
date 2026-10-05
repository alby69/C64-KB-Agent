---
id: src-lda
type: source
title: 'Source Summary: LDA — Load Accumulator'
aliases:
- LDA — Load Accumulator
- lda.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/lda.md
  sha256: 3492457dc00d03571e0da890c499083b07087f37c30cc7e6b99e23c4505b7c0e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: LDA — Load Accumulator

**Raw Source File**: `data/docs/c64ref/cpu-instructions/lda.md`
**SHA256**: `3492457dc00d03571e0da890c499083b07087f37c30cc7e6b99e23c4505b7c0e`

## Summary



# LDA — LDA — Load Accumulator

## Panoramica
L'istruzione `LDA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `M → A` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$A1` | 2 | 6 | Standard |
| Zero Page | `$A5` | 2 | 3 | Standard |
| Immedi...
