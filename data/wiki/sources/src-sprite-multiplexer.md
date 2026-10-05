---
id: src-sprite-multiplexer
type: source
title: 'Source Summary: Sprite Multiplexer'
aliases:
- Sprite Multiplexer
- sprite_multiplexer.md
tags:
- sprite programming
- basic
- assembly
- raster interrupts
- memory management
sources:
- path: data/docs/codebase_c64_org/base/sprite_multiplexer.md
  sha256: 9aed113a67c46f71aecd814465197dda24c83ded1f49c5fc203ae4a3d131cdfb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Sprite Multiplexer

**Raw Source File**: `data/docs/codebase_c64_org/base/sprite_multiplexer.md`
**SHA256**: `9aed113a67c46f71aecd814465197dda24c83ded1f49c5fc203ae4a3d131cdfb`

## Summary




# Sprite Multiplexer

# Sprite Multiplexer

By Fungus/Nostalgia.

The sources are in Turbo Assembler format.

You should be able to have 1 independant color per sprite, and also an independant image for each sprite. You could also add fore/background priority buffers and add that register to your plot code.

I chose to go for shortness in this routine rather than pure speed. It can be speeded up about 20% by unrolling all the plotting loops and using self modifed code instead of the second se...
