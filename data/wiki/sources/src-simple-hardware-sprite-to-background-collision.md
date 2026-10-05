---
id: src-simple-hardware-sprite-to-background-collision
type: source
title: 'Source Summary: base:simple_hardware_sprite_to_background_collision [Codebase64
  wiki]'
aliases:
- base:simple_hardware_sprite_to_background_collision [Codebase64 wiki]
- simple_hardware_sprite_to_background_collision.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/simple_hardware_sprite_to_background_collision.md
  sha256: a9e76ce787b87ae6b884a08fe0a759f4864435add76934a6d5b7388b1b6e8a41
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:simple_hardware_sprite_to_background_collision [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/simple_hardware_sprite_to_background_collision.md`
**SHA256**: `a9e76ce787b87ae6b884a08fe0a759f4864435add76934a6d5b7388b1b6e8a41`

## Summary



# base:simple_hardware_sprite_to_background_collision [Codebase64 wiki]

base:simple_hardware_sprite_to_background_collision

                #### Simple Hardware Sprite to Background collision

Using $D01E causes a simple hardware sprite/sprite collision detection, but some games I wrote i.e. Bomb Chase, Balloonacy and Balloonacy 2 all used hardware sprite/sprite collision, which uses $D01F only for the player's sprite. Here is how the code worked.

```
       lda $d01f
       lsr a ;Sprite 0...
