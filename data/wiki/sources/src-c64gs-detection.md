---
id: src-c64gs-detection
type: source
title: 'Source Summary: base:c64gs_detection [Codebase64 wiki]'
aliases:
- base:c64gs_detection [Codebase64 wiki]
- c64gs_detection.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/c64gs_detection.md
  sha256: f56e5d3b7c42baf0696d8dacfece96f95df7ca61bb313c9b1d66e15463a5ccf9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:c64gs_detection [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/c64gs_detection.md`
**SHA256**: `f56e5d3b7c42baf0696d8dacfece96f95df7ca61bb313c9b1d66e15463a5ccf9`

## Summary



# base:c64gs_detection [Codebase64 wiki]

base:c64gs_detection

                ## C64 Game System (C64GS) detection

If you're developing a cartridge-based game and want to setup the controls differently on C64GS (since it doesn't have any physical keyboard), here is how to detect it.

```
check_c64gs			; returns 1 in x-register if true, otherwise 0.
                lda $01		; save $01 temporarily
                pha
		lda #$36	; kernal will now be visible at $e000
		sta $01
		ldx #$00
		lda ...
