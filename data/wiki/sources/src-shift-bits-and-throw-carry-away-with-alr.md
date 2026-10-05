---
id: src-shift-bits-and-throw-carry-away-with-alr
type: source
title: 'Source Summary: Shift bits and throw carry away with ALR'
aliases:
- Shift bits and throw carry away with ALR
- shift_bits_and_throw_carry_away_with_alr.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/shift_bits_and_throw_carry_away_with_alr.md
  sha256: 266570fbac66b375fb72649c83bcabd9879b57b028afeff954ad637b5a09998c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Shift bits and throw carry away with ALR

**Raw Source File**: `data/docs/codebase_c64_org/base/shift_bits_and_throw_carry_away_with_alr.md`
**SHA256**: `266570fbac66b375fb72649c83bcabd9879b57b028afeff954ad637b5a09998c`

## Summary



# Shift bits and throw carry away with ALR

base:shift_bits_and_throw_carry_away_with_alr

                # Shift bits and throw carry away with ALR

In many cases when you shift/roll a byte to the right with LSR, you don't need the bits that are rolled out. So if you're planning on doing an ADC afterwards, you need a CLC inbetween.

lsr
clc
adc #$47

But with ALR you can AND the A register before it's shifted. So if you choose $fe (%11111110) as the AND mask, you set the bit that is rolled o...
