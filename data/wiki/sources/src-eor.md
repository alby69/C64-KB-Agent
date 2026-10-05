---
id: src-eor
type: source
title: 'Source Summary: EOR — Exclusive OR'
aliases:
- EOR — Exclusive OR
- eor.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/eor.md
  sha256: 07554dcd8fd77d2efbcc1c22185fc7fde2f3eca8e6bb6926a632fd78e8abefb8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: EOR — Exclusive OR

**Raw Source File**: `data/docs/c64ref/cpu-instructions/eor.md`
**SHA256**: `07554dcd8fd77d2efbcc1c22185fc7fde2f3eca8e6bb6926a632fd78e8abefb8`

## Summary



# EOR — EOR — Exclusive OR

## Panoramica
L'istruzione `EOR` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `logic` |
| Formula | `A ⊻ M → A` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$41` | 2 | 6 | Standard |
| Zero Page | `$45` | 2 | 3 | Standard |
| Immed...
