---
id: src-return
type: source
title: 'Source Summary: X,Y organization of screen'
aliases:
- X,Y organization of screen
- return.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/return.md
  sha256: e97c8da4f46b65ffef202f562cdee9fa023ede65560c491c8da7b41e655cbf80
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: X,Y organization of screen

**Raw Source File**: `data/docs/c64ref/kernal-api/return.md`
**SHA256**: `e97c8da4f46b65ffef202f562cdee9fa023ede65560c491c8da7b41e655cbf80`

## Summary



# Return — X,Y organization of screen ($FFED)

## Panoramica
La routine KERNAL `Return` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFED`
- **Chiamata**: `JSR Return` o `SYS 65517`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: X, Y
aratory routines: None
k requirements: 2
sters affected: X, Y

scription**: This routine returns the format of the screen, e.g., 40
s in X and 25 lines in Y....
