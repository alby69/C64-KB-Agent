---
id: src-fast-8bit-multiplication-16bit-product
type: source
title: 'Source Summary: base:fast_8bit_multiplication_16bit_product [Codebase64 wiki]'
aliases:
- base:fast_8bit_multiplication_16bit_product [Codebase64 wiki]
- fast_8bit_multiplication_16bit_product.md
tags:
- assembly
- memory management
sources:
- path: data/docs/codebase_c64_org/base/fast_8bit_multiplication_16bit_product.md
  sha256: 6fc0544eb5a857e9b7819c3fd9dc12b932114136dffcb7aca236a780800ba1bc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:fast_8bit_multiplication_16bit_product [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/fast_8bit_multiplication_16bit_product.md`
**SHA256**: `6fc0544eb5a857e9b7819c3fd9dc12b932114136dffcb7aca236a780800ba1bc`

## Summary



# base:fast_8bit_multiplication_16bit_product [Codebase64 wiki]

base:fast_8bit_multiplication_16bit_product

                ```
;------- MULTIPLY ----------------------
;8x8bits -> 16 bits, signed input and output
;x*y -> y(hi) & x(lo)
;
;warning: there are quite a few undeclared
;zero page addresses used by the mulgen subroutine
;
;the routine is based on this equation:
;
; a*b = ((a+b)/2)^2-((a-b)/2)^2
;
;Oswald/Resource
XTMP     = $e0  ;temporary for X reg
RL       = $e1  ;result lo
RH   ...
