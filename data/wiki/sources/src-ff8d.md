---
id: src-ff8d
type: source
title: 'Source Summary: et vectored I/O'
aliases:
- et vectored I/O
- ff8d.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/ff8d.md
  sha256: 2208c56dfee83202038a8ae2d3714dcba4a7ffa5777b304792c21dcebcefefcd
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: et vectored I/O

**Raw Source File**: `data/docs/c64ref/kernal-api/ff8d.md`
**SHA256**: `2208c56dfee83202038a8ae2d3714dcba4a7ffa5777b304792c21dcebcefefcd`

## Summary



# $FF8D — et vectored I/O ($FF8D)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF8D`
- **Chiamata**: `JSR None` o `SYS 65421`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: X, Y
aratory routines: None
r returns: None
k requirements: 2
sters affected: A, X, Y


scription**: This routine manages all system vector jump addresses
 in RAM. Calling this r...
