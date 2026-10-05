---
id: src-optimal-sort-16-bit-elements
type: source
title: 'Source Summary: Optimal Sort for any number of 16-bit elements'
aliases:
- Optimal Sort for any number of 16-bit elements
- optimal_sort_16-bit_elements.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/optimal_sort_16-bit_elements.md
  sha256: 48c5cad91517d741a63268de3e763f93f1f76e120cf5ed116245ea5a061e6fa4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Optimal Sort for any number of 16-bit elements

**Raw Source File**: `data/docs/codebase_c64_org/base/optimal_sort_16-bit_elements.md`
**SHA256**: `48c5cad91517d741a63268de3e763f93f1f76e120cf5ed116245ea5a061e6fa4`

## Summary



# Optimal Sort for any number of 16-bit elements

# Optimal Sort for any number of 16-bit elements

by Mats Rosengren

# General Discussion

The extension of the “[Optimal Sort](https://codebase.c64.org/doku.php?id=base:optimal_sort_8-bit_elements)” algorithm to “an unlimited number” (i.e. more then 255 elements) of 16 bit elements is straightforward using standard 6502 technique.

Consider first the loop using the Y register to sequentially access the elements starting with the second last an...
