---
id: src-ffbd
type: source
title: 'Source Summary: lename'
aliases:
- lename
- ffbd.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/ffbd.md
  sha256: 68a4c23d0fe6a6c3a141c2b317c7df8759af3c7167d035495c6f977fa02f1ac7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: lename

**Raw Source File**: `data/docs/c64ref/kernal-api/ffbd.md`
**SHA256**: `68a4c23d0fe6a6c3a141c2b317c7df8759af3c7167d035495c6f977fa02f1ac7`

## Summary



# $FFBD — lename ($FFBD)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFBD`
- **Chiamata**: `JSR None` o `SYS 65469`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A, X, Y
aratory routines:
k requirements: 2
sters affected:

scription**: This routine is used to set up the file name for the OPEN,
or LOAD routines. The accumulator must be loaded with ...
