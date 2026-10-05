---
id: src-pattern-and-nametable-buffers
type: source
title: 'Source Summary: The pattern and nametable buffers'
aliases:
- The pattern and nametable buffers
- pattern_and_nametable_buffers.md
tags:
- basic
- assembly
- graphics
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/pattern_and_nametable_buffers.md
  sha256: 09da58edff1c973eb7eb5faf8a7b4742c1cf9b7bc84a890311fd943f51dfd126
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: The pattern and nametable buffers

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/pattern_and_nametable_buffers.md`
**SHA256**: `09da58edff1c973eb7eb5faf8a7b4742c1cf9b7bc84a890311fd943f51dfd126`

## Summary



# The pattern and nametable buffers

## How the NES version achieves its beautifully smooth wireframe graphics

Unlike the other 6502-based versions of Elite, the NES version doesn't draw directly into screen memory. Instead, it draws into the pattern, nametable and attribute buffers, so let's take a look at this fundamental aspect of the game's graphics engine.

There are two sets of these graphics buffers. They are stored in the extra WRAM that's provided in the Elite cartridge (this RAM is ...
