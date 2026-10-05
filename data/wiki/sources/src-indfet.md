---
id: src-indfet
type: source
title: 'Source Summary: INDFET'
aliases:
- INDFET
- indfet.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/indfet.md
  sha256: f5592a3de8762c981a8643ac594343332eea7731759d19d2e189038689f4e486
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: INDFET

**Raw Source File**: `data/docs/c64ref/kernal-api/indfet.md`
**SHA256**: `f5592a3de8762c981a8643ac594343332eea7731759d19d2e189038689f4e486`

## Summary




# INDFET —  ($FF74)

## Panoramica
La routine KERNAL `INDFET` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF74`
- **Chiamata**: `JSR INDFET` o `SYS 65396`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine reads the contents of a location in a specified
Prior to calling this routine; you must load a two-byte
age pointer with the address of the location to be read
th the base location if a series of bytes ...
