---
id: src-drawing-lines-in-the-nes-version
type: source
title: 'Source Summary: Drawing lines in the NES version'
aliases:
- Drawing lines in the NES version
- drawing_lines_in_the_nes_version.md
tags:
- basic
- assembly
- graphics
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/drawing_lines_in_the_nes_version.md
  sha256: fb17998ef3d6454268d909c18e28a912743089a83b35515f54e302bd32243e5d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Drawing lines in the NES version

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/drawing_lines_in_the_nes_version.md`
**SHA256**: `fb17998ef3d6454268d909c18e28a912743089a83b35515f54e302bd32243e5d`

## Summary



# Drawing lines in the NES version

## Using tiles as stepping stones when drawing lines on the NES

Elite's space view is all about lines - it is a wireframe game, after all. And it turns out that every 6502-based version of Elite draws lines in the same way, using a well-known approach that's described in detail in the deep dive on [Elite's line-drawing algorithm](https://elite.bbcelite.com/elites_line-drawing_algorithm.html).

The NES version is no different, but because NES graphics are ti...
