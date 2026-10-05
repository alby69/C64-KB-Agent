---
id: src-extended-screen-coordinates
type: source
title: 'Source Summary: Extended screen coordinates'
aliases:
- Extended screen coordinates
- extended_screen_coordinates.md
tags:
- basic
- assembly
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/extended_screen_coordinates.md
  sha256: 33940729e9eaf5bb1755ccbd98ebba45ffcb5459b805e5e5a86035527177769b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Extended screen coordinates

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/extended_screen_coordinates.md`
**SHA256**: `33940729e9eaf5bb1755ccbd98ebba45ffcb5459b805e5e5a86035527177769b`

## Summary



# Extended screen coordinates

## The extended 16-bit screen coordinate system behind the space view

When simulating its universe of ships, stars and space stations, Elite uses large numbers - space is big, after all. The ship coordinates are stored as sign-magnitude numbers with 16 bits for the magnitudes, while the planet and sun coordinates go all the way up to 23-bit magnitudes (as they can be a lot further away from us than ships and stations).

To maintain accuracy when projecting these...
