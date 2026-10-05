---
id: src-improved-clockslide
type: source
title: 'Source Summary: Improved Clock Slide'
aliases:
- Improved Clock Slide
- improved_clockslide.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/improved_clockslide.md
  sha256: 2adeadeaf3c595afa28fef23c22b31c91478baa95c06a6ab5be8b5c8193ade83
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Improved Clock Slide

**Raw Source File**: `data/docs/codebase_c64_org/base/improved_clockslide.md`
**SHA256**: `2adeadeaf3c595afa28fef23c22b31c91478baa95c06a6ab5be8b5c8193ade83`

## Summary



# Improved Clock Slide

# Improved Clock Slide

by **lft**

Sometimes we want to delay a variable number of cycles, e.g. during VSP or when setting up a stable raster.

A typical way of handling a variable delay is to use a *clock slide*. In the following example, we start somewhere in a given range of cycles, we want to end up exactly at cycle 50, and we've computed the corresponding number of cycles to skip in A.

```
         ; delay 19-A cycles
         sta     branch+1    ; 31..41 (A in r...
