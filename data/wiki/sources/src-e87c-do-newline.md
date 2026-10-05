---
id: src-e87c-do-newline
type: source
title: 'Source Summary: do newline'
aliases:
- do newline
- e87c-do-newline.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e87c-do-newline.md
  sha256: b00bdbafae2e7cc0ca5c582c5b8a1d6593782b7a7ab2a02bd1b169d3acd0411f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: do newline

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e87c-do-newline.md`
**SHA256**: `b00bdbafae2e7cc0ca5c582c5b8a1d6593782b7a7ab2a02bd1b169d3acd0411f`

## Summary



# $E87C — do newline

## Disassemblatura
```assembly
.E87C  46 C9    LSR $C9   ; shift >> input cursor row
.E87E  A6 D6    LDX $D6   ; get the cursor row
.E880  E8       INX   ; increment the row
.E881  E0 19    CPX #$19   ; compare it with last row + 1
.E883  D0 03    BNE $E888   ; if not last row + 1 skip the screen scroll
.E885  20 EA E8 JSR $E8EA   ; else scroll the screen
.E888  B5 D9    LDA $D9,X   ; get start of line X pointer high byte
.E88A  10 F4    BPL $E880   ; loop if not start of...
