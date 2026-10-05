---
id: src-16-bit-absolute-comparison
type: source
title: 'Source Summary: 16-Bit Absolute Value Comparison'
aliases:
- 16-Bit Absolute Value Comparison
- 16-bit_absolute_comparison.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/16-bit_absolute_comparison.md
  sha256: ba6ed686feb6be0873a08a744f2724c5d5cc2652185114c65cd3428e40791a79
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 16-Bit Absolute Value Comparison

**Raw Source File**: `data/docs/codebase_c64_org/base/16-bit_absolute_comparison.md`
**SHA256**: `ba6ed686feb6be0873a08a744f2724c5d5cc2652185114c65cd3428e40791a79`

## Summary



# 16-Bit Absolute Value Comparison

base:16-bit_absolute_comparison

                # 16-Bit Absolute Value Comparison

## Skate & Eins Method

N1 = 16-bit signed number at zeropage

N2 = 16-bit signed number at zeropage

Here we compare;

|N1| and |N2|

in other representation

abs(N1) and abs(N2)

So, if N1 = 2000, N2 = -3000, N2 should be bigger since we compare the distance from zero.

Please note that equality is neglected here. Equal absolute values may end up in any of the two conditio...
