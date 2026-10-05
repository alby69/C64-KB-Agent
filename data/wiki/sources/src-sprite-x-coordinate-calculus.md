---
id: src-sprite-x-coordinate-calculus
type: source
title: 'Source Summary: base:sprite_x-coordinate_calculus [Codebase64 wiki]'
aliases:
- base:sprite_x-coordinate_calculus [Codebase64 wiki]
- sprite_x-coordinate_calculus.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/sprite_x-coordinate_calculus.md
  sha256: ecf6658f4c15b3cbd9b65add400bf8b2b0befdfa301628b340d20b2df5dcc6f9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:sprite_x-coordinate_calculus [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/sprite_x-coordinate_calculus.md`
**SHA256**: `ecf6658f4c15b3cbd9b65add400bf8b2b0befdfa301628b340d20b2df5dcc6f9`

## Summary



# base:sprite_x-coordinate_calculus [Codebase64 wiki]

base:sprite_x-coordinate_calculus

                ## Signed Sprite X-Coordinate calculus: by delta table

This piece of code adds a signed byte (from the delta table) to an unsigned byte (the sprite x-coordinate) and returns a unsigned 9-bit number, storing the lower 8-bits on the sprite x-coordinate register and 9th bit on the sprite x-coordinate MSB register.

```
	;Calc new sprite 0 X-coordinate by delta table
        ;by The_WOZ/soft1...
