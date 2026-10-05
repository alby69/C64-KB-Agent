---
id: src-24bit-division-24-bit-result
type: source
title: 'Source Summary: base:24bit_division_24-bit_result [Codebase64 wiki]'
aliases:
- base:24bit_division_24-bit_result [Codebase64 wiki]
- 24bit_division_24-bit_result.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/24bit_division_24-bit_result.md
  sha256: f5d6738f8c786c60759c72e3b6b10e77c32383bdcf96d410efcc66ed85fa7ec6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:24bit_division_24-bit_result [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/24bit_division_24-bit_result.md`
**SHA256**: `f5d6738f8c786c60759c72e3b6b10e77c32383bdcf96d410efcc66ed85fa7ec6`

## Summary



# base:24bit_division_24-bit_result [Codebase64 wiki]

base:24bit_division_24-bit_result

                It's just an enlarged version of the 16-bit division. There's not enough unused page-zero locations on a C64 to have all the variables in page-zero. The remainder variable is in page-zero because is the most used.

; Executes an unsigned integer division of a 24-bit dividend by a 24-bit divisor
; the result goes to dividend and remainder variables
;
; Verz!!! 18-mar-2017
div24	lda #0	     ...
