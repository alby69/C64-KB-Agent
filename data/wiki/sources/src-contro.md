---
id: src-contro
type: source
title: 'Source Summary: l Kernal messages'
aliases:
- l Kernal messages
- contro.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/contro.md
  sha256: 873b6972c9c221af3c278eccc47f4c0022c258a8f711b6a1f222aa0523839625
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: l Kernal messages

**Raw Source File**: `data/docs/c64ref/kernal-api/contro.md`
**SHA256**: `873b6972c9c221af3c278eccc47f4c0022c258a8f711b6a1f222aa0523839625`

## Summary



# Contro — l Kernal messages ($FF90)

## Panoramica
La routine KERNAL `Contro` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF90`
- **Chiamata**: `JSR Contro` o `SYS 65424`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A
aratory routines: None
r returns: None
k requirements: 2
sters affected: A

scription**: This routine controls the printing of error and control
es by the KERNAL. Either...
