---
id: src-8bit-multiplication-16bit-product
type: source
title: 'Source Summary: 8bit * 8bit = 16bit multiply'
aliases:
- 8bit * 8bit = 16bit multiply
- 8bit_multiplication_16bit_product.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/8bit_multiplication_16bit_product.md
  sha256: d6f4db16e9d65567e7bc4511df644f30c3c4faf0832c6f6ec66eca57d020826a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 8bit * 8bit = 16bit multiply

**Raw Source File**: `data/docs/codebase_c64_org/base/8bit_multiplication_16bit_product.md`
**SHA256**: `d6f4db16e9d65567e7bc4511df644f30c3c4faf0832c6f6ec66eca57d020826a`

## Summary



# 8bit * 8bit = 16bit multiply

base:8bit_multiplication_16bit_product

                # 8bit * 8bit = 16bit multiply

Extended from [here](https://codebase.c64.org/doku.php?id=base:8bit_multiplication_8bit_product)

;------------------------
; 8bit * 8bit = 16bit multiply
; By White Flame
; Multiplies "num1" by "num2" and stores result in .A (low byte, also in .X) and .Y (high byte)
; uses extra zp var "num1Hi"
; .X and .Y get clobbered.  Change the tax/txa and tay/tya to stack or zp storage...
