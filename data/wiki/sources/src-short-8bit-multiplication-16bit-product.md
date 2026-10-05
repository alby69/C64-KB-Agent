---
id: src-short-8bit-multiplication-16bit-product
type: source
title: 'Source Summary: Short 8bit * 8bit = 16bit multiply'
aliases:
- Short 8bit * 8bit = 16bit multiply
- short_8bit_multiplication_16bit_product.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/short_8bit_multiplication_16bit_product.md
  sha256: b60d3a1ac55437de06ceb1512f662ba833a40ed6220eb5cc710b7e532c36d8bc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Short 8bit * 8bit = 16bit multiply

**Raw Source File**: `data/docs/codebase_c64_org/base/short_8bit_multiplication_16bit_product.md`
**SHA256**: `b60d3a1ac55437de06ceb1512f662ba833a40ed6220eb5cc710b7e532c36d8bc`

## Summary



# Short 8bit * 8bit = 16bit multiply

base:short_8bit_multiplication_16bit_product

                # Short 8bit * 8bit = 16bit multiply

A small multiplication routine using the ancient egyptian multiplication algorithm. Factors should be stored in the FAC1 and FAC2 variables, the product can be found in Akku (high byte) and the X-Register (low byte). FAC1 will be destroyed. No tables required.

```
FAC1     = $58
FAC2     = $59
        ; A*256 + X = FAC1 * FAC2
MUL8
        lda #$00
        ...
