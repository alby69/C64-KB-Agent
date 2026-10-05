---
id: src-a49c-handle-new-basic-line
type: source
title: 'Source Summary: handle new BASIC line'
aliases:
- handle new BASIC line
- a49c-handle-new-basic-line.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a49c-handle-new-basic-line.md
  sha256: 7263498070beae6e4730a124acf0f52f002609c32856a950d0660584f7ae377b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: handle new BASIC line

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a49c-handle-new-basic-line.md`
**SHA256**: `7263498070beae6e4730a124acf0f52f002609c32856a950d0660584f7ae377b`

## Summary



# $A49C — handle new BASIC line

## Disassemblatura
```assembly
.A49C  20 6B A9 JSR $A96B   ; get fixed-point number into temporary integer
.A49F  20 79 A5 JSR $A579   ; crunch keywords into BASIC tokens
.A4A2  84 0B    STY $0B   ; save index pointer to end of crunched line
.A4A4  20 13 A6 JSR $A613   ; search BASIC for temporary integer line number
.A4A7  90 44    BCC $A4ED   ; if not found skip the line delete line # already exists so delete it
.A4A9  A0 01    LDY #$01   ; set index to next ...
