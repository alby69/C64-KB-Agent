---
id: src-getin
type: source
title: 'Source Summary: Preparation F13E/F1F5-F14D/F204'
aliases:
- Preparation F13E/F1F5-F14D/F204
- getin.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/getin.md
  sha256: a9a7a91590c9bab26a843c05e490bb8c0eac4166b2200f08593c5eac3e1f3244
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Preparation F13E/F1F5-F14D/F204

**Raw Source File**: `data/docs/c64ref/kernal-api/getin.md`
**SHA256**: `a9a7a91590c9bab26a843c05e490bb8c0eac4166b2200f08593c5eac3e1f3244`

## Summary



# GETIN — Preparation F13E/F1F5-F14D/F204 ($F13E)

## Panoramica
La routine KERNAL `GETIN` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$F13E`
- **Chiamata**: `JSR GETIN` o `SYS 61758`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: Indirect JMP through (032A) from Kernal GETIN vector at
FFE4.

outine first determines if the current input device is
yboard. If not, GETIN falls through to F14E/F205 for an
 dev...
