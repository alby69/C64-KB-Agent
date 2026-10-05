---
id: src-e5a0-initialise-the-vic-chip
type: source
title: 'Source Summary: initialise the vic chip'
aliases:
- initialise the vic chip
- e5a0-initialise-the-vic-chip.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e5a0-initialise-the-vic-chip.md
  sha256: 14ce65efbac65193129907383bcc8588689fcb1678ca8c46047c4fd4c165cc52
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: initialise the vic chip

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e5a0-initialise-the-vic-chip.md`
**SHA256**: `14ce65efbac65193129907383bcc8588689fcb1678ca8c46047c4fd4c165cc52`

## Summary



# $E5A0 — initialise the vic chip

## Disassemblatura
```assembly
.E5A0  A9 03    LDA #$03   ; set the screen as the output device
.E5A2  85 9A    STA $9A   ; save the output device number
.E5A4  A9 00    LDA #$00   ; set the keyboard as the input device
.E5A6  85 99    STA $99   ; save the input device number
.E5A8  A2 2F    LDX #$2F   ; set the count/index
.E5AA  BD B8 EC LDA $ECB8,X   ; get a vic ii chip initialisation value
.E5AD  9D FF CF STA $CFFF,X   ; save it to the vic ii chip
.E5B0  ...
