---
id: src-decoding-tile-based-maps
type: source
title: 'Source Summary: Decoding 4x4 tiles'
aliases:
- Decoding 4x4 tiles
- decoding_tile_based_maps.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/decoding_tile_based_maps.md
  sha256: 2d667f495a9e36ac8a4c3eded07263d5875218d18ba1539cf35bdf4a74eae4d0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Decoding 4x4 tiles

**Raw Source File**: `data/docs/codebase_c64_org/base/decoding_tile_based_maps.md`
**SHA256**: `2d667f495a9e36ac8a4c3eded07263d5875218d18ba1539cf35bdf4a74eae4d0`

## Summary




# Decoding 4x4 tiles

# Decoding 4x4 tiles

by Achim

If you use tile based maps for a game, you'll have to decode a whole screen first unless you want your scroll routine to scroll the background graphics onto the screen. Here's a piece of code that decodes 4×4 tiles to the screen. It colours the whole screen black (mc). Usually you've got two options:

1. Colour per tile
2. Colour per char

The first option is very useful when you want to save rastertime for the main program, but is obvious...
