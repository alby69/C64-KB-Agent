---
id: src-backface-culling
type: source
title: 'Source Summary: base:backface_culling [Codebase64 wiki]'
aliases:
- base:backface_culling [Codebase64 wiki]
- backface_culling.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/backface_culling.md
  sha256: 6dda5283abc2d281b70096cf0ca8e0a039a518562a605d0ef82deb2d705053c1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:backface_culling [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/backface_culling.md`
**SHA256**: `6dda5283abc2d281b70096cf0ca8e0a039a518562a605d0ef82deb2d705053c1`

## Summary



# base:backface_culling [Codebase64 wiki]

### Backface Culling

by Bitbreaker/Oxyron/Nuance

An easy way to find out if a face faces towards the viewer or away is to check whether the area covered by a face is positive (frontface) or negative (backface). This done by taking the first 3 vertices (already transformed into 2D) of that face and calculating the following:

(v1.y - v0.y) * (v2.x - v1.x) - (v1.x - v0.x) * (v2.y - v1.y)

If the result is positive, the face is visible and rendered, el...
