---
id: src-bvs
type: source
title: 'Source Summary: BVS — Branch if Overflow Set'
aliases:
- BVS — Branch if Overflow Set
- bvs.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/bvs.md
  sha256: aa8609634791f8457ea7254e11e01a8c764e670b1e1e80957f65c1658e68679d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BVS — Branch if Overflow Set

**Raw Source File**: `data/docs/c64ref/cpu-instructions/bvs.md`
**SHA256**: `aa8609634791f8457ea7254e11e01a8c764e670b1e1e80957f65c1658e68679d`

## Summary



# BVS — BVS — Branch if Overflow Set

## Panoramica
L'istruzione `BVS` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `bra` |
| Formula | `Branch on V = 1` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Relative | `$70` | 2 | 2+t+p | Standard |

## Descrizione
Branch on Overflow Set
     This i...
