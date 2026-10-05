---
id: src-ffdb
type: source
title: 'Source Summary: altime clock'
aliases:
- altime clock
- ffdb.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/ffdb.md
  sha256: ab9e6798018337ae459022466ee2655f5f9a0645030b139cb70b791ea8545daa
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: altime clock

**Raw Source File**: `data/docs/c64ref/kernal-api/ffdb.md`
**SHA256**: `ab9e6798018337ae459022466ee2655f5f9a0645030b139cb70b791ea8545daa`

## Summary



# $FFDB — altime clock ($FFDB)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFDB`
- **Chiamata**: `JSR None` o `SYS 65499`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A, X, Y
aratory routines: None
r returns: None
k requirements: 2
sters affected: None

scription**: A system clock is maintained by an interrupt routine that
s the clock every 1/60t...
