---
id: src-simple-software-sprite-to-background-collision
type: source
title: 'Source Summary: Simple Software to Background collision'
aliases:
- Simple Software to Background collision
- simple_software_sprite_to_background_collision.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/simple_software_sprite_to_background_collision.md
  sha256: bc2b5a75dad75d8707f67847e1731bd8abb3b9317859f21dacd0e3a86cd83a7c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Simple Software to Background collision

**Raw Source File**: `data/docs/codebase_c64_org/base/simple_software_sprite_to_background_collision.md`
**SHA256**: `bc2b5a75dad75d8707f67847e1731bd8abb3b9317859f21dacd0e3a86cd83a7c`

## Summary



# Simple Software to Background collision

base:simple_software_sprite_to_background_collision

                # Simple Software to Background collision

by Achim

To check wether a specific object has been hit or not, the correct screen position has to be calculated.

Use sprite-X to calculate the screen column:

lda spriteX     //16bit subtraction
sec            
sbc #$18	//x-offset, visible screen area starts at x=$18
sta tmp1
lda spriteMSB	//MSB in bit 0 of spriteMSB
sbc #$00        
lsr ...
