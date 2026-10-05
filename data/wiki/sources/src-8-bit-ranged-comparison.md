---
id: src-8-bit-ranged-comparison
type: source
title: 'Source Summary: Range Checking a Byte'
aliases:
- Range Checking a Byte
- 8-bit_ranged_comparison.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/8-bit_ranged_comparison.md
  sha256: c2f7438826be7fbb930bb404627629a6a541cdf1c235879afbd0e49c1af5ee9e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Range Checking a Byte

**Raw Source File**: `data/docs/codebase_c64_org/base/8-bit_ranged_comparison.md`
**SHA256**: `c2f7438826be7fbb930bb404627629a6a541cdf1c235879afbd0e49c1af5ee9e`

## Summary



# Range Checking a Byte

### Table of Contents

# Range Checking a Byte

## Approach by White Flame

In checking for the range [x,y), instead of performing 2 comparisons the idea is to subtract x to align the range to [0,y-x). This then allows us to perform a single unsigned comparison to check both ends of the range.

Any numbers lower than the original range will have wrapped the byte into the high values ⇐255, and any number higher than the original range will still be too large.

; Check ....
