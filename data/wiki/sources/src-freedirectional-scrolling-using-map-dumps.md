---
id: src-freedirectional-scrolling-using-map-dumps
type: source
title: 'Source Summary: Freedirectional scrolling using map dumps'
aliases:
- Freedirectional scrolling using map dumps
- freedirectional_scrolling_using_map_dumps.md
tags:
- sprite programming
- graphics
- assembly
sources:
- path: data/docs/codebase_c64_org/base/freedirectional_scrolling_using_map_dumps.md
  sha256: 1cd63a10c6975c288f06513891f7f7f41b7ee8657ca5cb6372dcd8b8eddb0a5b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Freedirectional scrolling using map dumps

**Raw Source File**: `data/docs/codebase_c64_org/base/freedirectional_scrolling_using_map_dumps.md`
**SHA256**: `1cd63a10c6975c288f06513891f7f7f41b7ee8657ca5cb6372dcd8b8eddb0a5b`

## Summary




# Freedirectional scrolling using map dumps

# Freedirectional scrolling using map dumps

by Achim

Here's the traditional way of scrolling. It can be found in classic games like Uridium, Paradroid, Ghosts'n Goblins etc.

The idea is to fully decode the map data and store it into RAM. In terms of memory usage this is not very efficient, of course. But by defining an origin top/left of the decoded map data the actual screen data can be displayed directly onto the screen. No RAM-shifitng routin...
