---
id: src-check
type: source
title: 'Source Summary: for STOP key'
aliases:
- for STOP key
- check.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/check.md
  sha256: 9f85b6186ddc39a8cf2b0c65144a45ec7eb3acb323904ab1c3646c4f3249ffc6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: for STOP key

**Raw Source File**: `data/docs/c64ref/kernal-api/check.md`
**SHA256**: `9f85b6186ddc39a8cf2b0c65144a45ec7eb3acb323904ab1c3646c4f3249ffc6`

## Summary



# Check — for STOP key ($FFE1)

## Panoramica
La routine KERNAL `Check` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFE1`
- **Chiamata**: `JSR Check` o `SYS 65505`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A
aratory routines: None
r returns: None
k requirements: None
sters affected: A, X

scription**: If the <STOP> key on the keyboard was pressed during a
call, this call returns the...
