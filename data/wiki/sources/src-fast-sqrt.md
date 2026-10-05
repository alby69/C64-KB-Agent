---
id: src-fast-sqrt
type: source
title: 'Source Summary: Square Root calculation'
aliases:
- Square Root calculation
- fast_sqrt.md
tags:
- assembly
- memory management
sources:
- path: data/docs/codebase_c64_org/base/fast_sqrt.md
  sha256: 20cefaac0bc1979572dceb2b42670dccdc32982fc5e8d4a68245b107d553c686
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Square Root calculation

**Raw Source File**: `data/docs/codebase_c64_org/base/fast_sqrt.md`
**SHA256**: `20cefaac0bc1979572dceb2b42670dccdc32982fc5e8d4a68245b107d553c686`

## Summary



# Square Root calculation

# Square Root calculation

Imagine you wanna have a square root:

R = sqrt(N)

That obviously gives you:

R^2 = N

Since we wanna establish a convergent algo, we simply use this during calculation:

R(n)^2 <= N

R(0) will be 0. To get closer to N we add a third value D to R as long as that formula is true. Since we work with binary computers, this D will be of the kind 2^x (128, 64, 32 etc).

Ok assuming we wanna have the root from a 16 bit number and since the outpu...
