---
id: src-sprite-interleave
type: source
title: 'Source Summary: Sprite Interleave'
aliases:
- Sprite Interleave
- sprite_interleave.md
tags:
- sprite programming
- basic
- graphics
- assembly
sources:
- path: data/docs/codebase_c64_org/base/sprite_interleave.md
  sha256: 6d86ec647bedcdf671fbe1c44d04cbd8b2fb8f099c12febb0c496300f8e8259e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Sprite Interleave

**Raw Source File**: `data/docs/codebase_c64_org/base/sprite_interleave.md`
**SHA256**: `6d86ec647bedcdf671fbe1c44d04cbd8b2fb8f099c12febb0c496300f8e8259e`

## Summary




# Sprite Interleave

### Table of Contents

# Sprite Interleave

By Raistlin/Genesis Project

#### Intro

When using large arrays of sprites, eg. an 8×10 array, it can be tricky to do this without having gaps or glitches. Annoyingly, C64 sprites are 21 pixels tall - so it's not possible to have this array without at least one row of sprites being around a bad line - where there simply aren't enough cycles to update all the sprite values.

![](https://codebase.c64.org/lib/exe/fetch.php?media=b...
