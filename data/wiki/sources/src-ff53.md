---
id: src-ff53
type: source
title: 'Source Summary: _CALL'
aliases:
- _CALL
- ff53.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/ff53.md
  sha256: ebfed6a23f60b2079d564e5d923800dfe717804b925ed698e53a33c3c4842707
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: _CALL

**Raw Source File**: `data/docs/c64ref/kernal-api/ff53.md`
**SHA256**: `ebfed6a23f60b2079d564e5d923800dfe717804b925ed698e53a33c3c4842707`

## Summary



# $FF53 — _CALL ($FF53)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF53`
- **Chiamata**: `JSR None` o `SYS 65363`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine attempts to load and execute boot sectors from a
ied disk drive. Call the routine with .X holding the de-
umber for the drive (usually 8) and with the accu-
r holding the character code corresponding to ...
