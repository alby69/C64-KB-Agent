---
id: src-bitplanes-in-nes-elite
type: source
title: 'Source Summary: Bitplanes in NES Elite'
aliases:
- Bitplanes in NES Elite
- bitplanes_in_nes_elite.md
tags:
- basic
- assembly
- memory management
- sprite programming
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/bitplanes_in_nes_elite.md
  sha256: 718807ed816c1d54764e5e858064fb50ab5ca659a73a5ff0a2b74769fb84d859
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Bitplanes in NES Elite

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/bitplanes_in_nes_elite.md`
**SHA256**: `718807ed816c1d54764e5e858064fb50ab5ca659a73a5ff0a2b74769fb84d859`

## Summary



# Bitplanes in NES Elite

## Squeezing two patterns into one tile using separate bitplanes

In the deep dive on [understanding the NES for Elite](https://elite.bbcelite.com/understanding_the_nes_for_elite.html), we saw how the pattern tables in the PPU's VRAM store patterns in four colours. This is the standard way of looking at NES graphics, and for most NES games, it makes sense: tiles contain four colours, and you can set those colours via the attribute tables.

For the static screens of El...
