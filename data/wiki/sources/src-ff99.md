---
id: src-ff99
type: source
title: 'Source Summary: et top of memory'
aliases:
- et top of memory
- ff99.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/ff99.md
  sha256: 99f957a173ecb8e2eb57928cca0d89b4ba3a12bedc74fd2cce7d7da8b8cad117
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: et top of memory

**Raw Source File**: `data/docs/c64ref/kernal-api/ff99.md`
**SHA256**: `99f957a173ecb8e2eb57928cca0d89b4ba3a12bedc74fd2cce7d7da8b8cad117`

## Summary



# $FF99 — et top of memory ($FF99)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF99`
- **Chiamata**: `JSR None` o `SYS 65433`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: X, Y
aratory routines: None
r returns: None
k requirements: 2
sters affected: X, Y

scription**: This routine is used to set the top of RAM. When this
e is called with the carry...
