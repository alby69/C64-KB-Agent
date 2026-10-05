---
id: src-sec
type: source
title: 'Source Summary: SEC — Set Carry Flag'
aliases:
- SEC — Set Carry Flag
- sec.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/sec.md
  sha256: 7757b8491a94ea35bb902325cceb3af2c05fbe9b50f842f014d6df994cc70fb2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SEC — Set Carry Flag

**Raw Source File**: `data/docs/c64ref/cpu-instructions/sec.md`
**SHA256**: `7757b8491a94ea35bb902325cceb3af2c05fbe9b50f842f014d6df994cc70fb2`

## Summary



# SEC — SEC — Set Carry Flag

## Panoramica
L'istruzione `SEC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `flags` |
| Formula | `1 → C` |
| Flag alterati | `-------1` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$38` | 1 | 2 | Standard |

## Descrizione
Set Carry Flag
     This instruction initializes the ca...
