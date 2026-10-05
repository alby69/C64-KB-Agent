---
id: src-sei
type: source
title: 'Source Summary: SEI — Set Interrupt Disable'
aliases:
- SEI — Set Interrupt Disable
- sei.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/sei.md
  sha256: 8c226f6172896f3405530079f78ee69535dfa6ef203391bc23ecf0f162ff80f4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SEI — Set Interrupt Disable

**Raw Source File**: `data/docs/c64ref/cpu-instructions/sei.md`
**SHA256**: `8c226f6172896f3405530079f78ee69535dfa6ef203391bc23ecf0f162ff80f4`

## Summary



# SEI — SEI — Set Interrupt Disable

## Panoramica
L'istruzione `SEI` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `flags` |
| Formula | `1 → I` |
| Flag alterati | `-----1--` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$78` | 1 | 2 | Standard |

## Descrizione
Set Interrupt Disable
     This instruction init...
