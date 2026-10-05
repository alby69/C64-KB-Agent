---
id: src-playing-music-a000-ffff
type: source
title: 'Source Summary: Playing music at $A000 - $FFFF "behind" kernal'
aliases:
- Playing music at $A000 - $FFFF "behind" kernal
- playing_music_a000-_ffff.md
tags:
- raster interrupts
- basic
- sound generation
- assembly
sources:
- path: data/docs/codebase_c64_org/base/playing_music_a000-_ffff.md
  sha256: 9756f73c705357ddafddd5987d6711d6ecdc18b8900a07ff7cc547a4e6311c5b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Playing music at $A000 - $FFFF "behind" kernal

**Raw Source File**: `data/docs/codebase_c64_org/base/playing_music_a000-_ffff.md`
**SHA256**: `9756f73c705357ddafddd5987d6711d6ecdc18b8900a07ff7cc547a4e6311c5b`

## Summary




# Playing music at $A000 - $FFFF "behind" kernal

base:playing_music_a000-_ffff

                # Playing music at $A000 - $FFFF "behind" kernal

Ok, you saw the simple IRQ music player I added previously, now let's play some music inside the IRQ that is outside the $0400-$9fff area. How do we come about it? Well, simple really. We need to turn off the kernal (SET #$35 to $01) initialize the tune and then turn the kernal back on (SET #$37 to $01). You do the same to play the music as well. T...
