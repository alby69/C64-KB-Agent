---
id: src-ffde
type: source
title: 'Source Summary: ealtime clock'
aliases:
- ealtime clock
- ffde.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/ffde.md
  sha256: 92cfab67909222ac7ea69159601c046ca218c6e337fd4ea1824b6eaca0a2853b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ealtime clock

**Raw Source File**: `data/docs/c64ref/kernal-api/ffde.md`
**SHA256**: `92cfab67909222ac7ea69159601c046ca218c6e337fd4ea1824b6eaca0a2853b`

## Summary



# $FFDE — ealtime clock ($FFDE)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFDE`
- **Chiamata**: `JSR None` o `SYS 65502`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A, X, Y
aratory routines: None
r returns: None
k requirements: 2
sters affected: A, X, Y

scription**: This routine is used to read the system clock. The clock's
tion is a 60th of ...
