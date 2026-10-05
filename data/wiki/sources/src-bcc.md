---
id: src-bcc
type: source
title: 'Source Summary: BCC — Branch if Carry Clear'
aliases:
- BCC — Branch if Carry Clear
- bcc.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/bcc.md
  sha256: 12a22c60df7549870afe5ae5ff2e0ea13821d646545617b21795635ae7c3d9a7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BCC — Branch if Carry Clear

**Raw Source File**: `data/docs/c64ref/cpu-instructions/bcc.md`
**SHA256**: `12a22c60df7549870afe5ae5ff2e0ea13821d646545617b21795635ae7c3d9a7`

## Summary



# BCC — BCC — Branch if Carry Clear

## Panoramica
L'istruzione `BCC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `bra` |
| Formula | `Branch on C = 0` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Relative | `$90` | 2 | 2+t+p | Standard |

## Descrizione
Branch on Carry Clear
     This ins...
