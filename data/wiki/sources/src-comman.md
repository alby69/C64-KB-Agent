---
id: src-comman
type: source
title: 'Source Summary: d serial bus to UNTALK'
aliases:
- d serial bus to UNTALK
- comman.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/comman.md
  sha256: 0fd860c6868ae78c07169368c4af523e13a34a5d43dcf70212a154b42f113cdb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: d serial bus to UNTALK

**Raw Source File**: `data/docs/c64ref/kernal-api/comman.md`
**SHA256**: `0fd860c6868ae78c07169368c4af523e13a34a5d43dcf70212a154b42f113cdb`

## Summary



# Comman — d serial bus to UNTALK ($FFAB)

## Panoramica
La routine KERNAL `Comman` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFAB`
- **Chiamata**: `JSR Comman` o `SYS 65451`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: None
aratory routines: None
r returns: See READST
k requirements: 8
sters affected: A

scription**: This routine transmits an UNTALK command on the serial
ll devices ...
