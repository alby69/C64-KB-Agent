---
id: src-tiny-a-to-ascii-routine
type: source
title: 'Source Summary: Tiny .A to ASCII routine'
aliases:
- Tiny .A to ASCII routine
- tiny__a_to_ascii_routine.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/tiny__a_to_ascii_routine.md
  sha256: f7d71066ed51185f60f628232d335a4485f7e7755ff8894a5a322b95dea6202b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Tiny .A to ASCII routine

**Raw Source File**: `data/docs/codebase_c64_org/base/tiny__a_to_ascii_routine.md`
**SHA256**: `f7d71066ed51185f60f628232d335a4485f7e7755ff8894a5a322b95dea6202b`

## Summary



# Tiny .A to ASCII routine

base:tiny_.a_to_ascii_routine

                # Tiny .A to ASCII routine

From somebody in comp.sys.cbm, don't remember who nor if I tweaked it further to get this version. The thread was probably “Converting An 8-bit Number Into A String”, but I couldn't find it in Google.

Converts .A to 3 ASCII/PETSCII digits: .Y = hundreds, .X = tens, .A = ones

  ldy #$2f
  ldx #$3a
  sec
- iny
  sbc #100
  bcs -
- dex
  adc #10
  bmi -
  adc #$2f
  rts

Converts .A to 2 ASCII...
