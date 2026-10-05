---
id: src-indsta
type: source
title: 'Source Summary: INDSTA'
aliases:
- INDSTA
- indsta.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/indsta.md
  sha256: 6e19093ff7ee7819c1d3b709bbfe4d25eaae187048c658e0a0b23a8fd298870b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: INDSTA

**Raw Source File**: `data/docs/c64ref/kernal-api/indsta.md`
**SHA256**: `6e19093ff7ee7819c1d3b709bbfe4d25eaae187048c658e0a0b23a8fd298870b`

## Summary




# INDSTA —  ($FF77)

## Panoramica
La routine KERNAL `INDSTA` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF77`
- **Chiamata**: `JSR INDSTA` o `SYS 65399`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine stores a value at an address in a specified bank.
 calling the routine, you must load a two-byte zero-page
r with the address of the location at which the byte is to
red (or with the base location if a ...
