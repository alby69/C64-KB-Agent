---
id: src-cbm64disp
type: source
title: 'Source Summary: Commodore 64 display modes'
aliases:
- Commodore 64 display modes
- cbm64disp.md
tags:
- graphics
- assembly
sources:
- path: data/docs/sta_c64_org/cbm64disp.md
  sha256: ac227576b4e010b85bd502d0789bb75f3414911a841efe3d41d0904c90bc58c1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Commodore 64 display modes

**Raw Source File**: `data/docs/sta_c64_org/cbm64disp.md`
**SHA256**: `ac227576b4e010b85bd502d0789bb75f3414911a841efe3d41d0904c90bc58c1`

## Summary




# Commodore 64 display modes

Screen based on:

- Screen RAM ($0400-$07FF, configurable)
- Character ROM ($D000-$DFFF)

Colors based on:

- Background Color ($D021)
- Color RAM ($D800-$DBFF)

Character shape and color:

1. Fetch screen byte from Screen RAM, multiply it by 8.
2. If charset is in lowercase/uppercase mode, add 2048 ($0800).
3. Fetch 8 bytes from this offset of the Character ROM and use it as a bitmap: 
  - Bit = 0: Pixel has background color.
  - Bit = 1: Pixel color is determin...
