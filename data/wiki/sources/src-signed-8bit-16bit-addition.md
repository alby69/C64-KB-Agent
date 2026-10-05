---
id: src-signed-8bit-16bit-addition
type: source
title: 'Source Summary: base:signed_8bit_16bit_addition [Codebase64 wiki]'
aliases:
- base:signed_8bit_16bit_addition [Codebase64 wiki]
- signed_8bit_16bit_addition.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/signed_8bit_16bit_addition.md
  sha256: f4a9504a659d50b3977c118fd0525b984337315261d5d7753d1a213591bc7e78
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:signed_8bit_16bit_addition [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/signed_8bit_16bit_addition.md`
**SHA256**: `f4a9504a659d50b3977c118fd0525b984337315261d5d7753d1a213591bc7e78`

## Summary



# base:signed_8bit_16bit_addition [Codebase64 wiki]

base:signed_8bit_16bit_addition

                To add a signed 8-bit delta to a 16-bit value, we need to sign-extend the delta to a full 16 bits. The low byte can be added as normal, but the upper byte needs to be $00 or $ff based on the sign of the low byte.

 ; Precalculate the sign-extended high byte in .X
 ldx #$00
 lda delta
 bpl :+
  dex        ; decrement high byte to $ff for a negative delta
:
 
 ; Normal 16-bit addition
 clc
 adc ...
