---
id: src-merge-char-bullets
type: source
title: 'Source Summary: Merge char bullets with background chars'
aliases:
- Merge char bullets with background chars
- merge_char_bullets.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/merge_char_bullets.md
  sha256: 5d8072f125f04bb28dc59aa49ddd16e44f4b7633a777c631832a4ff68a3aebfa
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Merge char bullets with background chars

**Raw Source File**: `data/docs/codebase_c64_org/base/merge_char_bullets.md`
**SHA256**: `5d8072f125f04bb28dc59aa49ddd16e44f4b7633a777c631832a4ff68a3aebfa`

## Summary




# Merge char bullets with background chars

# Merge char bullets with background chars

by Achim

Char bullets look quite ugly when flying around. A way to achieve a more aesthetic look is to generate new chars on the fly everytime the bullet's moving one char ahead.

First thing to do is to reserve as many empty chars in your charset as you need bullets in your game.

For example 8 chars:

charset:	$2000-$2800
8 empty chars:	$27c0, $27c8, $27d0, $27d8, $27e0, $27e8, $27f0, $27f8
char values:...
