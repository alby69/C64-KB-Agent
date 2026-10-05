---
id: src-line-clipping
type: source
title: 'Source Summary: Line-clipping'
aliases:
- Line-clipping
- line-clipping.md
tags:
- basic
- assembly
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/line-clipping.md
  sha256: 001bc5e9379075d43c37fedc86c30ac4bc2502b34a6ba9982cc53fe6c11ff14d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Line-clipping

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/line-clipping.md`
**SHA256**: `001bc5e9379075d43c37fedc86c30ac4bc2502b34a6ba9982cc53fe6c11ff14d`

## Summary



# Line-clipping

## Efficiently clipping an extended line to the part that's on-screen

Space is big. Vintage computer screens, however, are not big. Elite's space view is a whopping 256 pixels across and 192 pixels high, and somehow we have to cram planets, suns and seat-of-the-pants space battles into this tiny, thumbnail-sized bit of cathode-ray real estate. This isn't easy.

The first part of the solution is to simulate not only the part of space that's visible on-screen, but the surroundi...
