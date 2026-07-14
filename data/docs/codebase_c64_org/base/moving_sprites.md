---
title: Moving sprites / Sorting movement from VIC update
source_url: https://codebase.c64.org/doku.php?id=base%3Amoving_sprites
category: reference
topics:
- raster interrupts
- sprite programming
- assembly
difficulty: beginner
language: assembly
hardware:
- SID
- VIC-II
- CPU
- KERNAL
related:
- sprite-programming
- sound-programming
- memory-map
- raster-interrupts
- sid-registers
- music-player
- kernal-routines
- vic-ii-registers
scraped_at: '2026-07-14'
---

# Moving sprites / Sorting movement from VIC update

base:moving_sprites

                ### Table of Contents

# Moving sprites / Sorting movement from VIC update

by Achim

## x+msb

Moving sprites can be annoying in terms of msb handling. To avoid the msb issue you usually use tables for moving the sprites and let a small routine update the VIC registers every frame.

spritey: .byte $00, $00, $00, $00, $00, $00, $00, $00 spritex: .byte $00, $00, $00, $00, $00, $00, $00, $00 spritemsb: .byte $00, $00, $00, $00, $00, $00, $00, $00 spritecolor: ... spritepointer: ...

Now simple 16bit additions/subtractions apply to moving sprites. The main program can ignore the msb handling.

Here's a small routine to update VIC registers. Should be called by an irq. Preferably before VIC starts to draw the next frame.

ldx #$07 ldy #$0e loop: lda spritey,x sta $d001,y //write y lda spritex,x sta $d000,y //write x lda spritemsb,x cmp #$01 //no msb=carry clear / msb=carry set rol $d010 //carry -> $d010, repeat 8 times and all bits are set lda spritecolor,x sta $d027,x lda spritepointer,x sta $07f8,x //screen at $0400 dey dey dex bpl loop

## Oldschool: x*2

This allows to use 8bit calculations for moving the sprite on x axis. No need for a msb table anymore. On the downside sprites can only be moved with 2px/frame.

spritey: .byte $00, $00, $00, $00, $00, $00, $00, $00 spritex: .byte $00, $00, $00, $00, $00, $00, $00, $00 spritecolor: ... spritepointer: ...

Update VIC registers:

```
	ldx #$07
	ldy #$0e
			
loop:	lda spritey,x
	sta $d001,y		//write y
	lda spritex,x
	asl			//x*2>$ff -> carry set=msb, x*2<=$ff -> carry clear=no msb
	sta $d000,y		//write x*2
	rol $d010		//carry -> $d010
			
	lda spritecolor,x
	sta $d027,x
	lda spritepointer,x
	sta $07f8,x		//screen at $0400
	
        dey
	dey
	dex
	bpl loop
```
base/moving_sprites.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`spritey`** (unknown): No description available
- **`spritex`** (unknown): No description available
- **`spritemsb`** (unknown): No description available
- **`spritecolor`** (unknown): No description available
- **`spritepointer`** (unknown): No description available

```assembly
spritey:	.byte $00, $00, $00, $00, $00, $00, $00, $00
spritex:	.byte $00, $00, $00, $00, $00, $00, $00, $00
spritemsb:	.byte $00, $00, $00, $00, $00, $00, $00, $00
spritecolor: 	...
spritepointer: 	...
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`loop`** (unknown): No description available

```assembly
ldx #$07
		ldy #$0e
			
loop:		lda spritey,x
		sta $d001,y		//write y
		lda spritex,x
		sta $d000,y		//write x
		lda spritemsb,x
		cmp #$01		//no msb=carry clear  / msb=carry set
		rol $d010		//carry -> $d010, repeat 8 times and all bits are set
			
		lda spritecolor,x
		sta $d027,x
		lda spritepointer,x
		sta $07f8,x		//screen at $0400

		dey
		dey
		dex
		bpl loop
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`spritey`** (unknown): No description available
- **`spritex`** (unknown): No description available
- **`spritecolor`** (unknown): No description available
- **`spritepointer`** (unknown): No description available

```assembly
spritey:	.byte $00, $00, $00, $00, $00, $00, $00, $00
spritex:	.byte $00, $00, $00, $00, $00, $00, $00, $00
spritecolor: 	...
spritepointer: 	...
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`loop`** (unknown): No description available

```assembly
ldx #$07
	ldy #$0e
			
loop:	lda spritey,x
	sta $d001,y		//write y
	lda spritex,x
	asl			//x*2>$ff -> carry set=msb, x*2<=$ff -> carry clear=no msb
	sta $d000,y		//write x*2
	rol $d010		//carry -> $d010
			
	lda spritecolor,x
	sta $d027,x
	lda spritepointer,x
	sta $07f8,x		//screen at $0400
	
        dey
	dey
	dex
	bpl loop
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Amoving_sprites](https://codebase.c64.org/doku.php?id=base%3Amoving_sprites)*
