---
id: src-static-starfield
type: source
title: 'Source Summary: Static Starfield'
aliases:
- Static Starfield
- static_starfield.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/static_starfield.md
  sha256: 8a141be2df77ac52fe7031572b47fd9aa5a2d2164e79e871b39c6a6b622813f8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Static Starfield

**Raw Source File**: `data/docs/codebase_c64_org/base/static_starfield.md`
**SHA256**: `8a141be2df77ac52fe7031572b47fd9aa5a2d2164e79e871b39c6a6b622813f8`

## Summary




# Static Starfield

### Table of Contents

# Static Starfield

by Achim

Locus classicus for this effect is Uridium: Fast scrolling graphics with fixed stars in the background. This kind of parallax shifting is simple but effective. Here's a small tutorial for a sidescrolling game using two screen buffers.

Only two steps necessary to achieve this effect:

1. Manipulate one char corresponding to the soft scroll registers in $d016
2. Check wether this char can be printed on its screen position...
