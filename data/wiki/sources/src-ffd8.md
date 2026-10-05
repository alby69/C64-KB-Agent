---
id: src-ffd8
type: source
title: 'Source Summary: AM to device'
aliases:
- AM to device
- ffd8.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/ffd8.md
  sha256: 5cf286443ec2567a0329b6c76991c59d976e0a82e41b6dcf9a88a85d4eb18083
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: AM to device

**Raw Source File**: `data/docs/c64ref/kernal-api/ffd8.md`
**SHA256**: `5cf286443ec2567a0329b6c76991c59d976e0a82e41b6dcf9a88a85d4eb18083`

## Summary



# $FFD8 — AM to device ($FFD8)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFD8`
- **Chiamata**: `JSR None` o `SYS 65496`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A, X, Y
aratory routines: SETLFS, SETNAM
r returns: 5,8,9, READST
k requirements: None
sters affected: A, X, Y


scription**: This routine saves a section of memory. Memory is saved...
