---
id: src-extract-column-from-tile-based-map
type: source
title: 'Source Summary: Extract column from tile based maps'
aliases:
- Extract column from tile based maps
- extract_column_from_tile_based_map.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/extract_column_from_tile_based_map.md
  sha256: e0f200efa12fdc477908d4fcfe2cef5d68f2435e805f555b1c2f8db699645717
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Extract column from tile based maps

**Raw Source File**: `data/docs/codebase_c64_org/base/extract_column_from_tile_based_map.md`
**SHA256**: `e0f200efa12fdc477908d4fcfe2cef5d68f2435e805f555b1c2f8db699645717`

## Summary



# Extract column from tile based maps

# Extract column from tile based maps

by Achim

For a side scrolling game you'll have to extract one row only from your tile data and print it left or right on the screen. The following routine can be used to extract columns on either side. Call it like this:

ldy lo-bytescreen
ldx hi-bytescreen
jsr extractcolumn

To make this work properly a map pointer (always top/left) and tileX (=column 00, 01, 02, 03) have to be defined.

The main program should use...
