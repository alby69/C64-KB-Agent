---
id: src-hybrid-hardware-software-sprite-collision-detection
type: source
title: 'Source Summary: base:hybrid_hardware_software_sprite_collision_detection [Codebase64
  wiki]'
aliases:
- base:hybrid_hardware_software_sprite_collision_detection [Codebase64 wiki]
- hybrid_hardware_software_sprite_collision_detection.md
tags:
- sprite programming
- assembly
- memory management
sources:
- path: data/docs/codebase_c64_org/base/hybrid_hardware_software_sprite_collision_detection.md
  sha256: ffeb4c716f48d02a32af4eec0ba213deba88eb2525b7e1269729ee0c5cd894bd
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:hybrid_hardware_software_sprite_collision_detection [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/hybrid_hardware_software_sprite_collision_detection.md`
**SHA256**: `ffeb4c716f48d02a32af4eec0ba213deba88eb2525b7e1269729ee0c5cd894bd`

## Summary



# base:hybrid_hardware_software_sprite_collision_detection [Codebase64 wiki]

base:hybrid_hardware_software_sprite_collision_detection

                This code checks which sprite triggered the hardware sprite collision detection when bit 1 of $D01E is turned on. Assuming sprite 0 is the player sprite and sprites 1…7 are the “enemies”. A collision is considered TRUE if a sprite is within +/-20px on the Y axis and +/-23px on X axis from the player sprite. SPR_COLL_DETECT returns in .X the spr...
