---
id: src-8bit-multiplication-8bit-product
type: source
title: 'Source Summary: General 8bit * 8bit = 8bit multiply'
aliases:
- General 8bit * 8bit = 8bit multiply
- 8bit_multiplication_8bit_product.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/8bit_multiplication_8bit_product.md
  sha256: 951524c9ea56dca37a6ebea17de107d8b7238ed091a1d975a4ac9c29bd937429
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: General 8bit * 8bit = 8bit multiply

**Raw Source File**: `data/docs/codebase_c64_org/base/8bit_multiplication_8bit_product.md`
**SHA256**: `951524c9ea56dca37a6ebea17de107d8b7238ed091a1d975a4ac9c29bd937429`

## Summary



# General 8bit * 8bit = 8bit multiply

base:8bit_multiplication_8bit_product

                # General 8bit * 8bit = 8bit multiply

; General 8bit * 8bit = 8bit multiply
; by White Flame 20030207
; Multiplies "num1" by "num2" and returns result in .A
; Instead of using a bit counter, this routine early-exits when num2 reaches zero, thus saving iterations.
; Input variables:
;   num1 (multiplicand)
;   num2 (multiplier), should be small for speed
;   Signedness should not matter
; .X and .Y ar...
