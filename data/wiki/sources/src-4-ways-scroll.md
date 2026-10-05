---
id: src-4-ways-scroll
type: source
title: 'Source Summary: base:4_ways_scroll [Codebase64 wiki]'
aliases:
- base:4_ways_scroll [Codebase64 wiki]
- 4_ways_scroll.md
tags:
- raster interrupts
- sprite programming
sources:
- path: data/docs/codebase_c64_org/base/4_ways_scroll.md
  sha256: c5b0ed886ce1cab1afa4ee280b815ca5f11692ecfd9b21d37711fd5128f3a290
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:4_ways_scroll [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/4_ways_scroll.md`
**SHA256**: `c5b0ed886ce1cab1afa4ee280b815ca5f11692ecfd9b21d37711fd5128f3a290`

## Summary




# base:4_ways_scroll [Codebase64 wiki]

base:4_ways_scroll

                
4 Way Scroll by Malcolm Bamber
[http://www.dark-well.pwp.blueyonder.co.uk/](http://www.dark-well.pwp.blueyonder.co.uk/)

How I scrolled a 2 by 2 tiled map I hope it is a help to some one trying to scroll the screen

This first part here will show you what the irq is doing when called

*SCROLL UP* 

IF YSCROLL=3

  ADD ONE TO UDFLAG
  IF UDFLAG NOT 1 OR 2 THEN THEN QUIT OUT OF IRQ
  IF UDFLAG=1 THEN SO MOVE MAP POINTE...
