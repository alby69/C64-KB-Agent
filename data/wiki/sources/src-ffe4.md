---
id: src-ffe4
type: source
title: 'Source Summary: aracter from keyboard buffer'
aliases:
- aracter from keyboard buffer
- ffe4.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/ffe4.md
  sha256: e1819f47715462a16f970c09f6cb02af657762cb35ebac137300805b5e7fffff
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: aracter from keyboard buffer

**Raw Source File**: `data/docs/c64ref/kernal-api/ffe4.md`
**SHA256**: `e1819f47715462a16f970c09f6cb02af657762cb35ebac137300805b5e7fffff`

## Summary



# $FFE4 — aracter from keyboard buffer ($FFE4)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFE4`
- **Chiamata**: `JSR None` o `SYS 65508`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A
aratory routines: CHKIN, OPEN
r returns: See READST
k requirements: 7+
sters affected: A (X, Y)

scription**: If the channel is the keyboard, this subroutine remov...
