---
id: src-drawing-pixels-in-the-electron-version
type: source
title: 'Source Summary: Drawing pixels in the Electron version'
aliases:
- Drawing pixels in the Electron version
- drawing_pixels_in_the_electron_version.md
tags:
- basic
- assembly
- graphics
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/drawing_pixels_in_the_electron_version.md
  sha256: d2a58fdaa45cda2d233280341d987fa34667e43f8475b1d34d571beb0d2276c1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Drawing pixels in the Electron version

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/drawing_pixels_in_the_electron_version.md`
**SHA256**: `d2a58fdaa45cda2d233280341d987fa34667e43f8475b1d34d571beb0d2276c1`

## Summary



# Drawing pixels in the Electron version

## Poking pixels into screen memory in the Acorn Electron version of Elite

The BBC Micro version of Elite has a custom screen mode that makes life pretty easy when poking pixels into screen memory. The main reason is the [square custom screen mode](https://elite.bbcelite.com/drawing_monochrome_pixels_in_mode_4.html), which is based on mode 4, but with a reduced width and height (it has 32 character columns and 31 character rows, compared to 40 columns...
