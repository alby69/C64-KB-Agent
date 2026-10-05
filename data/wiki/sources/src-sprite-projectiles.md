---
id: src-sprite-projectiles
type: source
title: 'Source Summary: Sprite projectiles'
aliases:
- Sprite projectiles
- sprite_projectiles.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/sprite_projectiles.md
  sha256: 3bfeab80d13fdcec55cde1c32ee22837951acee7b304d6710f880fdec9ed13f5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Sprite projectiles

**Raw Source File**: `data/docs/codebase_c64_org/base/sprite_projectiles.md`
**SHA256**: `3bfeab80d13fdcec55cde1c32ee22837951acee7b304d6710f880fdec9ed13f5`

## Summary



# Sprite projectiles

base:sprite_projectiles

                # Sprite projectiles

by Achim

Here's a small piece of code to make one sprite fly directly to another one. If the player is aiming at an enemy (or vice versa), this routine will make sure the projectile hits the target.

It's using the bresenham line algorithm for all four quadrants. It only works with deltaX < $ff.

- Call “projecileslope” to prepare the line algorithm.
- Call “projectileflying” to move the projectile.

```
; ca...
