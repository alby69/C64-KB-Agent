---
id: src-sprite-converter
type: source
title: 'Source Summary: Bitmap to sprite converter written in Python'
aliases:
- Bitmap to sprite converter written in Python
- sprite_converter.md
tags:
- sprite programming
- basic
- graphics
- assembly
sources:
- path: data/docs/codebase_c64_org/base/sprite_converter.md
  sha256: 0302b61ff0b08553a218ef8b5b7d0807ab56816f7f3d69b30ab1ea8b3b7ec60d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Bitmap to sprite converter written in Python

**Raw Source File**: `data/docs/codebase_c64_org/base/sprite_converter.md`
**SHA256**: `0302b61ff0b08553a218ef8b5b7d0807ab56816f7f3d69b30ab1ea8b3b7ec60d`

## Summary



# Bitmap to sprite converter written in Python

base:sprite_converter

                # Bitmap to sprite converter written in Python

This is a simple Python hack that converts monochrome images with a multiple of 24x21px to an array of sprites. It can save the sprites with or without load address. Public Domain.

```
#!/usr/bin/env python
# .spr converter for arbitrary sized images (multiple of 24x21)
# 1st argument: file to convert
# 2nd argument: target file
# 3rd argument: load address in...
