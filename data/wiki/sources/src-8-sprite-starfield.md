---
id: src-8-sprite-starfield
type: source
title: 'Source Summary: base:8_sprite_starfield [Codebase64 wiki]'
aliases:
- base:8_sprite_starfield [Codebase64 wiki]
- 8_sprite_starfield.md
tags:
- raster interrupts
- sprite programming
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/8_sprite_starfield.md
  sha256: eb0abc73d33d1bf037436dc5d136759a3c3c0569cf4caf42e51e9939eedeb360
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:8_sprite_starfield [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/8_sprite_starfield.md`
**SHA256**: `eb0abc73d33d1bf037436dc5d136759a3c3c0569cf4caf42e51e9939eedeb360`

## Summary




# base:8_sprite_starfield [Codebase64 wiki]

base:8_sprite_starfield

                ## 8 Sprite Starfield

This piece of source, done in ACME shows you a very simple way to create a simple star field/space feature, using 8 sprites. Basically this is a simple routine that will wrap 8 stars across the screen, according to the speed table. Maybe some other time I'll work on a routine which will display more than 8 stars in its simplest form.

```
;==============================================...
