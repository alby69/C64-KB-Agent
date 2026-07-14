---
title: Simple Software to Background collision
source_url: https://codebase.c64.org/doku.php?id=base%3Asimple_software_sprite_to_background_collision
category: reference
topics:
- sprite programming
- assembly
difficulty: beginner
language: assembly
hardware:
- VIC-II
- KERNAL
related:
- sprite-programming
- memory-map
- raster-interrupts
- kernal-routines
- vic-ii-registers
scraped_at: '2026-07-14'
---

# Simple Software to Background collision

base:simple_software_sprite_to_background_collision

                # Simple Software to Background collision

by Achim

To check wether a specific object has been hit or not, the correct screen position has to be calculated.

Use sprite-X to calculate the screen column:

lda spriteX //16bit subtraction sec sbc #$18 //x-offset, visible screen area starts at x=$18 sta tmp1 lda spriteMSB //MSB in bit 0 of spriteMSB sbc #$00 lsr //MSB -> carry lda tmp1 ror //9bit value : 8 lsr lsr sta column

If you're code uses the 2*x trick to simplify MSB-handling, an 8bit subtraction and a division by 4 is needed.

Use sprite-Y to calculate number of screen rows:

lda spriteY sec sbc #$32 //y-offset, visible screen area starts at y=$32 lsr //8bit value : 8 lsr lsr sta numberrows

Use “numberrows” to fetch actual screen row from a lookup table:

```
        ldx numberrows
        lda screenmemlowbyte,x		//=lookup table for low bytes of screen rows
        sta tmp0			//zp address
        lda screenmemhibyte,x		//=lookup table for hi bytes
        sta tmp1			//zp address+1
				
checkvalue:		
	ldy column
	lda (tmp0),y		        //read char value
	...
```
The result is the top left screen position of the sprite.

There are two options to check the other eight possible screen positions underneath the sprite (or any other position next to the sprite):

- Use different x- and y-offset values for subtraction. (Check this program:[spritebackgr.zip](https://codebase.c64.org/lib/exe/fetch.php?media=base:spritebackgr.zip), hit “x” and “y” to change offset values, Sprite located at $2000)
- Manipulate “column” to reach next two screen rows and next two screen columns: column+40=next screen row, column+80=lowest screen row, column+1=top middle of sprite, column+2=top right of sprite etc.

base/simple_software_sprite_to_background_collision.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
lda spriteX     //16bit subtraction
sec            
sbc #$18	//x-offset, visible screen area starts at x=$18
sta tmp1
lda spriteMSB	//MSB in bit 0 of spriteMSB
sbc #$00        
lsr             //MSB -> carry
lda tmp1
ror		//9bit value : 8
lsr
lsr
sta column
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
lda spriteY
sec
sbc #$32        //y-offset, visible screen area starts at y=$32
lsr		//8bit value : 8
lsr
lsr
sta numberrows
```

### Snippet Codice (BASIC)

```basic
ldx numberrows
        lda screenmemlowbyte,x		//=lookup table for low bytes of screen rows
        sta tmp0			//zp address
        lda screenmemhibyte,x		//=lookup table for hi bytes
        sta tmp1			//zp address+1
				
checkvalue:		
	ldy column
	lda (tmp0),y		        //read char value
	...
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asimple_software_sprite_to_background_collision](https://codebase.c64.org/doku.php?id=base%3Asimple_software_sprite_to_background_collision)*
