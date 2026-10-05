---
id: src-ffc0
type: source
title: 'Source Summary: logical file'
aliases:
- logical file
- ffc0.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/ffc0.md
  sha256: 6208d3e220ce5520added0fa72605b27626acf1f93e6cada587290585d7a0315
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: logical file

**Raw Source File**: `data/docs/c64ref/kernal-api/ffc0.md`
**SHA256**: `6208d3e220ce5520added0fa72605b27626acf1f93e6cada587290585d7a0315`

## Summary



# $FFC0 — logical file ($FFC0)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFC0`
- **Chiamata**: `JSR None` o `SYS 65472`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: None
aratory routines: SETLFS, SETNAM
r returns: 1,2,4,5,6,240, READST
k requirements: None
sters affected: A, X, Y

scription**: This routine is used to OPEN a logical file. Once t...
