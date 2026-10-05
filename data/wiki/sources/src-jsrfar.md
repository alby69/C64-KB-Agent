---
id: src-jsrfar
type: source
title: 'Source Summary: JSRFAR'
aliases:
- JSRFAR
- jsrfar.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/jsrfar.md
  sha256: 82a17a417facfb26379e42eea5665287f9c2125ea8f61fa557be16384110db44
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: JSRFAR

**Raw Source File**: `data/docs/c64ref/kernal-api/jsrfar.md`
**SHA256**: `82a17a417facfb26379e42eea5665287f9c2125ea8f61fa557be16384110db44`

## Summary




# JSRFAR —  ($FF6E)

## Panoramica
La routine KERNAL `JSRFAR` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF6E`
- **Chiamata**: `JSR JSRFAR` o `SYS 65390`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine jumps to a subroutine in a specified bank and re-
to the calling routine in bank 15. Prior to calling this
e, you must store the bank number (0-15) of the target
e in location 2 and the address of the t...
