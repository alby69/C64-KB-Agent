---
id: src-fake-music-player
type: source
title: 'Source Summary: Fake Music Player'
aliases:
- Fake Music Player
- fake_music_player.md
tags:
- sprite programming
- basic
- assembly
- raster interrupts
- sound generation
- memory management
sources:
- path: data/docs/codebase_c64_org/base/fake_music_player.md
  sha256: 13db76112eb6a4e66b595d56f1286dcd33510e26d4177e5718ec7b6caf029e2b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Fake Music Player

**Raw Source File**: `data/docs/codebase_c64_org/base/fake_music_player.md`
**SHA256**: `13db76112eb6a4e66b595d56f1286dcd33510e26d4177e5718ec7b6caf029e2b`

## Summary




# Fake Music Player

### Table of Contents

# Fake Music Player

By karoshier.

## The problem

While coding a game, or a demo effect that eats up lots of raster time, the coder ought to consider also the music. And such music is likely not to be ready yet or simply the code is in a too early stage to start talking about the music which is going to fulfill the explosion of senses of the finished production. But we still want:

- our init and play calls already in place, to forget about them
-...
