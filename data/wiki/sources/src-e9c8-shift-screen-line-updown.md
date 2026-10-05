---
id: src-e9c8-shift-screen-line-updown
type: source
title: 'Source Summary: shift screen line up/down'
aliases:
- shift screen line up/down
- e9c8-shift-screen-line-updown.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e9c8-shift-screen-line-updown.md
  sha256: d4762d447c72f7eae1a23156399a5e2aa74486153c297004e3cb23a49ade1d40
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: shift screen line up/down

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e9c8-shift-screen-line-updown.md`
**SHA256**: `d4762d447c72f7eae1a23156399a5e2aa74486153c297004e3cb23a49ade1d40`

## Summary



# $E9C8 — shift screen line up/down

## Disassemblatura
```assembly
.E9C8  29 03    AND #$03   ; mask 0000 00xx, line memory page
.E9CA  0D 88 02 ORA $0288   ; OR with screen memory page
.E9CD  85 AD    STA $AD   ; save next/previous line pointer high byte
.E9CF  20 E0 E9 JSR $E9E0   ; calculate pointers to screen lines colour RAM
.E9D2  A0 27    LDY #$27   ; set the column count
.E9D4  B1 AC    LDA ($AC),Y   ; get character from next/previous screen line
.E9D6  91 D1    STA ($D1),Y   ; save c...
