---
id: src-ffd5
type: source
title: 'Source Summary: AM from a device'
aliases:
- AM from a device
- ffd5.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/ffd5.md
  sha256: 015146430298cf442e97a45c5aa30c2aba7306006aa85191c3cf992349608f4e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: AM from a device

**Raw Source File**: `data/docs/c64ref/kernal-api/ffd5.md`
**SHA256**: `015146430298cf442e97a45c5aa30c2aba7306006aa85191c3cf992349608f4e`

## Summary



# $FFD5 — AM from a device ($FFD5)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFD5`
- **Chiamata**: `JSR None` o `SYS 65493`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A, X, Y
aratory routines: SETLFS, SETNAM
r returns: 0,4,5,8,9, READST
k requirements: None
sters affected: A, X, Y

scription**: This routine LOADs data bytes from any input dev...
