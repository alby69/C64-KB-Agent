---
title: Extract row from tile based map
source_url: https://codebase.c64.org/doku.php?id=base%3Aextract_row_from_tile_based_map
category: reference
topics:
- sprite programming
- assembly
difficulty: beginner
language: assembly
hardware:
- KERNAL
related:
- sprite-programming
- memory-map
- raster-interrupts
- kernal-routines
- vic-ii-registers
scraped_at: '2026-07-14'
---

# Extract row from tile based map

base:extract_row_from_tile_based_map

                # Extract row from tile based map

by Achim

Example 4×4 tile:

aabb ccdd eeff gghh

Tile data stored in memory:

aabbccddeeffgghh

In order to read and plot the correct tile row for a vertical scrolling game, tileY has to be defined.

```
tileY: 00, ...    aabb
       04, ...    ccdd
       08, ...    eeff
       0c, ...    gghh
```
Again a map pointer is needed (top-left) and mapX (=map width) for correct map data handling. For a straight vertical scrolling game

mapX = number of tiles left to right. In case of 4×4 tiles: mapX=#$0a, in case of 5×5 tiles mapX=#$08.

Pseudo code for scrolling down (player moving up):

lda tileY bne samemaprow //top tile row done? lda map //map - mapX sec sbc mapX sta map lda map+1 sbc #$00 sta map+1 lda #$10 //tileY=0c samemaprow: sec sbc #$04 sta tileY lda map //don't mess up map pointer... sta maptmp lda map+1 sta maptmp+1 lda lo-bytescreentop ldx hi-bytescreentop jsr extractrow ...

Pseudo code for scrolling up (player moving down):

lda map //using tmp again sta maptmp lda map+1 sta maptmp+1 ldx numbertiles //number of tiles top-bottom !: lda maptmp //calculate map row bottom clc adc mapX sta maptmp lda maptmp+1 adc #$00 sta maptmp+1 dex bpl !- lda lo-bytescreenbottom ldx hi-bytescreenbottom jsr extractrow lda tileY cmp #$0c //lowest tile row done? bne !+ lda map //map + mapX clc adc mapX sta map lda map+1 adc #$00 sta map+1 lda #$fc //tileY=00 !: clc adc #$04 sta tileY ...

Extracting a row is pretty simple…

```
/*--------------------------------------------------------------------------
Extract row from tile data
by A. Volkers, 2011
a = lo-bytescreen
x = hi-bytescreen
->KickAssambler
--------------------------------------------------------------------------*/
.pc = $1000
.const tilemem	= 	48	//hi-byte tile data: $3000
.var tileY	=	$02	//row 00, 04, 08, 0c
.var map	= 	$03	//16bit address for main program
.var mapX	=	$04	//map width
.var tiledata	=	$fc	//16bit address tile
.var maptmp	=	$fe	//16bit tmp for mappointer
extractrow:	sta plotrow+1		//prepare selfmod
		clc
		adc #$28
		sta check+1		
		stx plotrow+2		
				
extract:	ldy #$00
		lda (maptmp),y		//calculate tile data address
		and #$0f		//use tables for 5x5 tiles instead			
		asl
		asl
		asl
		asl
		sta tiledata		//lo-byte
		lda (maptmp),y
		and #$f0
		lsr
		lsr
		lsr
		lsr
		clc
                adc #tilemem		//hi-byte
		sta tiledata+1		
				
		ldy tileY		//get actual tile row
		ldx #$03		//#$04 for 5x5 tiles
readtile:	lda (tiledata),y	//read actual tile data
plotrow:	sta $ffff		//selfmod for screen position	
		inc plotrow+1
		bne !+
		inc plotrow+2
!:		lda plotrow+1		
check:		cmp #$28		//40 chars done?
		beq exit
		iny
		dex
		bpl readtile
		inc maptmp		//next tile
		bne !+
		inc maptmp+1
!:		clv
		bvc extract		
exit:		rts
```
Check out this program which uses the same routine. Hardscrolling only, no colour RAM shifting: [tile_row.zip](https://codebase.c64.org/lib/exe/fetch.php?media=base:tile_row.zip)

base/extract_row_from_tile_based_map.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
aabb
ccdd
eeff
gghh
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
aabbccddeeffgghh
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`tileY`** (unknown): No description available

```assembly
tileY: 00, ...    aabb
       04, ...    ccdd
       08, ...    eeff
       0c, ...    gghh
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`samemaprow`** (unknown): No description available

```assembly
lda tileY
		bne samemaprow		//top tile row done?
			
		lda map			//map - mapX
		sec
		sbc mapX
		sta map
		lda map+1
		sbc #$00
		sta map+1			
		lda #$10		//tileY=0c
samemaprow:	sec
		sbc #$04
		sta tileY		

		lda map			//don't mess up map pointer...
		sta maptmp
		lda map+1
		sta maptmp+1
			
		lda lo-bytescreentop
		ldx hi-bytescreentop
		jsr extractrow
		...
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
lda map			//using tmp again
		sta maptmp
		lda map+1
		sta maptmp+1	

		ldx numbertiles		//number of tiles top-bottom
!:		lda maptmp		//calculate map row bottom
		clc
		adc mapX
		sta maptmp			
		lda maptmp+1
		adc #$00
		sta maptmp+1
		dex
		bpl !-
						
		lda lo-bytescreenbottom
		ldx hi-bytescreenbottom
		jsr extractrow
			
		lda tileY
		cmp #$0c		//lowest tile row done?
		bne !+
		lda map			//map + mapX
		clc
		adc mapX
		sta map
		lda map+1
		adc #$00
		sta map+1
		lda #$fc		//tileY=00
!:		clc
		adc #$04
		sta tileY
		...
```

### Snippet Codice (BASIC)

```basic
/*--------------------------------------------------------------------------
Extract row from tile data
by A. Volkers, 2011

a = lo-bytescreen
x = hi-bytescreen

->KickAssambler
--------------------------------------------------------------------------*/
.pc = $1000

.const tilemem	= 	48	//hi-byte tile data: $3000

.var tileY	=	$02	//row 00, 04, 08, 0c
.var map	= 	$03	//16bit address for main program
.var mapX	=	$04	//map width
.var tiledata	=	$fc	//16bit address tile
.var maptmp	=	$fe	//16bit tmp for mappointer



extractrow:	sta plotrow+1		//prepare selfmod
		clc
		adc #$28
		sta check+1		
		stx plotrow+2		
				
extract:	ldy #$00
		lda (maptmp),y		//calculate tile data address
		and #$0f		//use tables for 5x5 tiles instead			
		asl
		asl
		asl
		asl
		sta tiledata		//lo-byte
		lda (maptmp),y
		and #$f0
		lsr
		lsr
		lsr
		lsr
		clc
                adc #tilemem		//hi-byte
		sta tiledata+1		
				
		ldy tileY		//get actual tile row
		ldx #$03		//#$04 for 5x5 tiles
readtile:	lda (tiledata),y	//read actual tile data
plotrow:	sta $ffff		//selfmod for screen position	
		inc plotrow+1
		bne !+
		inc plotrow+2
!:		lda plotrow+1		
check:		cmp #$28		//40 chars done?
		beq exit
		iny
		dex
		bpl readtile
		inc maptmp		//next tile
		bne !+
		inc maptmp+1
!:		clv
		bvc extract		
exit:		rts
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Aextract_row_from_tile_based_map](https://codebase.c64.org/doku.php?id=base%3Aextract_row_from_tile_based_map)*
