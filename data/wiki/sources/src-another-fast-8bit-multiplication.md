---
id: src-another-fast-8bit-multiplication
type: source
title: 'Source Summary: Fast 8bit * 8bit = 16bit multiply'
aliases:
- Fast 8bit * 8bit = 16bit multiply
- another_fast_8bit_multiplication.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/another_fast_8bit_multiplication.md
  sha256: a5e02688b9001d2004535dac04fa3366590ae911596e1c73f0903ef514135f4e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Fast 8bit * 8bit = 16bit multiply

**Raw Source File**: `data/docs/codebase_c64_org/base/another_fast_8bit_multiplication.md`
**SHA256**: `a5e02688b9001d2004535dac04fa3366590ae911596e1c73f0903ef514135f4e`

## Summary



# Fast 8bit * 8bit = 16bit multiply

base:another_fast_8bit_multiplication

                # Fast 8bit * 8bit = 16bit multiply

```
; Fast 8bit * 8bit = 16bit multiply with 512 bytes tables
; Multiplies AC by "fac" and returns result in .A (high) and "rlo" (low)
; by litwr (aka Vladimir Lidovski)with help of Urusergi 20151023
;it uses formula
;  x*y = ((x+y)/2)^2 - ((x-y)/2)^2, if x+y is even
;      = ((x+y-1)/2)^2 - ((x-y-1)/2)^2 + y, if x+y is odd and x>=y
; Input variables:
;   AC (multipl...
