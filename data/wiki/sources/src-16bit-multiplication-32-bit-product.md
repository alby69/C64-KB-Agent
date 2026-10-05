---
id: src-16bit-multiplication-32-bit-product
type: source
title: 'Source Summary: 16-bit multiply with 32-bit product'
aliases:
- 16-bit multiply with 32-bit product
- 16bit_multiplication_32-bit_product.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/16bit_multiplication_32-bit_product.md
  sha256: 0b5163fc9cc8b20418ea0e8ba6d8ea186356daa49db06236875a489a62cd4050
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 16-bit multiply with 32-bit product

**Raw Source File**: `data/docs/codebase_c64_org/base/16bit_multiplication_32-bit_product.md`
**SHA256**: `0b5163fc9cc8b20418ea0e8ba6d8ea186356daa49db06236875a489a62cd4050`

## Summary



# 16-bit multiply with 32-bit product

base:16bit_multiplication_32-bit_product

                # 16-bit multiply with 32-bit product

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
		lda	product+2	; get upper half of produc...
