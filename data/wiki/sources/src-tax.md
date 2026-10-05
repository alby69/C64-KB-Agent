---
id: src-tax
type: source
title: 'Source Summary: TAX — Transfer Accumulator to X'
aliases:
- TAX — Transfer Accumulator to X
- tax.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/tax.md
  sha256: 8c13ba0d02b4994cb747834ef3504f43254428b0007a6c3d5111f66106c8d221
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: TAX — Transfer Accumulator to X

**Raw Source File**: `data/docs/c64ref/cpu-instructions/tax.md`
**SHA256**: `8c13ba0d02b4994cb747834ef3504f43254428b0007a6c3d5111f66106c8d221`

## Summary



# TAX — TAX — Transfer Accumulator to X

## Panoramica
L'istruzione `TAX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `trans` |
| Formula | `A → X` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$AA` | 1 | 2 | Standard |

## Descrizione
Transfer Accumulator To Index X
     This in...
