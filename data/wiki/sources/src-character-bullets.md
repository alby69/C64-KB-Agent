---
id: src-character-bullets
type: source
title: 'Source Summary: Character bullets'
aliases:
- Character bullets
- character_bullets.md
tags:
- sprite programming
- assembly
- basic
- input handling
sources:
- path: data/docs/codebase_c64_org/base/character_bullets.md
  sha256: 5869b86cebfeb17be9cf21a86aa4da15d0920c2aac2a58f2f2d6aa6f4124f1fa
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Character bullets

**Raw Source File**: `data/docs/codebase_c64_org/base/character_bullets.md`
**SHA256**: `5869b86cebfeb17be9cf21a86aa4da15d0920c2aac2a58f2f2d6aa6f4124f1fa`

## Summary




# Character bullets

### Table of Contents

# Character bullets

by Achim

Here're a few basic ideas on how to handle character bullets. Using character bullets is a bit annoying, but it's the easiest way to save sprites.

## Preperation

First thing to do is to set up a lookup table that holds the screen addresses for each screen row. This will make the movements a lot easier.

;create lookup table for screen rows
					
	lda #$00
	sta tmp0		;zp address
	sta tmp0+1		;zp address+1
						
	sta ...
