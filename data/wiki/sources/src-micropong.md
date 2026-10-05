---
id: src-micropong
type: source
title: 'Source Summary: base:micropong [Codebase64 wiki]'
aliases:
- base:micropong [Codebase64 wiki]
- micropong.md
tags:
- raster interrupts
- assembly
- memory management
- input handling
sources:
- path: data/docs/codebase_c64_org/base/micropong.md
  sha256: 835f6b78690eef2be6f17ff947c3622cf991da0686dfc188ac9f982b007b4c5e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:micropong [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/micropong.md`
**SHA256**: `835f6b78690eef2be6f17ff947c3622cf991da0686dfc188ac9f982b007b4c5e`

## Summary




# base:micropong [Codebase64 wiki]

base:micropong

                It's a bit buggy (and unplayable) but it might show some techniques that may come in handy. The game features 2 player action (???), a real intro and a 8 by 8 pixel playfield. All of this in 824 bytes.

; sourcecrap [c]2005 HMVDVA/HeMa!
; do what you like with this. print it out and wipe your ass with it :-/
joystick1		= $dc01
joystick2		= $dc00
UP1			= 254
DOWN1		= 253
FIRE1		= 239
UP2			= 126
DOWN2		= 125
FIRE2		= 111
Games...
