---
id: src-drawing-pixels-in-the-nes-version
type: source
title: 'Source Summary: Drawing pixels in the NES version'
aliases:
- Drawing pixels in the NES version
- drawing_pixels_in_the_nes_version.md
tags:
- basic
- assembly
- graphics
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/drawing_pixels_in_the_nes_version.md
  sha256: 2d28f414c299cd4b3d5c924ae020b012deab28de1931a32b58a415e238e20bb2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Drawing pixels in the NES version

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/drawing_pixels_in_the_nes_version.md`
**SHA256**: `2d28f414c299cd4b3d5c924ae020b012deab28de1931a32b58a415e238e20bb2`

## Summary



# Drawing pixels in the NES version

## How the NES version pokes pixels into the console's tile-based screen

As described in the deep dive on [understanding the NES for Elite](https://elite.bbcelite.com/understanding_the_nes_for_elite.html), graphics on the NES are really different to home computers like the BBC Micro. In particular, the freedom of being able to poke pixels directly into screen memory - which is at the core of the graphics routines in most versions of Elite - is replaced by ...
