---
id: src-signed-8bit-divide-by-2-arithmetic-shift-right
type: source
title: 'Source Summary: Arithmetic shift right'
aliases:
- Arithmetic shift right
- signed_8bit_divide_by_2_arithmetic_shift_right.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/signed_8bit_divide_by_2_arithmetic_shift_right.md
  sha256: ace577d0bd7a0d65fbb6b7d398e848a7edca0bb91ea73adf4c5f494c8996b212
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Arithmetic shift right

**Raw Source File**: `data/docs/codebase_c64_org/base/signed_8bit_divide_by_2_arithmetic_shift_right.md`
**SHA256**: `ace577d0bd7a0d65fbb6b7d398e848a7edca0bb91ea73adf4c5f494c8996b212`

## Summary



# Arithmetic shift right

# Arithmetic shift right

By Bitbreaker

If we want to divide by the power of 2 we usually shift right. That is fine with unsigned numbers, but for signed numbers we would need a arithemtic shift right, that we have no opcode for. So we need a trick to preserve bit 7 in another way:

```
    cmp #$80 ;copy bit 7 to carry (i love that trick also for other situations where A should not be clobbered)
    ror      ;now rotate and we successfully preserved bit 7
```
Easy l...
