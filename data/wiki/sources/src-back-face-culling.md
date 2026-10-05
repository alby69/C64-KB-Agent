---
id: src-back-face-culling
type: source
title: 'Source Summary: Back-face culling'
aliases:
- Back-face culling
- back-face_culling.md
tags:
- basic
- assembly
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/back-face_culling.md
  sha256: 2073748b1a769ec0e990ad99f3787eb4bd7020f94dca903c8bd26530f54940dd
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Back-face culling

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/back-face_culling.md`
**SHA256**: `2073748b1a769ec0e990ad99f3787eb4bd7020f94dca903c8bd26530f54940dd`

## Summary



# Back-face culling

## How Elite draws solid-looking 3D ships by only drawing visible faces

One of the reasons that Elite's 3D wireframe ships look so good is because you can't see through them - they look genuinely solid. This is down to a process called "back-face culling", a mathematical process that works out which faces of the ship are visible to the viewer and which ones aren't. It then discards (or "culls") any faces that aren't visible and only draws those that we can actually see. T...
