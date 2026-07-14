---
title: 16-bit multiply with 32-bit product
source_url: https://codebase.c64.org/doku.php?id=base%3A16bit_multiplication_32-bit_product
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware:
- KERNAL
- CPU
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
---

# 16-bit multiply with 32-bit product

base:16bit_multiplication_32-bit_product

                # 16-bit multiply with 32-bit product

;16-bit multiply with 32-bit product ;took from 6502.org multiplier = $f7 multiplicand = $f9 product = $fb mult16 lda #$00 sta product+2 ; clear upper bits of product sta product+3 ldx #$10 ; set binary count to 16 shift_r lsr multiplier+1 ; divide multiplier by 2 ror multiplier bcc rotate_r lda product+2 ; get upper half of product and add multiplicand clc adc multiplicand sta product+2 lda product+3 adc multiplicand+1 rotate_r ror ; rotate partial product sta product+3 ror product+2 ror product+1 ror product dex bne shift_r rts

base/16bit_multiplication_32-bit_product.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: DASM)

#### Routine Identificate:
- **`mult16`** (unknown): No description available
- **`shift_r`** (unknown): No description available
- **`rotate_r`** (unknown): No description available

```assembly
;16-bit multiply with 32-bit product 
;took from 6502.org
 
multiplier	= $f7 
multiplicand	= $f9 
product		= $fb 
 
mult16 		lda	#$00
		sta	product+2	; clear upper bits of product
		sta	product+3 
		ldx	#$10		; set binary count to 16 
shift_r		lsr	multiplier+1	; divide multiplier by 2 
		ror	multiplier
		bcc	rotate_r 
		lda	product+2	; get upper half of product and add multiplicand
		clc
		adc	multiplicand
		sta	product+2
		lda	product+3 
		adc	multiplicand+1
rotate_r	ror			; rotate partial product 
		sta	product+3 
		ror	product+2
		ror	product+1 
		ror	product 
		dex
		bne	shift_r 
		rts
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3A16bit_multiplication_32-bit_product](https://codebase.c64.org/doku.php?id=base%3A16bit_multiplication_32-bit_product)*
