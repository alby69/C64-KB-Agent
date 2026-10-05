---
id: src-close
type: source
title: 'Source Summary: input and output channels'
aliases:
- input and output channels
- close.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/close.md
  sha256: 50c2b7087e82d02499df7a1e1912def31f07edd740852c55b6326a42f3d720a9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: input and output channels

**Raw Source File**: `data/docs/c64ref/kernal-api/close.md`
**SHA256**: `50c2b7087e82d02499df7a1e1912def31f07edd740852c55b6326a42f3d720a9`

## Summary



# Close — input and output channels ($FFCC)

## Panoramica
La routine KERNAL `Close` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFCC`
- **Chiamata**: `JSR Close` o `SYS 65484`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: None
aratory routines: None
r returns:
k requirements: 9
sters affected: A, X

scription**: This routine is called to clear all open channels and re-
the I/O channels...
