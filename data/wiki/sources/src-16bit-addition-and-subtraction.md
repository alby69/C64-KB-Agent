---
id: src-16bit-addition-and-subtraction
type: source
title: 'Source Summary: base:16bit_addition_and_subtraction [Codebase64 wiki]'
aliases:
- base:16bit_addition_and_subtraction [Codebase64 wiki]
- 16bit_addition_and_subtraction.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/16bit_addition_and_subtraction.md
  sha256: 0e0ded942f9c9f1facf29cd4a8cc1e1bc76431bb39e8fdc75bcf7aa3f6e9a114
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:16bit_addition_and_subtraction [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/16bit_addition_and_subtraction.md`
**SHA256**: `0e0ded942f9c9f1facf29cd4a8cc1e1bc76431bb39e8fdc75bcf7aa3f6e9a114`

## Summary



# base:16bit_addition_and_subtraction [Codebase64 wiki]

base:16bit_addition_and_subtraction

                ### 16-bit addition and subtraction

16-bit basic arithmetic is very easy. Using the carry flag, you can simply chain 8-bit operations to perform this simple task on longer integers. Starting from the least signifant byte, work your way up to the MSB. The routine is the same for adding and subtracting, except for the fact that when adding, the carry flag is initially cleared and for su...
