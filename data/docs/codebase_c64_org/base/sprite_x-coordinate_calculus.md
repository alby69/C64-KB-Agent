---
title: base:sprite_x-coordinate_calculus [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Asprite_x-coordinate_calculus
category: reference
topics:
- assembly
- sprite programming
difficulty: intermediate
language: assembly
hardware:
- KERNAL
- VIC-II
related:
- memory-map
- sprite-programming
- kernal-routines
- vic-ii-registers
- raster-interrupts
scraped_at: '2026-07-20'
---

# base:sprite_x-coordinate_calculus [Codebase64 wiki]

base:sprite_x-coordinate_calculus

                ## Signed Sprite X-Coordinate calculus: by delta table

This piece of code adds a signed byte (from the delta table) to an unsigned byte (the sprite x-coordinate) and returns a unsigned 9-bit number, storing the lower 8-bits on the sprite x-coordinate register and 9th bit on the sprite x-coordinate MSB register.

```
	;Calc new sprite 0 X-coordinate by delta table
        ;by The_WOZ/soft154i
        ; XDELTA = delta table for X
        ; y register = XDELTA index
	clc
	clv
	lda	$D000           ;Load first operand: sprite0 x-coordinate
	bmi	.pxa0           ;Test sign of first operand
	adc	XDELTA,y	;First operand is positive (in 2's complement)
	sta	$D000
	bpl	.cnt
	bvs	.cnt
	lda	#$fe		;Reset MSB
	and	$D010
	jmp	.pxm0
.pxa0
	adc	XDELTA,y	;First operand is negative
	sta	$D000
	bvs	.cnt
	bcc	.cnt
	bmi	.cnt
	lda	#$01		;Set MSB
	ora	$D010
.pxm0	sta	$D010
.cnt    ;--- Rest of the program ---
; X Delta table, ACME format
XDELTA !byte 5,6,5,6,5,6
      !byte 5,5,5,5,5,4
      !byte 4,4,4,4,3,4
      !byte 3,2,3,2,2,2
      !byte 1,1,1,1,0,0
      !byte 0,0,0,-1,-1,-1
      !byte -1,-1,-1,-2,-2,-1
      !byte -2,-2,-2,-2,-1,-2
      !byte -2,-2,-1,-2,-2,-1
      !byte -2,-1,-1,-1,-1,0
      !byte -1,0,-1,0,0,1
      !byte 0,1,0,1,1,1
      !byte 1,2,1,2,2,1
      !byte 2,2,2,1,2,2
      !byte 2,2,1,2,2,1
      !byte 1,1,1,1,1,0
      !byte 0,0,0,0,-1,-1
      !byte -1,-1,-2,-2,-2,-3
      !byte -2,-3,-4,-3,-4,-4
      !byte -4,-4,-4,-5,-5,-5
      !byte -5,-5,-6,-5,-6,-5
      !byte -6,-6,-5,-6,-5,-6
      !byte -5,-6,-5,-5,-5,-5
      !byte -5,-4,-4,-4,-4,-4
      !byte -3,-4,-3,-2,-3,-2
      !byte -2,-2,-1,-1,-1,-1
      !byte 0,0,0,0,0,1
      !byte 1,1,1,1,1,2
      !byte 2,1,2,2,2,2
      !byte 1,2,2,2,1,2
      !byte 2,1,2,1,1,1
      !byte 1,0,1,0,1,0
      !byte 0,-1,0,-1,0,-1
      !byte -1,-1,-1,-2,-1,-2
      !byte -2,-1,-2,-2,-2,-1
      !byte -2,-2,-2,-2,-1,-2
      !byte -2,-1,-1,-1,-1,-1
      !byte -1,0,0,0,0,0
      !byte 1,1,1,1,2,2
      !byte 2,3,2,3,4,3
      !byte 4,4,4,4,4,5
      !byte 5,5,5,5,6,5
      !byte 6,5,6,6
```
base/sprite_x-coordinate_calculus.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
;Calc new sprite 0 X-coordinate by delta table
        ;by The_WOZ/soft154i

        ; XDELTA = delta table for X
        ; y register = XDELTA index
	clc
	clv
	lda	$D000           ;Load first operand: sprite0 x-coordinate
	bmi	.pxa0           ;Test sign of first operand
	adc	XDELTA,y	;First operand is positive (in 2's complement)
	sta	$D000
	bpl	.cnt
	bvs	.cnt
	lda	#$fe		;Reset MSB
	and	$D010
	jmp	.pxm0
.pxa0
	adc	XDELTA,y	;First operand is negative
	sta	$D000
	bvs	.cnt
	bcc	.cnt
	bmi	.cnt
	lda	#$01		;Set MSB
	ora	$D010
.pxm0	sta	$D010

.cnt    ;--- Rest of the program ---

; X Delta table, ACME format
XDELTA !byte 5,6,5,6,5,6
      !byte 5,5,5,5,5,4
      !byte 4,4,4,4,3,4
      !byte 3,2,3,2,2,2
      !byte 1,1,1,1,0,0
      !byte 0,0,0,-1,-1,-1
      !byte -1,-1,-1,-2,-2,-1
      !byte -2,-2,-2,-2,-1,-2
      !byte -2,-2,-1,-2,-2,-1
      !byte -2,-1,-1,-1,-1,0
      !byte -1,0,-1,0,0,1
      !byte 0,1,0,1,1,1
      !byte 1,2,1,2,2,1
      !byte 2,2,2,1,2,2
      !byte 2,2,1,2,2,1
      !byte 1,1,1,1,1,0
      !byte 0,0,0,0,-1,-1
      !byte -1,-1,-2,-2,-2,-3
      !byte -2,-3,-4,-3,-4,-4
      !byte -4,-4,-4,-5,-5,-5
      !byte -5,-5,-6,-5,-6,-5
      !byte -6,-6,-5,-6,-5,-6
      !byte -5,-6,-5,-5,-5,-5
      !byte -5,-4,-4,-4,-4,-4
      !byte -3,-4,-3,-2,-3,-2
      !byte -2,-2,-1,-1,-1,-1
      !byte 0,0,0,0,0,1
      !byte 1,1,1,1,1,2
      !byte 2,1,2,2,2,2
      !byte 1,2,2,2,1,2
      !byte 2,1,2,1,1,1
      !byte 1,0,1,0,1,0
      !byte 0,-1,0,-1,0,-1
      !byte -1,-1,-1,-2,-1,-2
      !byte -2,-1,-2,-2,-2,-1
      !byte -2,-2,-2,-2,-1,-2
      !byte -2,-1,-1,-1,-1,-1
      !byte -1,0,0,0,0,0
      !byte 1,1,1,1,2,2
      !byte 2,3,2,3,4,3
      !byte 4,4,4,4,4,5
      !byte 5,5,5,5,6,5
      !byte 6,5,6,6
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asprite_x-coordinate_calculus](https://codebase.c64.org/doku.php?id=base%3Asprite_x-coordinate_calculus)*
