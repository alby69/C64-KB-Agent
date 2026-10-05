---
id: src-fixed-point-arithmethic
type: source
title: 'Source Summary: Fixed point arithmethic'
aliases:
- Fixed point arithmethic
- fixed_point_arithmethic.md
tags:
- assembly
- memory management
sources:
- path: data/docs/codebase_c64_org/base/fixed_point_arithmethic.md
  sha256: 8e05a7c7fce8e9159a838cf8682f64202a090f742e7c0723b9b9c7b9d93df59b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Fixed point arithmethic

**Raw Source File**: `data/docs/codebase_c64_org/base/fixed_point_arithmethic.md`
**SHA256**: `8e05a7c7fce8e9159a838cf8682f64202a090f742e7c0723b9b9c7b9d93df59b`

## Summary



# Fixed point arithmethic

# Fixed point arithmethic

A fixed-point number representation is a number that has a fixed number of digits before and after the radix point (e.g. “.” in English decimal notation).

In terms of binary numbers, each magnitude bit represents a power of two, while each fractional bit represents an inverse power of two. Thus the first fractional bit is ½, the second is ¼, the third is ⅛ and so on.

8:8 Fixed Point representation is the most straightforward approach (in ...
