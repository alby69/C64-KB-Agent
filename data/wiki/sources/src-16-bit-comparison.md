---
id: src-16-bit-comparison
type: source
title: 'Source Summary: 16-Bit Comparison'
aliases:
- 16-Bit Comparison
- 16-bit_comparison.md
tags:
- assembly
- memory management
sources:
- path: data/docs/codebase_c64_org/base/16-bit_comparison.md
  sha256: a8a910c7ef5ec0ce2d318f42588d5b6da422648e8fb4093a7e6c0dd1ced37ded
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 16-Bit Comparison

**Raw Source File**: `data/docs/codebase_c64_org/base/16-bit_comparison.md`
**SHA256**: `a8a910c7ef5ec0ce2d318f42588d5b6da422648e8fb4093a7e6c0dd1ced37ded`

## Summary



# 16-Bit Comparison

### Table of Contents

# 16-Bit Comparison

One would think that a compare and branch approach would suffice when comparing 16 bit numbers, but this is not the case if you want full compatibility (If you don't care about the NEGATIVE Flag, it is a lot easier). If we consider two U16 numbers (A and M), there are many fringe cases which messes up due to the special handling of the NEGATIVE flag which strictly is set according to BIT15 of the A - M subtraction result.

For ex...
