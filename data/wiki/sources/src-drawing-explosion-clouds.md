---
id: src-drawing-explosion-clouds
type: source
title: 'Source Summary: Drawing explosion clouds'
aliases:
- Drawing explosion clouds
- drawing_explosion_clouds.md
tags:
- assembly
- sprite programming
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/drawing_explosion_clouds.md
  sha256: 34529cc946251eec1617e1577ba575a189468aef540fd079046491a54de14e0a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Drawing explosion clouds

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/drawing_explosion_clouds.md`
**SHA256**: `34529cc946251eec1617e1577ba575a189468aef540fd079046491a54de14e0a`

## Summary



# Drawing explosion clouds

## Drawing and storing explosion clouds for ships whose luck runs out...

Explosions in Elite are really rather beautiful. Here's a video of a Mamba glittering in the dark as it meets its maker:

Like the ships, planet and sun, explosion clouds take a lot of maths to draw, and like them, we store the results of all this maths in a heap. For explosion clouds, which we draw in the [DOEXP](https://elite.bbcelite.com/cassette/main/subroutine/doexp.html) routine, we use ...
