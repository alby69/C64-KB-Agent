---
id: src-output
type: source
title: 'Source Summary: byte to serial port'
aliases:
- byte to serial port
- output.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/output.md
  sha256: 4912f47fed25eb4c5e4a2029ca858e49d1b0bf5139d5f5ed26f6781965586db8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: byte to serial port

**Raw Source File**: `data/docs/c64ref/kernal-api/output.md`
**SHA256**: `4912f47fed25eb4c5e4a2029ca858e49d1b0bf5139d5f5ed26f6781965586db8`

## Summary



# Output — byte to serial port ($FFA8)

## Panoramica
La routine KERNAL `Output` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFA8`
- **Chiamata**: `JSR Output` o `SYS 65448`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A
aratory routines: LISTEN, [SECOND]
r returns: See READST
k requirements: 5
sters affected: None

scription**: This routine is used to send information to devices on th...
