---
id: src-moving-sprites
type: source
title: 'Source Summary: Moving sprites / Sorting movement from VIC update'
aliases:
- Moving sprites / Sorting movement from VIC update
- moving_sprites.md
tags:
- raster interrupts
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/moving_sprites.md
  sha256: cf06beab0cd3b117a377239e9f066c23b2da9f3afdb53a9306380b2d6ed8fea9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Moving sprites / Sorting movement from VIC update

**Raw Source File**: `data/docs/codebase_c64_org/base/moving_sprites.md`
**SHA256**: `cf06beab0cd3b117a377239e9f066c23b2da9f3afdb53a9306380b2d6ed8fea9`

## Summary



# Moving sprites / Sorting movement from VIC update

base:moving_sprites

                ### Table of Contents

# Moving sprites / Sorting movement from VIC update

by Achim

## x+msb

Moving sprites can be annoying in terms of msb handling. To avoid the msb issue you usually use tables for moving the sprites and let a small routine update the VIC registers every frame.

spritey:	.byte $00, $00, $00, $00, $00, $00, $00, $00
spritex:	.byte $00, $00, $00, $00, $00, $00, $00, $00
spritemsb:	.byt...
