---
id: src-a-faster-radix-sort
type: source
title: 'Source Summary: A Faster Radix Sort'
aliases:
- A Faster Radix Sort
- a_faster_radix_sort.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/a_faster_radix_sort.md
  sha256: 5dd90eb5993dbc7b5d88c879dd42e11d5c6adfd0f84686252b9e2b0193a55443
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: A Faster Radix Sort

**Raw Source File**: `data/docs/codebase_c64_org/base/a_faster_radix_sort.md`
**SHA256**: `5dd90eb5993dbc7b5d88c879dd42e11d5c6adfd0f84686252b9e2b0193a55443`

## Summary



# A Faster Radix Sort

### Table of Contents

# A Faster Radix Sort

by lft

This article describes an implementation of *radix sort* optimized for sprite
multiplexers. The input is a set of actors numbered 0 to *N*-1, where each actor
has a Y-position in the range 0–223 stored in an array (called `ypos`) on the
zero-page. The routine will push the *N* actor numbers on the stack, in order of
increasing Y-coordinates.

For a real multiplexer, it is actually preferable to either:

- Push them in...
