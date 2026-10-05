---
id: src-quick-vicii-screen-setup
type: source
title: 'Source Summary: Quick VIC-II Screen Setup'
aliases:
- Quick VIC-II Screen Setup
- quick_vicii_screen_setup.md
tags:
- sprite programming
- graphics
- assembly
sources:
- path: data/docs/codebase_c64_org/base/quick_vicii_screen_setup.md
  sha256: 8d3153b30cdb58865764b9960db5796bac8a0f3a02b597002c8a3a64637ba28c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Quick VIC-II Screen Setup

**Raw Source File**: `data/docs/codebase_c64_org/base/quick_vicii_screen_setup.md`
**SHA256**: `8d3153b30cdb58865764b9960db5796bac8a0f3a02b597002c8a3a64637ba28c`

## Summary




# Quick VIC-II Screen Setup

base:quick_vicii_screen_setup

                # Quick VIC-II Screen Setup

This code snippet will set the both the bank and the screen address registers, given simple pointers to screenChars and screenPixels.

 screenChars  = $0400 ; the 40x25 buffer
 screenPixels = $1000 ; the pixel data for font or bitmap ($1000 or $9000 are always charrom)
; Select VIC bank
 lda # ((screenChars ^ $ffff) >> 14)
 sta $dd00
; Set VIC screen and font pointers
 lda # (((screenChars...
