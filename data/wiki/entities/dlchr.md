---
id: dlchr
type: entity
title: DLCHR
aliases:
- DLCHR
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/dlchr.md
  sha256: 1757fa85481ef19f204a4481318a362b25ef784ac9e7770b7813697bf23a90d1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-dlchr
---

# DLCHR




# DLCHR —  ($FF62)

## Panoramica
La routine KERNAL `DLCHR` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF62`
- **Chiamata**: `JSR DLCHR` o `SYS 65378`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine copies character shape data for both standard
aracter sets into the VDC video chip's private block of
roviding character definitions for the 80-column dis-
(The VDC has no character ROM.) This routine is also
 as part of IOEMFI for the 128.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-dlchr]]
