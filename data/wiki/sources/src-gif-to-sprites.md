---
id: src-gif-to-sprites
type: source
title: 'Source Summary: GIF to sprites'
aliases:
- GIF to sprites
- gif_to_sprites.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/gif_to_sprites.md
  sha256: 783d4551daa44448386f60b907b360595155d34ddea395d1f732d2975e766d69
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: GIF to sprites

**Raw Source File**: `data/docs/codebase_c64_org/base/gif_to_sprites.md`
**SHA256**: `783d4551daa44448386f60b907b360595155d34ddea395d1f732d2975e766d69`

## Summary



# GIF to sprites

# GIF to sprites

By Mace

This is a Kick Assembler script that turns a GIF into separate sprites. The order is represented by strings that contain letters, enabling you to make a sprite font with only the letters that you use, but distributed into memory where the sprite pointers have screen code offset.

To clearify: if you have the A as your first letter in the top left of your GIF, it will be transfered to spriteMemory + 1*64 (where 1 is the screencode of the letter A). S...
