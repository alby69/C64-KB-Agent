---
title: Extract column from tile based maps
source_url: https://codebase.c64.org/doku.php?id=base%3Aextract_column_from_tile_based_map
category: reference
topics:
- assembly
- sprite programming
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- SID
related:
- sid-registers
- memory-map
- music-player
- sprite-programming
- sound-programming
- kernal-routines
- vic-ii-registers
- raster-interrupts
scraped_at: '2026-07-20'
---

# Extract column from tile based maps

# Extract column from tile based maps

by Achim

For a side scrolling game you'll have to extract one row only from your tile data and print it left or right on the screen. The following routine can be used to extract columns on either side. Call it like this:

ldy lo-bytescreen ldx hi-bytescreen jsr extractcolumn

To make this work properly a map pointer (always top/left) and tileX (=column 00, 01, 02, 03) have to be defined.

The main program should use it like this.

Pseudo code for scrolling to the right (player moving left)

ldx tileX dex bpl !+ //tileX<00? lda mappointer //shift map pointer to the left... sec sbc #$01 sta mappointer lda mappointer+1 sbc #$00 sta mappointer+1 ldx #$03 //...and start with column 03 !: stx tileX lda mappointer //use tmp to make sure sta maptmp //the map pointer lda mappointer+1 //doesn't get messed up sta maptmp+1 ldy lo-bytescreenleft ldx lo-bytescreenleft jsr extract column

To print new data on the right, switch the mappointer to top/right first. Then extract a new column, finally increment tileX (and mappointer if necessary).

Pseudo code for scrolling to the left (player moving right)

lda mappointer //switch to top/right clc adc #$0a //#$08 in case of 5x5 sta maptmp //again using a tmp lda mappointer+1 adc #$00 sta maptmp+1 ldy lo-bytescreenright ldx hi-bytescreenright jsr extract column ldx tileX inx cpx #$04 //tileX>4? bne no inc mappointer //shift map pointer to the right... bne !+ inc mappointer+1 !: ldx #$00 //...and start with column 00 no: stx tileX

Here's the code. MapX and Mappointer have to be handled by your main program.

```
/*------------------------------------------------
Extract colummn from tile data
by A. Volkers, 2011
y = lo-byte screen column
x = hi-byte screen column
->KickAssambler
------------------------------------------------*/
.pc = $1000
.const tilemem		= 	48	//hi-byte tile data: $3000
.var tileX		=	$02	//column 0-3
.var mappointer		= 	$03	//16bit address for main program
.var mapX		=	$05	//map width
.var tiledata		=	$f9	//16bit address tile
.var screenposition	= 	$fb	//16bit screen column
.var maptmp		= 	$fd	//16bit map tmp for decoding
.var numberTiles	=	$ff	//number of tiles top-bottom
			
			
newcolumn:	sty screenposition
		stx screenposition+1
		lda #$05		//5 tiles top-bottom, 20 screen rows
		sta numberTiles
readcolumn:	ldy #$00
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
			
		ldy tileX					
		lda (tiledata),y			
		ldy #$00
		sta (screenposition),y	
		lda tileX
		clc
		adc #$04
		tay
		lda (tiledata),y
		ldy #$28
		sta (screenposition),y
		lda tileX
		clc
		adc #$08
		tay
		lda (tiledata),y
		ldy #$50
		sta (screenposition),y
		lda tileX
		clc
		adc #$0c
		tay
		lda (tiledata),y
		ldy #$78
		sta (screenposition),y	//add ldy #$a0 sta(screenposition),y for 5x5 tiles
		
		lda maptmp		//next map row			
		clc	
		adc mapX					
		sta maptmp
		bcc !+
		inc maptmp+1
!:		lda screenposition	//adjust screen position
		clc
		adc #$a0		//#$c8 in case of 5x5 tiles
		sta screenposition
		bcc !+
		inc screenposition+1
!:		dec numberTiles		//all tiles done?
		bne readcolumn
		rts	
```
The following example decodes a whole screen first (using this routine: [Decoding 4x4 tiles](https://codebase.c64.org/doku.php?id=base:decoding_tile_based_maps)), then a map can be scrolled left and right (hard scrolling only). Combine it with soft scrolling and colour RAM shifting.
[tile_column.zip](https://codebase.c64.org/lib/exe/fetch.php?media=base:tile_column.zip)

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
ldy lo-bytescreen
ldx hi-bytescreen
jsr extractcolumn
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
ldx tileX
	dex
	bpl !+			//tileX<00?
	lda mappointer		//shift map pointer to the left...
	sec			
	sbc #$01
	sta mappointer
	lda mappointer+1
	sbc #$00
	sta mappointer+1
	ldx #$03		//...and start with column 03
!:	stx tileX

	lda mappointer		//use tmp to make sure
	sta maptmp		//the map pointer
	lda mappointer+1	//doesn't get messed up
	sta maptmp+1

	ldy lo-bytescreenleft
	ldx lo-bytescreenleft
	jsr extract column
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`no`** (unknown): No description available

```assembly
lda mappointer		//switch to top/right
	clc
	adc #$0a                //#$08 in case of 5x5
	sta maptmp		//again using a tmp
	lda mappointer+1
	adc #$00
	sta maptmp+1
	
	ldy lo-bytescreenright
	ldx hi-bytescreenright
	jsr extract column
	
	ldx tileX
	inx
	cpx #$04		//tileX>4?
	bne no
	inc mappointer          //shift map pointer to the right...
	bne !+
	inc mappointer+1
!:	ldx #$00                //...and start with column 00 
no:	stx tileX
```

### Snippet Codice (BASIC)

```basic
/*------------------------------------------------
Extract colummn from tile data
by A. Volkers, 2011

y = lo-byte screen column
x = hi-byte screen column

->KickAssambler
------------------------------------------------*/
.pc = $1000


.const tilemem		= 	48	//hi-byte tile data: $3000

.var tileX		=	$02	//column 0-3
.var mappointer		= 	$03	//16bit address for main program
.var mapX		=	$05	//map width
.var tiledata		=	$f9	//16bit address tile
.var screenposition	= 	$fb	//16bit screen column
.var maptmp		= 	$fd	//16bit map tmp for decoding
.var numberTiles	=	$ff	//number of tiles top-bottom
			
			

newcolumn:	sty screenposition
		stx screenposition+1
		lda #$05		//5 tiles top-bottom, 20 screen rows
		sta numberTiles

readcolumn:	ldy #$00
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
			
		ldy tileX					
		lda (tiledata),y			
		ldy #$00
		sta (screenposition),y	
		lda tileX
		clc
		adc #$04
		tay
		lda (tiledata),y
		ldy #$28
		sta (screenposition),y
		lda tileX
		clc
		adc #$08
		tay
		lda (tiledata),y
		ldy #$50
		sta (screenposition),y
		lda tileX
		clc
		adc #$0c
		tay
		lda (tiledata),y
		ldy #$78
		sta (screenposition),y	//add ldy #$a0 sta(screenposition),y for 5x5 tiles
		
		lda maptmp		//next map row			
		clc	
		adc mapX					
		sta maptmp
		bcc !+
		inc maptmp+1

!:		lda screenposition	//adjust screen position
		clc
		adc #$a0		//#$c8 in case of 5x5 tiles
		sta screenposition
		bcc !+
		inc screenposition+1

!:		dec numberTiles		//all tiles done?
		bne readcolumn
		rts
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Aextract_column_from_tile_based_map](https://codebase.c64.org/doku.php?id=base%3Aextract_column_from_tile_based_map)*
