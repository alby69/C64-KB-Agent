---
id: src-stretching-sprites
type: source
title: 'Source Summary: Sprite Stretching'
aliases:
- Sprite Stretching
- stretching_sprites.md
tags:
- raster interrupts
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/stretching_sprites.md
  sha256: fc6695b9f3b9c882ac8827e63e385b815fe24daa72923d49d9d684d5c14b66d0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Sprite Stretching

**Raw Source File**: `data/docs/codebase_c64_org/base/stretching_sprites.md`
**SHA256**: `fc6695b9f3b9c882ac8827e63e385b815fe24daa72923d49d9d684d5c14b66d0`

## Summary




# Sprite Stretching

base:stretching_sprites

                # Sprite Stretching

Sprite stretching uses the technique of setting the bits of $d017 to 1, and then back to 0 on the next rasterline. This will fool the VIC not to increase the internal sprite-gfx-pointer and display the same line of sprite-graphics again. By repeating this trick every rasterline, you can decide how many times each line of sprite-graphics will be shown.

Code example follows. Note that $d017 is set from the table...
