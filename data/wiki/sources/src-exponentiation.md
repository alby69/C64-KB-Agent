---
id: src-exponentiation
type: source
title: 'Source Summary: Exponentiation'
aliases:
- Exponentiation
- exponentiation.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/exponentiation.md
  sha256: bf989a8f6c8f4976f8206007ad75c118e18741e7d798a7034e824ca4e662b229
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Exponentiation

**Raw Source File**: `data/docs/codebase_c64_org/base/exponentiation.md`
**SHA256**: `bf989a8f6c8f4976f8206007ad75c118e18741e7d798a7034e824ca4e662b229`

## Summary



# Exponentiation

# Exponentiation

This routine computes the exponentiation of a 16 bit value. It handles only integer values. The largest result is 2^32-1 (32 bits); that makes 31 the largest possible exponent. Results larger than 2^32-1 will overflow.

The algorithm is recursive and at each iteration breaks the exponentiation in a simpler product: if the exponent is even, it will compute the exponentiation with half the exponent and square it, while if it's odd it will compute the product o...
