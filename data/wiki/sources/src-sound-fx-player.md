---
id: src-sound-fx-player
type: source
title: 'Source Summary: Sound Fx Player'
aliases:
- Sound Fx Player
- sound_fx_player.md
tags:
- raster interrupts
- sound generation
- assembly
sources:
- path: data/docs/codebase_c64_org/base/sound_fx_player.md
  sha256: c003c4dde6ff9bb225288bb636f32e0c57801276b61912e11ae045183915f1dc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Sound Fx Player

**Raw Source File**: `data/docs/codebase_c64_org/base/sound_fx_player.md`
**SHA256**: `c003c4dde6ff9bb225288bb636f32e0c57801276b61912e11ae045183915f1dc`

## Summary




# Sound Fx Player

base:sound_fx_player

                # Sound Fx Player

By Malcolm Bamber

Sourcecode available here: [soundfx.zip](https://codebase.c64.org/lib/exe/fetch.php?media=base:soundfx.zip)

```
; PLAYSOUND FX	
; MALCOLM BAMBER
; CODE IN C64ASM  			
* = $0800 
.byte $00,$0c,$08,$0a,$00,$9e,$31,$36,$35,$30,$30,$00,$00,$00,$00
* = 16500    
	sid	= $D400
	raster = 50
	lda #$0f
	sta $d418     ; Select Filter Mode and Volume
	lda #1
	sta 649       ; disable keyboard buffering
	lda #0
...
