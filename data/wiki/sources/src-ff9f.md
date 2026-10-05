---
id: src-ff9f
type: source
title: 'Source Summary: eyboard'
aliases:
- eyboard
- ff9f.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/ff9f.md
  sha256: 43f4ec09a9242bfd51da4ebcb2095950261a9f81670653b3c30189cd43c1adf6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: eyboard

**Raw Source File**: `data/docs/c64ref/kernal-api/ff9f.md`
**SHA256**: `43f4ec09a9242bfd51da4ebcb2095950261a9f81670653b3c30189cd43c1adf6`

## Summary



# $FF9F — eyboard ($FF9F)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF9F`
- **Chiamata**: `JSR None` o `SYS 65439`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: None
aratory routines: IOINIT
r returns: None
k requirements: 5
sters affected: A, X, Y

scription**: This routine scans the Commodore 64 keyboard and checks
essed keys. It is the same r...
