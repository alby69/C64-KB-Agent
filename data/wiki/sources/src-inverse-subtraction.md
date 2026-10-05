---
id: src-inverse-subtraction
type: source
title: 'Source Summary: Inverse Subtraction'
aliases:
- Inverse Subtraction
- inverse_subtraction.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/inverse_subtraction.md
  sha256: 1efac9c9d69846949cb5de5bb054fe02a7db0d5657f0e224f34863cd39d51bc0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Inverse Subtraction

**Raw Source File**: `data/docs/codebase_c64_org/base/inverse_subtraction.md`
**SHA256**: `1efac9c9d69846949cb5de5bb054fe02a7db0d5657f0e224f34863cd39d51bc0`

## Summary



# Inverse Subtraction

# Inverse Subtraction

by White Flame

To subtract A from a number, or “number - .A”, we transform it to the doable “-.A + number”:

 eor #$ff
 sec
 adc number

and that's it.

## Further elaboration

by Frantic

One may think that the following two pieces of code would produce exactly the same result:

  ;Variant 1 - Subtract XX by YY using clc/adc
  lda #XX
  clc
  adc #YY  ;E.g. to subtract with 1, use $ff here

  ;Variant 2 - Subtract $XX by $YY using sec/adc
  lda #...
