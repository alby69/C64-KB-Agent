---
id: src-24bit-multiplication-24bit-product
type: source
title: 'Source Summary: 24 bit multiplication (signed or unsigned)'
aliases:
- 24 bit multiplication (signed or unsigned)
- 24bit_multiplication_24bit_product.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/24bit_multiplication_24bit_product.md
  sha256: 9bb701947fb9ecf170ae293052dae91f947b778d187dac10187aec0c11e85ba5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 24 bit multiplication (signed or unsigned)

**Raw Source File**: `data/docs/codebase_c64_org/base/24bit_multiplication_24bit_product.md`
**SHA256**: `9bb701947fb9ecf170ae293052dae91f947b778d187dac10187aec0c11e85ba5`

## Summary



# 24 bit multiplication (signed or unsigned)

base:24bit_multiplication_24bit_product

                # 24 bit multiplication (signed or unsigned)

```
 	; Signed or unsigned 24-bit multiply (24-bit product) 	
	; by Neils
	; DASM format
	PROCESSOR 6502
	
factor1	EQU $61
factor2 EQU $64
product	EQU $67
	MAC twoscomplement
	lda {1}+2
	eor #$ff
	sta {1}+2
	lda {1}+1
	eor #$ff
	sta {1}+1
	lda {1}
	eor #$ff
	clc
	adc #$01
	sta {1}
	ENDM
	; An example program that multiplies -981 by 1340
	; Benchma...
