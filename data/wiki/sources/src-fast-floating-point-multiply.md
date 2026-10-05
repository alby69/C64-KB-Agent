---
id: src-fast-floating-point-multiply
type: source
title: 'Source Summary: Fast Floating Point Multiply'
aliases:
- Fast Floating Point Multiply
- fast_floating_point_multiply.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/fast_floating_point_multiply.md
  sha256: 1a32f471ca69a620e7b5d5f27d40255c19490ad2a1684689ddb9441585c51385
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Fast Floating Point Multiply

**Raw Source File**: `data/docs/codebase_c64_org/base/fast_floating_point_multiply.md`
**SHA256**: `1a32f471ca69a620e7b5d5f27d40255c19490ad2a1684689ddb9441585c51385`

## Summary



# Fast Floating Point Multiply

base:fast_floating_point_multiply

                # Fast Floating Point Multiply

This code uses the fast multiplication [found here](https://codebase.c64.org/doku.php?id=base:seriously_fast_multiplication) to quickly multiply the mantissas. Each multiplication is added to the product as you go.

In the procedure shown below, the red indicates where the two bytes have been added to the partial product, and the orange is where a carry has propagated.

![](https:...
