---
id: src-spriteintro
type: source
title: 'Source Summary: General introduction to sprites'
aliases:
- General introduction to sprites
- spriteintro.md
tags:
- raster interrupts
- sprite programming
- graphics
- assembly
sources:
- path: data/docs/codebase_c64_org/base/spriteintro.md
  sha256: 04d2f149c00e05c86d5139eb143bf9c8f0c609cb8484118ec8b48afd85e6edfd
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: General introduction to sprites

**Raw Source File**: `data/docs/codebase_c64_org/base/spriteintro.md`
**SHA256**: `04d2f149c00e05c86d5139eb143bf9c8f0c609cb8484118ec8b48afd85e6edfd`

## Summary




# General introduction to sprites

### Table of Contents

# General introduction to sprites

Sprites are freely movable 24×21 hires pixel sized objects. There are 8 of them, while it is possible to display more than 8, the rule of thumb is that *it is not possible display more than 8 on the same rasterline.*

Sprites have the following attributes:

- Display Enabled/Disabled
- X,Y position
- Multicolor/Hires mode
- One individual color/sprite
- In multicolor mode you have 2 colors that are th...
