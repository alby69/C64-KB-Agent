---
id: src-f6dd
type: source
title: 'Source Summary: SETTIM Execution F6DD/F760-F6EC/F76F'
aliases:
- SETTIM Execution F6DD/F760-F6EC/F76F
- f6dd.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/f6dd.md
  sha256: 74ff54698588261cdec90e7cf73920b4b5d480f6fa2aa8d5d6eab2b37469b426
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SETTIM Execution F6DD/F760-F6EC/F76F

**Raw Source File**: `data/docs/c64ref/kernal-api/f6dd.md`
**SHA256**: `74ff54698588261cdec90e7cf73920b4b5d480f6fa2aa8d5d6eab2b37469b426`

## Summary



# $F6DD — SETTIM Execution F6DD/F760-F6EC/F76F ($F6DD)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$F6DD`
- **Chiamata**: `JSR None` o `SYS 63197`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JMP from Kernal RDTIM vector at FFDE; alternate entry at
767 by JMP from Kernal SETTIM vector at FFDB.

he RDTIM entry point, this routine reads the jiffy
at A2-A0 into the ac...
