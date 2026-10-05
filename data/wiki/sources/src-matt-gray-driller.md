---
id: src-matt-gray-driller
type: source
title: 'Source Summary: Disassembly of Matt Gray''s "Driller"'
aliases:
- Disassembly of Matt Gray's "Driller"
- matt_gray_-_driller.md
tags:
- raster interrupts
- assembly
sources:
- path: data/docs/codebase_c64_org/base/matt_gray_-_driller.md
  sha256: 397f8ceb87561362584cf7252256f393a2050599e1a486c8f3f677dc0b76412b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Disassembly of Matt Gray's "Driller"

**Raw Source File**: `data/docs/codebase_c64_org/base/matt_gray_-_driller.md`
**SHA256**: `397f8ceb87561362584cf7252256f393a2050599e1a486c8f3f677dc0b76412b`

## Summary




# Disassembly of Matt Gray's "Driller"

base:matt_gray_-_driller

                # Disassembly of Matt Gray's "Driller"

```
; da65 V2.12.9 - (C) Copyright 2000-2005,  Ullrich von Bassewitz
; Created:    2009-04-01 09:43:40
; Input	file: Matt_Gray-Driller.prg
track_ptr	= $FB
pattern_ptr	= $FD
play_voice:
	lda	tune_ctrl			; 0900
	bne	is_playing			; 0903
	sta	$D418				; 0905
	rts					; 0908
is_playing:
	cmp	#$AB				; 0909  +
	beq	continue_playing		; 090B
	jmp	change_tune			; 090D
reset_voices:...
