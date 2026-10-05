---
id: src-8bit-multiplication-16bit-product-fast-no-tables
type: source
title: 'Source Summary: 8bit multiplication with 16bit product'
aliases:
- 8bit multiplication with 16bit product
- 8bit_multiplication_16bit_product_fast_no_tables.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/8bit_multiplication_16bit_product_fast_no_tables.md
  sha256: 6908b89f73659f59c137c58e9dbafdc896c8f93343c50a989fd4bd649d38dfec
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 8bit multiplication with 16bit product

**Raw Source File**: `data/docs/codebase_c64_org/base/8bit_multiplication_16bit_product_fast_no_tables.md`
**SHA256**: `6908b89f73659f59c137c58e9dbafdc896c8f93343c50a989fd4bd649d38dfec`

## Summary



# 8bit multiplication with 16bit product

base:8bit_multiplication_16bit_product_fast_no_tables

                # 8bit multiplication with 16bit product

This code aims to be fast, without using tables.

```
; mul 8x8 16 bit result for when you can't afford big tables
; by djmips 
;
; inputs are mul1 and X.  mul1 and mul2 should be zp locations
; A should be zero entering but if you want it will factor in as 1/2 A added to the result.
;
; output is 16 bit in A : mul1   (A is high byte)
;
; le...
