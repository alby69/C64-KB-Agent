---
id: src-e965-open-up-a-space-on-the-screen
type: source
title: 'Source Summary: open up a space on the screen'
aliases:
- open up a space on the screen
- e965-open-up-a-space-on-the-screen.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e965-open-up-a-space-on-the-screen.md
  sha256: 6175c4fa3e487e777d424c7882a32e7a4df5abd062c7d48377c6c51e2e999f05
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: open up a space on the screen

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e965-open-up-a-space-on-the-screen.md`
**SHA256**: `6175c4fa3e487e777d424c7882a32e7a4df5abd062c7d48377c6c51e2e999f05`

## Summary



# $E965 — open up a space on the screen

## Disassemblatura
```assembly
.E965  A6 D6    LDX $D6   ; get the cursor row
.E967  E8       INX   ; increment the row
.E968  B5 D9    LDA $D9,X   ; get the start of line X pointer high byte
.E96A  10 FB    BPL $E967   ; loop if not start of logical line
.E96C  8E A5 02 STX $02A5   ; save the screen row marker
.E96F  E0 18    CPX #$18   ; compare it with the last line
.E971  F0 0E    BEQ $E981   ; if = last line go ??
.E973  90 0C    BCC $E981   ; if <...
