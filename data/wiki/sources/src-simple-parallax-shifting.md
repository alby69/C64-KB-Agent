---
id: src-simple-parallax-shifting
type: source
title: 'Source Summary: Simple parallax shifting'
aliases:
- Simple parallax shifting
- simple_parallax_shifting.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/simple_parallax_shifting.md
  sha256: 8a298f7b57255a9e8726a77adeaa978c3301332d4563101608cd675217279479
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Simple parallax shifting

**Raw Source File**: `data/docs/codebase_c64_org/base/simple_parallax_shifting.md`
**SHA256**: `8a298f7b57255a9e8726a77adeaa978c3301332d4563101608cd675217279479`

## Summary




# Simple parallax shifting

### Table of Contents

# Simple parallax shifting

by Achim

A parallax effect can be achieved by shifting bits and bytes of one char or a pattern of chars, e. g. 2×2 tiles, corresponding to the soft scroll registers ($d016 & $d011).

![](https://codebase.c64.org/lib/exe/fetch.php?media=base:parallax.gif)


This effect can be seen in numerous games (e.g. Bounder, Parallax, Marauder etc.). Here's a small example for a 2×2 tile, hires.

Example 2×2 tile with chars A,...
