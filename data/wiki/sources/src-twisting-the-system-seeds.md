---
id: src-twisting-the-system-seeds
type: source
title: 'Source Summary: Twisting the system seeds'
aliases:
- Twisting the system seeds
- twisting_the_system_seeds.md
tags:
- basic
- assembly
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/twisting_the_system_seeds.md
  sha256: 34568345461c0b1957cb62dce564036f8fb4b5d679726dd46afd5f1fe80f1995
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Twisting the system seeds

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/twisting_the_system_seeds.md`
**SHA256**: `34568345461c0b1957cb62dce564036f8fb4b5d679726dd46afd5f1fe80f1995`

## Summary



# Twisting the system seeds

## How the system seeds are twisted to produce entire galaxies of stars

Data on each star system in Elite's galaxies is generated procedurally, and the core of this process is the set of three 16-bit seeds that describe each system in the universe. Each of the eight galaxies in the game is generated in the same way, by taking an initial set of seeds and "twisting" them to generate 256 systems, one after the other.

Specifically, given the initial set of seeds, we ...
