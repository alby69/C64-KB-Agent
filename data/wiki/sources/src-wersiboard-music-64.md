---
id: src-wersiboard-music-64
type: source
title: 'Source Summary: Wersiboard Music 64'
aliases:
- Wersiboard Music 64
- wersiboard_music_64.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/wersiboard_music_64.md
  sha256: a9048aaabf39ad842c70987753fba72e8f9c904deb61aad73b80c2afab55be00
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Wersiboard Music 64

**Raw Source File**: `data/docs/codebase_c64_org/base/wersiboard_music_64.md`
**SHA256**: `a9048aaabf39ad842c70987753fba72e8f9c904deb61aad73b80c2afab55be00`

## Summary



# Wersiboard Music 64

base:wersiboard_music_64

                # Wersiboard Music 64

This is a claviature for the C64, connected through the cartridge port. It is mapped to $df00-$df06, and every key corresponds to one bit each in those seven bytes respectively, except for $df06, where only bit 0 is used. This is because the keyboard consists of (6*8)+1 keys, and therefore 6 bytes is not enough to cover all of the keys. A bit weird, but that is how we like it.

![](https://codebase.c64.org/...
