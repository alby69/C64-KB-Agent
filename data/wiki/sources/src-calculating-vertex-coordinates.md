---
id: src-calculating-vertex-coordinates
type: source
title: 'Source Summary: Calculating vertex coordinates'
aliases:
- Calculating vertex coordinates
- calculating_vertex_coordinates.md
tags:
- assembly
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/calculating_vertex_coordinates.md
  sha256: 9c89b5f148cebe32e9732427ea9f6df814631c49828a0af2ffbbd77acc1e3421
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Calculating vertex coordinates

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/calculating_vertex_coordinates.md`
**SHA256**: `9c89b5f148cebe32e9732427ea9f6df814631c49828a0af2ffbbd77acc1e3421`

## Summary



# Calculating vertex coordinates

## Determining whether a ship's vertex is visible or hidden from us

To understand the following, you'll probably want to have a look through the deep dive on [back-face culling](https://elite.bbcelite.com/back-face_culling.html), which describes how we can work out whether or not a ship's face is visible.

As part of the back-face cull, we projected the vector [x y z] onto the orientation vector space like this:

  [x y z] projected onto sidev = [x y z] . sid...
