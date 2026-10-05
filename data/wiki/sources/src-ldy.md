---
id: src-ldy
type: source
title: 'Source Summary: LDY — Load Y Register'
aliases:
- LDY — Load Y Register
- ldy.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/ldy.md
  sha256: efdb665c068522ddb695370654993a0e16f968e83c71aea9200448e0a8a26a1c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: LDY — Load Y Register

**Raw Source File**: `data/docs/c64ref/cpu-instructions/ldy.md`
**SHA256**: `efdb665c068522ddb695370654993a0e16f968e83c71aea9200448e0a8a26a1c`

## Summary



# LDY — LDY — Load Y Register

## Panoramica
L'istruzione `LDY` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `load` |
| Formula | `M → Y` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$A0` | 2 | 2 | Standard |
| Zero Page | `$A4` | 2 | 3 | Standard |
| Absolute | `$AC` | 3 | 4 |...
