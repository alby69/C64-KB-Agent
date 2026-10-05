---
id: src-initia
type: source
title: 'Source Summary: lize RAM, reset tape buffer'
aliases:
- lize RAM, reset tape buffer
- initia.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/initia.md
  sha256: 66ffaf645449acb49853673a0b7ebd1f1ca54c58993e649febaddc49af325503
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: lize RAM, reset tape buffer

**Raw Source File**: `data/docs/c64ref/kernal-api/initia.md`
**SHA256**: `66ffaf645449acb49853673a0b7ebd1f1ca54c58993e649febaddc49af325503`

## Summary



# Initia — lize RAM, reset tape buffer ($FF87)

## Panoramica
La routine KERNAL `Initia` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF87`
- **Chiamata**: `JSR Initia` o `SYS 65415`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A, X, Y
aratory routines: None
r returns: None
k requirements: 2
sters affected: A, X, Y

scription**: This routine is used to test RAM and set the top and
 of m...
