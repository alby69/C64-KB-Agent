---
id: src-sprite-mirror
type: source
title: 'Source Summary: base:sprite_mirror [Codebase64 wiki]'
aliases:
- base:sprite_mirror [Codebase64 wiki]
- sprite_mirror.md
tags:
- sprite programming
- assembly
- graphics
- memory management
sources:
- path: data/docs/codebase_c64_org/base/sprite_mirror.md
  sha256: 4f9fece11cf74c788df027e44b8e89f300dd2376bc3061c9c39da479ba9b83aa
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:sprite_mirror [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/sprite_mirror.md`
**SHA256**: `4f9fece11cf74c788df027e44b8e89f300dd2376bc3061c9c39da479ba9b83aa`

## Summary



# base:sprite_mirror [Codebase64 wiki]

base:sprite_mirror

                ## Sprite Mirror

Sometimes 16Kb are not enough to contain all the frames of your animations. A common trick used by many games, such as Impossible Mission, is to mirror sprites horizontally at runtime so that only the frames for the main character facing one direction must be stored at any time. This is a simple routine in Kick Assembler that flips a sprite horizontally. If source and destination sprites are the same,...
