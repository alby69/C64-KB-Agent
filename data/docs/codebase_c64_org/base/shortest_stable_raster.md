---
title: Shortest Stable Raster code (PAL/NTSC)
source_url: https://codebase.c64.org/doku.php?id=base%3Ashortest_stable_raster
category: reference
topics:
- raster interrupts
- assembly
difficulty: advanced
language: assembly
hardware:
- VIC-II
related:
- vic-ii-registers
- raster-interrupts
- sprite-programming
scraped_at: '2026-07-20'
---


# Shortest Stable Raster code (PAL/NTSC)

base:shortest_stable_raster

                # Shortest Stable Raster code (PAL/NTSC)

The polling method, half variance technique, in its shortest form. PAL/NTSC.

```
;64tass format
stirq	.byte $a5	;subroutine
        .byte $ea
        .byte $a9 	;for NTSC, change this to $ea
        .byte $ea
	ldy #$07    
-       dey
        bne -
        inx
        rts
        ldx #$28	;main start is here!
-       cpx $d012
        bne -
        
        jsr stirq+1 	;40 cycles
        cpx $d012
        beq +
        nop
        nop
+       jsr stirq+1 	;40 cycles
        cpx $d012
        beq +
        bit $ea
+       jsr stirq  	;41 cycles
        cpx $d012
        bne +
        
+       nop      	;stable raster here
```
base/shortest_stable_raster.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
;64tass format

stirq	.byte $a5	;subroutine
        .byte $ea
        .byte $a9 	;for NTSC, change this to $ea
        .byte $ea
	ldy #$07    
-       dey
        bne -
        inx
        rts

        ldx #$28	;main start is here!
-       cpx $d012
        bne -
        
        jsr stirq+1 	;40 cycles
        cpx $d012
        beq +
        nop
        nop

+       jsr stirq+1 	;40 cycles
        cpx $d012
        beq +
        bit $ea

+       jsr stirq  	;41 cycles
        cpx $d012
        bne +
        
+       nop      	;stable raster here
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ashortest_stable_raster](https://codebase.c64.org/doku.php?id=base%3Ashortest_stable_raster)*


### Collegamenti e Riferimenti Hardware
- **$D012 (Raster Counter)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d012).
