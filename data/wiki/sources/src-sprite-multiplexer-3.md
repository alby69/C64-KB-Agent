---
id: src-sprite-multiplexer-3
type: source
title: 'Source Summary: Sprite Multiplexer'
aliases:
- Sprite Multiplexer
- sprite_multiplexer_3.md
tags:
- raster interrupts
- assembly
- sprite programming
- memory management
sources:
- path: data/docs/codebase_c64_org/base/sprite_multiplexer_3.md
  sha256: a2ce19a2cc341e7ec0ce2008058956c7dd1eceb47e2886003cde8901ed3be334
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Sprite Multiplexer

**Raw Source File**: `data/docs/codebase_c64_org/base/sprite_multiplexer_3.md`
**SHA256**: `a2ce19a2cc341e7ec0ce2008058956c7dd1eceb47e2886003cde8901ed3be334`

## Summary




# Sprite Multiplexer

base:sprite_multiplexer_3

                # Sprite Multiplexer

Turbo Assembler source. This one is more advanced than the other one made by Fungus but still got some bugs. Watch out!

```
;---------------------------------------
;New Multiplexer Engine
;24 sprite version
;
;Written by Fungus in 2005
;---------------------------------------
         *= $2000
xofs     = $06          ;x position
                        ;offset
yofs     = $06          ;x position
         ...
