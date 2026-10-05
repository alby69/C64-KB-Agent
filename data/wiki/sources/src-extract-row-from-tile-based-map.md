---
id: src-extract-row-from-tile-based-map
type: source
title: 'Source Summary: Extract row from tile based map'
aliases:
- Extract row from tile based map
- extract_row_from_tile_based_map.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/extract_row_from_tile_based_map.md
  sha256: 70579434cc7fe64b21cd7c8f21bfd9e06fc224c6afe3323051a73acb3c64ffbe
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Extract row from tile based map

**Raw Source File**: `data/docs/codebase_c64_org/base/extract_row_from_tile_based_map.md`
**SHA256**: `70579434cc7fe64b21cd7c8f21bfd9e06fc224c6afe3323051a73acb3c64ffbe`

## Summary



# Extract row from tile based map

base:extract_row_from_tile_based_map

                # Extract row from tile based map

by Achim

Example 4×4 tile:

aabb
ccdd
eeff
gghh

Tile data stored in memory:

aabbccddeeffgghh

In order to read and plot the correct tile row for a vertical scrolling game, tileY has to be defined.

```
tileY: 00, ...    aabb
       04, ...    ccdd
       08, ...    eeff
       0c, ...    gghh
```
Again a map pointer is needed (top-left) and mapX (=map width) for correc...
