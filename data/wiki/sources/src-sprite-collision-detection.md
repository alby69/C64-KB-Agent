---
id: src-sprite-collision-detection
type: source
title: 'Source Summary: Individual sprite ''boxes'' for collision detection'
aliases:
- Individual sprite 'boxes' for collision detection
- sprite_collision_detection.md
tags:
- raster interrupts
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/sprite_collision_detection.md
  sha256: 02f66cbf8c3adc793a488f19eeb849ec93b8ad7c09578237d6beb8feac292034
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Individual sprite 'boxes' for collision detection

**Raw Source File**: `data/docs/codebase_c64_org/base/sprite_collision_detection.md`
**SHA256**: `02f66cbf8c3adc793a488f19eeb849ec93b8ad7c09578237d6beb8feac292034`

## Summary




# Individual sprite 'boxes' for collision detection

### Table of Contents

# Individual sprite 'boxes' for collision detection

by Achim

The regular way of detecting a sprite to sprite collision is to define a box around the sprite, which means you add an offset to the sprite's y and x values to get y2 and x2.

In most cases the '[one size fits all](https://codebase.c64.org/doku.php?id=base:simple_software_sprite_to_sprite_collision)' approach will work, as long as all sprites in the game h...
