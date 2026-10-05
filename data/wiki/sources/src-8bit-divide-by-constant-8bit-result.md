---
id: src-8bit-divide-by-constant-8bit-result
type: source
title: 'Source Summary: 8bit Divide by Constant — 8bit result'
aliases:
- 8bit Divide by Constant — 8bit result
- 8bit_divide_by_constant_8bit_result.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/8bit_divide_by_constant_8bit_result.md
  sha256: e880c55e97dc58d32b5a8c577ce2eab3a678fc103047db8faacf575a3acd2dd3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 8bit Divide by Constant — 8bit result

**Raw Source File**: `data/docs/codebase_c64_org/base/8bit_divide_by_constant_8bit_result.md`
**SHA256**: `e880c55e97dc58d32b5a8c577ce2eab3a678fc103047db8faacf575a3acd2dd3`

## Summary



# 8bit Divide by Constant — 8bit result

base:8bit_divide_by_constant_8bit_result

                # 8bit Divide by Constant — 8bit result

; Unsigned Integer Division Routines (rev 2)
; by Omegamatrix
;
; Rev 1 (June 14, 2014)
; Divide by 6,10,12,20,24,26, and 28 have all been replace with new and better routines.
;
; Rev 2 (June 21, 2014)
; Divide by 22 routines has been upgraded to one that saves 3 cycles, same amount of bytes as before.
;
;
;
; To use these routines begin with unsigned val...
