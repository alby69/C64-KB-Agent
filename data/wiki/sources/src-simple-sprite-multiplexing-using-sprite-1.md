---
id: src-simple-sprite-multiplexing-using-sprite-1
type: source
title: 'Source Summary: base:simple_sprite-multiplexing_using_sprite_1 [Codebase64
  wiki]'
aliases:
- base:simple_sprite-multiplexing_using_sprite_1 [Codebase64 wiki]
- simple_sprite-multiplexing_using_sprite_1.md
tags:
- sprite programming
- basic
- graphics
- assembly
- raster interrupts
sources:
- path: data/docs/codebase_c64_org/base/simple_sprite-multiplexing_using_sprite_1.md
  sha256: 0ac76fff1a9575fbd3b70f84208b82d3e753092f25e584019131386c54134ac2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:simple_sprite-multiplexing_using_sprite_1 [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/simple_sprite-multiplexing_using_sprite_1.md`
**SHA256**: `0ac76fff1a9575fbd3b70f84208b82d3e753092f25e584019131386c54134ac2`

## Summary




# base:simple_sprite-multiplexing_using_sprite_1 [Codebase64 wiki]

base:simple_sprite-multiplexing_using_sprite_1

                ```
 !to "multiplexer.prg",cbm
 
;---------------------------------------------------------------------------
;
;
;
; Basics : IRQ
; @L       Wait for Y-Pos
;          write (new) Y-Position            
;          write (new) Sprite-Pointer 
;          set some other registers according to the sprite
;          wait 21+1 (Spriteheight+1) Rasterlines 
;          J...
