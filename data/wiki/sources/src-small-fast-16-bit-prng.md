---
id: src-small-fast-16-bit-prng
type: source
title: 'Source Summary: base:small_fast_16-bit_prng [Codebase64 wiki]'
aliases:
- base:small_fast_16-bit_prng [Codebase64 wiki]
- small_fast_16-bit_prng.md
tags:
- assembly
- memory management
sources:
- path: data/docs/codebase_c64_org/base/small_fast_16-bit_prng.md
  sha256: ed8b47f819f1241f99243a3c9095e1e5097a6c8bd5fcef7157677b53beb91edf
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:small_fast_16-bit_prng [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/small_fast_16-bit_prng.md`
**SHA256**: `ed8b47f819f1241f99243a3c9095e1e5097a6c8bd5fcef7157677b53beb91edf`

## Summary



# base:small_fast_16-bit_prng [Codebase64 wiki]

base:small_fast_16-bit_prng

                #### 16-bit PRNG

by White Flame

See [Small, fast 8-bit PRNG](https://codebase.c64.org/doku.php?id=base:small_fast_8-bit_prng) for details of the algorithm.  This should randomly iterate over a full 0000-ffff range, instead of the 0001-ffff range that the more common Galois LFSR covers.

Code is not well tested, though.

 lda seed
 beq lowZero ; $0000 and $8000 are special values to test for
 
 ; Do ...
