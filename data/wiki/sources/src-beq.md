---
id: src-beq
type: source
title: 'Source Summary: BEQ — Branch if Equal'
aliases:
- BEQ — Branch if Equal
- beq.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/beq.md
  sha256: 279236ea50b3ee71a17afdffef35ff82ffdf441a53d52d62676ed99bf186b55c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BEQ — Branch if Equal

**Raw Source File**: `data/docs/c64ref/cpu-instructions/beq.md`
**SHA256**: `279236ea50b3ee71a17afdffef35ff82ffdf441a53d52d62676ed99bf186b55c`

## Summary



# BEQ — BEQ — Branch if Equal

## Panoramica
L'istruzione `BEQ` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `bra` |
| Formula | `Branch on Z = 1` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Relative | `$F0` | 2 | 2+t+p | Standard |

## Descrizione
Branch on Result Zero
     This instructi...
