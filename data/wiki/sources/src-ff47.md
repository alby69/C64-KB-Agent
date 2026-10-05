---
id: src-ff47
type: source
title: 'Source Summary: N_SPOUT'
aliases:
- N_SPOUT
- ff47.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/ff47.md
  sha256: cc4f786dceb5061c4cf23bad5358a7334bb3bfad27b687968c4f840273fc2b70
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: N_SPOUT

**Raw Source File**: `data/docs/c64ref/kernal-api/ff47.md`
**SHA256**: `cc4f786dceb5061c4cf23bad5358a7334bb3bfad27b687968c4f840273fc2b70`

## Summary



# $FF47 — N_SPOUT ($FF47)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF47`
- **Chiamata**: `JSR None` o `SYS 65351`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
ow-level serial I/O routine sets up the serial bus for fast
 mode) communications. Unless you're writing a custom
ransfer routine, it's not necessary to call this routine
itly. All higher-level serial 1/0 rou...
