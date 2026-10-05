---
id: src-small-fast-8-bit-prng
type: source
title: 'Source Summary: An tiny, fast, 8-bit pseudo-random number generator in 6502
  assembly'
aliases:
- An tiny, fast, 8-bit pseudo-random number generator in 6502 assembly
- small_fast_8-bit_prng.md
tags:
- assembly
- memory management
sources:
- path: data/docs/codebase_c64_org/base/small_fast_8-bit_prng.md
  sha256: ebab63086e74255535b7501e552384aed558fce94932c5f3c7d839e557c2bedd
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: An tiny, fast, 8-bit pseudo-random number generator in 6502 assembly

**Raw Source File**: `data/docs/codebase_c64_org/base/small_fast_8-bit_prng.md`
**SHA256**: `ebab63086e74255535b7501e552384aed558fce94932c5f3c7d839e557c2bedd`

## Summary



# An tiny, fast, 8-bit pseudo-random number generator in 6502 assembly

# An tiny, fast, 8-bit pseudo-random number generator in 6502 assembly

by White Flame

(Thanks to bogax for pointing out the $80→$00 link)

*This is my re-discovery of the well-known [Linear feedback shift register](http://en.wikipedia.org/wiki/Linear_feedback_shift_register) type of PRNG, having seen a bit of its implementation elsewhere.*

This simple routine is based on this mutation of a number:

```
        lda seed
...
