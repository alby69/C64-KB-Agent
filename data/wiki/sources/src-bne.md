---
id: src-bne
type: source
title: 'Source Summary: BNE — Branch if Not Equal'
aliases:
- BNE — Branch if Not Equal
- bne.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/bne.md
  sha256: 981816751a832bb529092035f138f0a4e2f11371912d0b8d164e9575a04862c3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BNE — Branch if Not Equal

**Raw Source File**: `data/docs/c64ref/cpu-instructions/bne.md`
**SHA256**: `981816751a832bb529092035f138f0a4e2f11371912d0b8d164e9575a04862c3`

## Summary



# BNE — BNE — Branch if Not Equal

## Panoramica
L'istruzione `BNE` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `bra` |
| Formula | `Branch on Z = 0` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Relative | `$D0` | 2 | 2+t+p | Standard |

## Descrizione
Branch on Result Not Zero
     This i...
