---
id: src-advanced-optimizing
type: source
title: 'Source Summary: Advanced optimizing'
aliases:
- Advanced optimizing
- advanced_optimizing.md
tags:
- sprite programming
- basic
- graphics
- assembly
- raster interrupts
- memory management
sources:
- path: data/docs/codebase_c64_org/base/advanced_optimizing.md
  sha256: eb6e6ea1014485f8acda4671ba44633a45dbb851cbeef1cdd2bc673e199508dc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Advanced optimizing

**Raw Source File**: `data/docs/codebase_c64_org/base/advanced_optimizing.md`
**SHA256**: `eb6e6ea1014485f8acda4671ba44633a45dbb851cbeef1cdd2bc673e199508dc`

## Summary




# Advanced optimizing

# Advanced optimizing

In addition to the tutorials about speedcode and its generation I want to show some other possibilities to save some cycles and thus speed up your code. Therefore I try to give you some triggers on common situations. Feel free to add many more examples.

# Branches and conditional code blocks

Branches take 2 cycles if not taken, and 3 cycles if taken. Having this in mind, we can quickly save one cycle by choosing our branch wisely.

```
        ....
