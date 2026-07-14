---
title: 16-bit Division
source_url: https://codebase.c64.org/doku.php?id=base%3A16bit_division_16-bit_result
category: reference
topics:
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
---

# 16-bit Division

base:16bit_division_16-bit_result

                # 16-bit Division

To make the most common integer multiplication/division routines complete:

divisor = $58 ;$59 used for hi-byte dividend = $fb ;$fc used for hi-byte remainder = $fd ;$fe used for hi-byte result = dividend ;save memory by reusing divident to store the result divide lda #0 ;preset remainder to 0 sta remainder sta remainder+1 ldx #16 ;repeat for each bit: ... divloop asl dividend ;dividend lb & hb*2, msb -> Carry rol dividend+1 rol remainder ;remainder lb & hb * 2 + msb from carry rol remainder+1 lda remainder sec sbc divisor ;substract divisor to see if it fits in tay ;lb result -> Y, for we may need it later lda remainder+1 sbc divisor+1 bcc skip ;if carry=0 then divisor didn't fit in yet sta remainder+1 ;else save substraction result as new remainder, sty remainder inc result ;and INCrement result cause divisor fit in 1 times skip dex bne divloop rts

Variations of the above routine have been published in several C=64 mags. In terms of speed AND memory usage it should be the optimum.

base/16bit_division_16-bit_result.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
divisor = $58     ;$59 used for hi-byte
dividend = $fb	  ;$fc used for hi-byte
remainder = $fd	  ;$fe used for hi-byte
result = dividend ;save memory by reusing divident to store the result

divide	lda #0	        ;preset remainder to 0
	sta remainder
	sta remainder+1
	ldx #16	        ;repeat for each bit: ...

divloop	asl dividend	;dividend lb & hb*2, msb -> Carry
	rol dividend+1	
	rol remainder	;remainder lb & hb * 2 + msb from carry
	rol remainder+1
	lda remainder
	sec
	sbc divisor	;substract divisor to see if it fits in
	tay	        ;lb result -> Y, for we may need it later
	lda remainder+1
	sbc divisor+1
	bcc skip	;if carry=0 then divisor didn't fit in yet

	sta remainder+1	;else save substraction result as new remainder,
	sty remainder	
	inc result	;and INCrement result cause divisor fit in 1 times

skip	dex
	bne divloop	
	rts
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3A16bit_division_16-bit_result](https://codebase.c64.org/doku.php?id=base%3A16bit_division_16-bit_result)*
