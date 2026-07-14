---
title: Swapping ZeroPage data
source_url: https://codebase.c64.org/doku.php?id=base%3Aswapping_zp_data
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware:
- SID
- KERNAL
related:
- sound-programming
- memory-map
- sid-registers
- music-player
- kernal-routines
scraped_at: '2026-07-14'
---

# Swapping ZeroPage data

base:swapping_zp_data

                # Swapping ZeroPage data

On some occasions you might want to save and restore ZP data. I.e. you have no time to patch a SID player, or the speedup you gain by giving several routines full ZP access is worth it. The small snippet below swaps 10 bytes from $00 on with memory in $10. It clutters X,Y and A though. Enjoy, enthusi.

ldx #10 loop ldy $00,x lda $10,x sta $00,x sty $10,x dex bpl loop

base/swapping_zp_data.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
ldx #10 
loop 
   ldy $00,x 
   lda $10,x 
   sta $00,x 
   sty $10,x 
   dex 
   bpl loop
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Aswapping_zp_data](https://codebase.c64.org/doku.php?id=base%3Aswapping_zp_data)*
