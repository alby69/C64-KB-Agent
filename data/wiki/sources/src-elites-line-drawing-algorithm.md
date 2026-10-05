---
id: src-elites-line-drawing-algorithm
type: source
title: 'Source Summary: Elite''s line-drawing algorithm'
aliases:
- Elite's line-drawing algorithm
- elites_line-drawing_algorithm.md
tags:
- basic
- assembly
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/elites_line-drawing_algorithm.md
  sha256: 23fc48cb71a8a47a33986dcd492c4ab3b0a1e6ed3a155694dcb642e916883314
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Elite's line-drawing algorithm

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/elites_line-drawing_algorithm.md`
**SHA256**: `23fc48cb71a8a47a33986dcd492c4ab3b0a1e6ed3a155694dcb642e916883314`

## Summary



# Elite's line-drawing algorithm

## The main line-drawing algorithm used to draw non-horizontal lines

Most of what you see in the space view in Elite is composed of straight lines. The ships are drawn using wireframes that are made up of straight lines, the planets are made from circles and arcs that consist of lots of small, straight lines, and the sun is no more than a sequence of horizontal lines, drawn along a vertical axis. Having a fast line-drawing algorithm is essential in a game lik...
