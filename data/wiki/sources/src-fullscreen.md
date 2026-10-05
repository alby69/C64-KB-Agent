---
id: src-fullscreen
type: source
title: 'Source Summary: base:fullscreen [Codebase64 wiki]'
aliases:
- base:fullscreen [Codebase64 wiki]
- fullscreen.md
tags:
- sprite programming
- graphics
- assembly
sources:
- path: data/docs/codebase_c64_org/base/fullscreen.md
  sha256: 0c8fa084c6fbe41e70e3cd2a361e36e8b559bb286b3208e9729bfdcde67fea8b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:fullscreen [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/fullscreen.md`
**SHA256**: `0c8fa084c6fbe41e70e3cd2a361e36e8b559bb286b3208e9729bfdcde67fea8b`

## Summary



# base:fullscreen [Codebase64 wiki]

## Fullscreen vectors

Rendering lines into a single charset is a quite easy excursion, as we operate on the current pixel/line only. With filled areas, we have shared edges with other polygons, this raises complexity quite a bit. (And there's even more to make it complicated)

So let's define the goal to render a filled area into a single charset, where the screen is used as map. Whenever a new position on screen is taken, we can either add more content to...
