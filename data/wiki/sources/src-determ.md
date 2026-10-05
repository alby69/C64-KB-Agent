---
id: src-determ
type: source
title: 'Source Summary: ine Device for SAVE F5ED/F685-F5F9/F691'
aliases:
- ine Device for SAVE F5ED/F685-F5F9/F691
- determ.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/determ.md
  sha256: 51a07f8b2db2d4bce0e3874703c9b1da5c27db47b4cfdf1b6ac60d7f4ff64df5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ine Device for SAVE F5ED/F685-F5F9/F691

**Raw Source File**: `data/docs/c64ref/kernal-api/determ.md`
**SHA256**: `51a07f8b2db2d4bce0e3874703c9b1da5c27db47b4cfdf1b6ac60d7f4ff64df5`

## Summary



# Determ — ine Device for SAVE F5ED/F685-F5F9/F691 ($F5ED)

## Panoramica
La routine KERNAL `Determ` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$F5ED`
- **Chiamata**: `JSR Determ` o `SYS 62957`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: Indirect JMP through (0322) at F5EA/F682 in Jump to SAVE
.

 current device is the keyboard or the screen, load
cumulator with 9 and set the carry bit to display the I...
