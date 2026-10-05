---
id: src-input
type: source
title: 'Source Summary: character from channel'
aliases:
- character from channel
- input.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/input.md
  sha256: d30c336b45f9b12be7db4ebdf748de88661d4e0a816b84df717e21a44b086ec2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: character from channel

**Raw Source File**: `data/docs/c64ref/kernal-api/input.md`
**SHA256**: `d30c336b45f9b12be7db4ebdf748de88661d4e0a816b84df717e21a44b086ec2`

## Summary



# Input — character from channel ($FFCF)

## Panoramica
La routine KERNAL `Input` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFCF`
- **Chiamata**: `JSR Input` o `SYS 65487`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A
aratory routines: (OPEN, CHKIN)
r returns: 0 (See READST)
k requirements: 7+
sters affected: A, X

scription**: This routine gets a byte of data from a channel already...
