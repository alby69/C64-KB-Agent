---
id: src-increm
type: source
title: 'Source Summary: ent realtime clock'
aliases:
- ent realtime clock
- increm.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/increm.md
  sha256: 622e1a26f1f33347d7eea9a80cd4f00fcdb733a40118d805a35c66c6436d9dad
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ent realtime clock

**Raw Source File**: `data/docs/c64ref/kernal-api/increm.md`
**SHA256**: `622e1a26f1f33347d7eea9a80cd4f00fcdb733a40118d805a35c66c6436d9dad`

## Summary



# Increm — ent realtime clock ($FFEA)

## Panoramica
La routine KERNAL `Increm` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFEA`
- **Chiamata**: `JSR Increm` o `SYS 65514`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: None
aratory routines: None
r returns: None
k requirements: 2
sters affected: A, X

scription**: This routine updates the system clock. Normally this
e is called by the n...
