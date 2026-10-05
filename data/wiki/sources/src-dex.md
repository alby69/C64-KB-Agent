---
id: src-dex
type: source
title: 'Source Summary: DEX — Decrement X Register'
aliases:
- DEX — Decrement X Register
- dex.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/dex.md
  sha256: b053b72fa38d42431beabd05380160d7bdd6b8396958cd96d4214a9ff1903014
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: DEX — Decrement X Register

**Raw Source File**: `data/docs/c64ref/cpu-instructions/dex.md`
**SHA256**: `b053b72fa38d42431beabd05380160d7bdd6b8396958cd96d4214a9ff1903014`

## Summary



# DEX — DEX — Decrement X Register

## Panoramica
L'istruzione `DEX` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `inc` |
| Formula | `X - 1 → X` |
| Flag alterati | `N-----Z-` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$CA` | 1 | 2 | Standard |

## Descrizione
Decrement Index Register X By One
     This ins...
