---
id: src-sprites-in-bottom-sideborder
type: source
title: 'Source Summary: Sprites in bottom sideborder'
aliases:
- Sprites in bottom sideborder
- sprites_in_bottom_sideborder.md
tags:
- raster interrupts
- assembly
- sprite programming
- memory management
sources:
- path: data/docs/codebase_c64_org/base/sprites_in_bottom_sideborder.md
  sha256: 60e614c61709688e42d3d12161263a106ac8e444407a58907170f7d12c6ce5db
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Sprites in bottom sideborder

**Raw Source File**: `data/docs/codebase_c64_org/base/sprites_in_bottom_sideborder.md`
**SHA256**: `60e614c61709688e42d3d12161263a106ac8e444407a58907170f7d12c6ce5db`

## Summary




# Sprites in bottom sideborder

base:sprites_in_bottom_sideborder

                # Sprites in bottom sideborder

By Groepaz.

```
        *=$0810
        sei
        ; init ghostbyte with some pattern to make border more visible
        ; and so we can see character boundaries in the border
        lda #%10000000
        sta $3fff
        ; setup textscreen Y position
        lda #$18
        sta $d011
        ; init X scroll
        lda #$c8
        sta $d016
        ; now setup the 8 spri...
