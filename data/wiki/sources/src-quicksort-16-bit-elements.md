---
id: src-quicksort-16-bit-elements
type: source
title: 'Source Summary: Quicksort (for 16-bit Elements)'
aliases:
- Quicksort (for 16-bit Elements)
- quicksort_16-bit_elements.md
tags:
- assembly
- basic
- sound generation
- memory management
sources:
- path: data/docs/codebase_c64_org/base/quicksort_16-bit_elements.md
  sha256: bbf530d0878c92d0ccf77454476a469b425aa051a0a523c6a5cad8617ec9fb1d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Quicksort (for 16-bit Elements)

**Raw Source File**: `data/docs/codebase_c64_org/base/quicksort_16-bit_elements.md`
**SHA256**: `bbf530d0878c92d0ccf77454476a469b425aa051a0a523c6a5cad8617ec9fb1d`

## Summary



# Quicksort (for 16-bit Elements)

# Quicksort (for 16-bit Elements)

by Vladimir Lidovski aka litwr, 13 Aug 2016 (with help of BigEd)

It is well known that the best, the fastest sort routine is Quicksort. It is very odd that its implementations for 6502 for all of 42 years (from 1975 to 2016) have a bit blurred and unofficial status. The main problem is in the stack depending nature of Quicksort and the stack limit of 256 bytes of 6502 architecture. It is solvable.

The next Pascal code was ...
