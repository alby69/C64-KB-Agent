---
title: 8bit log table generator
source_url: https://codebase.c64.org/doku.php?id=base%3A8bit_logarithm_table_generator_routine
category: reference
topics:
- basic
- assembly
difficulty: intermediate
language: assembly
hardware: []
related: []
scraped_at: '2026-07-14'
---

# 8bit log table generator

# 8bit log table generator

Logarithm tables are often used in C64 and for much the same reason they were originally invented, that is exploiting the same identities your old slide rule uses for transforming multiplication and division into addition and subtraction:

lg(x*y) = lg(x) + lg(y) lg(x/y) = lg(x) - lg(y)

Typically they'd be used together with an exponentiation table (to get the approximate result), with the exponent built-in to another table (such as in my atan routine), or on their own for comparison purposes (as for dot products and the like.)

Yet they're also poorly compressible so a generator routine comes in handy. This version is an eight-bit implementation of the classic shift-add algorithm where you repeatedly try to factorize (x²-1)/x² factors out of a normalized number, with the factors' logarithms stored in a pre-calculated table. An alternative would be to use BASIC to get a much smaller, more precise, and frustratingly slow generator. But this seems like a fair tradeoff between size, speed and precision (saving some 145 bytes or so after compression.)

Note that the result is scaled to fit in eight-bits. This can most naturally be viewed a base-two logarithm in 3:5 fixed-point.

table = $c000 ;page aligned seed .byte $00,$00 .byte $02,$05 .byte $0c,$1f reduce pla adc seed,y sec next pha ldy #5 txa sta shift+4 shift ror shift+4 sbx #$00 bcs reduce tax dey bpl shift pla store sbc #$1f sta table lsr store+3 bcc store enter dec *+4 lda #$00 sta store+3 asl a tax lda #$00 bcs next ; sta table ;do whatever makes most sense for log(0) rts

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
lg(x*y) = lg(x) + lg(y)
lg(x/y) = lg(x) - lg(y)
```

### Snippet Codice (BASIC)

```basic
table	= $c000		;page aligned

seed	.byte $00,$00
	.byte $02,$05
	.byte $0c,$1f

reduce	pla
	adc seed,y
	sec
next	pha
	ldy #5
	txa
	sta shift+4

shift	ror shift+4
	sbx #$00
	bcs reduce
	tax
	dey
	bpl shift

	pla
store	sbc #$1f
	sta table
	lsr store+3
	bcc store

enter	dec *+4
	lda #$00
	sta store+3
	asl a
	tax
	lda #$00
	bcs next

;	sta table	;do whatever makes most sense for log(0)
	rts
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3A8bit_logarithm_table_generator_routine](https://codebase.c64.org/doku.php?id=base%3A8bit_logarithm_table_generator_routine)*
