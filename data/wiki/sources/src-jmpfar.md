---
id: src-jmpfar
type: source
title: 'Source Summary: JMPFAR'
aliases:
- JMPFAR
- jmpfar.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/jmpfar.md
  sha256: cafbbe0bca5d4a97f3ae82d453f1b80a126604a7f771d60a286257270d1948e3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: JMPFAR

**Raw Source File**: `data/docs/c64ref/kernal-api/jmpfar.md`
**SHA256**: `cafbbe0bca5d4a97f3ae82d453f1b80a126604a7f771d60a286257270d1948e3`

## Summary




# JMPFAR —  ($FF71)

## Panoramica
La routine KERNAL `JMPFAR` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF71`
- **Chiamata**: `JSR JMPFAR` o `SYS 65393`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
jumps to a routine in a specified bank, with no return
 calling bank. Prior to calling this routine, you must store
nk number (0-15) of the target routine in location 2 and
dress of the target routine in locat...
