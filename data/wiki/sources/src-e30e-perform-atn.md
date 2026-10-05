---
id: src-e30e-perform-atn
type: source
title: 'Source Summary: perform ATN()'
aliases:
- perform ATN()
- e30e-perform-atn.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e30e-perform-atn.md
  sha256: 9331d598167891175c75057e04a743fd15f8951878838f3a820265f56e85ca54
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform ATN()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e30e-perform-atn.md`
**SHA256**: `9331d598167891175c75057e04a743fd15f8951878838f3a820265f56e85ca54`

## Summary



# $E30E — perform ATN()

## Disassemblatura
```assembly
.E30E  A5 66    LDA $66   ; get FAC1 sign (b7)
.E310  48       PHA   ; save sign
.E311  10 03    BPL $E316   ; branch if +ve
.E313  20 B4 BF JSR $BFB4   ; else do - FAC1
.E316  A5 61    LDA $61   ; get FAC1 exponent
.E318  48       PHA   ; push exponent
.E319  C9 81    CMP #$81   ; compare with 1
.E31B  90 07    BCC $E324   ; branch if FAC1 < 1
.E31D  A9 BC    LDA #$BC   ; pointer to 1 low byte
.E31F  A0 B9    LDY #$B9   ; pointer to 1 hi...
