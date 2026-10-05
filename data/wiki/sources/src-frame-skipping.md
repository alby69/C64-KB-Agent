---
id: src-frame-skipping
type: source
title: 'Source Summary: Frame skipping'
aliases:
- Frame skipping
- frame_skipping.md
tags:
- raster interrupts
- assembly
sources:
- path: data/docs/codebase_c64_org/base/frame_skipping.md
  sha256: f24716f72450945b1e8c675869ccb13a1c65639ccd2582b423a93581d77eeb9c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Frame skipping

**Raw Source File**: `data/docs/codebase_c64_org/base/frame_skipping.md`
**SHA256**: `f24716f72450945b1e8c675869ccb13a1c65639ccd2582b423a93581d77eeb9c`

## Summary



# Frame skipping

base:frame_skipping

                # Frame skipping

Once in a while you created some effect that just goes too quick when you update it every frame. The option is to have a check in order to skip your routine every other frame. Put this inside your IRQ.

start:
   inc skipper+1      // increase the check byte
   
skipper:
   lda #$00           // check byte
   and #$01           // check first bit (even or odd number?)
   beq passroutine    // skip routine on even numbers
...
