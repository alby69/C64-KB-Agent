---
id: src-playing-music-on-pal-and-ntsc
type: source
title: 'Source Summary: Playing music on PAL and NTSC'
aliases:
- Playing music on PAL and NTSC
- playing_music_on_pal_and_ntsc.md
tags:
- basic
- sound generation
sources:
- path: data/docs/codebase_c64_org/base/playing_music_on_pal_and_ntsc.md
  sha256: 3d7e1f56cb279fb723ef5d342f2ac40877610f249bc7203d046ebe5826bab907
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Playing music on PAL and NTSC

**Raw Source File**: `data/docs/codebase_c64_org/base/playing_music_on_pal_and_ntsc.md`
**SHA256**: `3d7e1f56cb279fb723ef5d342f2ac40877610f249bc7203d046ebe5826bab907`

## Summary



# Playing music on PAL and NTSC

# Playing music on PAL and NTSC

By FTC/HT

This article deals (briefly) with the question of how to play PAL tunes on a NTSC system, and vice versa. Most music players are called once a frame in order to update the music which is playing. One PAL frame is 312*63=19656 ($4CC8) cycles and one NTSC frame is 263*65=17095 ($42C7) cycles. In addition, a cycle is in itself taking a different amount of time on a PAL system compared to on a NTSC system because the syst...
