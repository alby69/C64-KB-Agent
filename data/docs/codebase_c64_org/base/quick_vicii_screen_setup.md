---
title: Quick VIC-II Screen Setup
source_url: https://codebase.c64.org/doku.php?id=base%3Aquick_vicii_screen_setup
category: reference
topics:
- graphics
- sprite programming
- assembly
difficulty: beginner
language: assembly
hardware:
- VIC-II
- CPU
- KERNAL
related:
- sprite-programming
- memory-map
- raster-interrupts
- kernal-routines
- vic-ii-registers
scraped_at: '2026-07-14'
---


# Quick VIC-II Screen Setup

base:quick_vicii_screen_setup

                # Quick VIC-II Screen Setup

This code snippet will set the both the bank and the screen address registers, given simple pointers to screenChars and screenPixels.

screenChars = $0400 ; the 40x25 buffer screenPixels = $1000 ; the pixel data for font or bitmap ($1000 or $9000 are always charrom) ; Select VIC bank lda # ((screenChars ^ $ffff) >> 14) sta $dd00 ; Set VIC screen and font pointers lda # (((screenChars & $3fff) / $0400) << 4) + (((screenPixels & $3fff) / $0800) << 1) sta $d018

by White Flame

base/quick_vicii_screen_setup.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
screenChars  = $0400 ; the 40x25 buffer
 screenPixels = $1000 ; the pixel data for font or bitmap ($1000 or $9000 are always charrom)

; Select VIC bank
 lda # ((screenChars ^ $ffff) >> 14)
 sta $dd00

; Set VIC screen and font pointers
 lda # (((screenChars & $3fff) / $0400) << 4) + (((screenPixels & $3fff) / $0800) << 1)
 sta $d018
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Aquick_vicii_screen_setup](https://codebase.c64.org/doku.php?id=base%3Aquick_vicii_screen_setup)*


### Collegamenti e Riferimenti Hardware
- **$D018 (Memory Setup Register)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d018).
