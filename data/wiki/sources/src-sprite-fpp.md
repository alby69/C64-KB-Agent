---
id: src-sprite-fpp
type: source
title: 'Source Summary: Sprite FPP'
aliases:
- Sprite FPP
- sprite_fpp.md
tags:
- raster interrupts
- sprite programming
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/sprite_fpp.md
  sha256: 2fe996b8f5785d7f30d39b15aca6192dbf7c33bda5229f6a06f5c260e7482e5f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Sprite FPP

**Raw Source File**: `data/docs/codebase_c64_org/base/sprite_fpp.md`
**SHA256**: `2fe996b8f5785d7f30d39b15aca6192dbf7c33bda5229f6a06f5c260e7482e5f`

## Summary




# Sprite FPP

# Sprite FPP

The basic theory behind a Sprite FPP is quite simple: Change sprite-pointer value every rasterline. Though there are a few things to prepare before it works in reality.

First we want to use a bigger graphics area than one sprite. With a normal [$d017-stretcher](https://codebase.c64.org/doku.php?id=base:stretching_sprites) we can make the sprites arbitrary high, and at the same time we only use one line of the sprite for graphics. If we then place our 8 sprites bes...
