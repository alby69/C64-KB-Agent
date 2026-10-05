---
id: src-flexible-32-sprite-multiplexer
type: source
title: 'Source Summary: base:flexible_32_sprite_multiplexer [Codebase64 wiki]'
aliases:
- base:flexible_32_sprite_multiplexer [Codebase64 wiki]
- flexible_32_sprite_multiplexer.md
tags:
- raster interrupts
- assembly
- sprite programming
- input handling
sources:
- path: data/docs/codebase_c64_org/base/flexible_32_sprite_multiplexer.md
  sha256: 169daeb585df1a04f79669faf94470e925561426435a199f070db7d8cd64acfe
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:flexible_32_sprite_multiplexer [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/flexible_32_sprite_multiplexer.md`
**SHA256**: `169daeb585df1a04f79669faf94470e925561426435a199f070db7d8cd64acfe`

## Summary




# base:flexible_32_sprite_multiplexer [Codebase64 wiki]

base:flexible_32_sprite_multiplexer

                ## Flexible 32 Sprite Multiplexer

Here's an example of a flexible 32 Sprite Multiplexer with dynamic interrupts and very fast y-pos sorting. I wanted to use this in a sequel of Vincent, a jump and run game I wrote in 1990. The sorting routine is based on 'Bubble a la Rune' and uses an unrolled approach using zeropage variables for speed. It should be one of the fastest multiplexers a...
