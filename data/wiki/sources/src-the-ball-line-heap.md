---
id: src-the-ball-line-heap
type: source
title: 'Source Summary: The ball line heap'
aliases:
- The ball line heap
- the_ball_line_heap.md
tags:
- assembly
- sprite programming
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/the_ball_line_heap.md
  sha256: 53fde1549174543d42c3cb15c4dbba9d4d404d4ba3175be859656ba115d96c1d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: The ball line heap

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/the_ball_line_heap.md`
**SHA256**: `53fde1549174543d42c3cb15c4dbba9d4d404d4ba3175be859656ba115d96c1d`

## Summary



# The ball line heap

## How we remember the lines used to draw circles so they can be redrawn

The planet, the sun and ships in our local bubble of universe are complicated things, and we have to use an awful lot of maths to calculate their shapes on-screen. Not surprisingly, all that maths takes up quite a bit of processor time. We can remove shapes from the screen by drawing the same shapes again in exactly the same place (which erases them because it's all done with EOR logic), so if we ca...
