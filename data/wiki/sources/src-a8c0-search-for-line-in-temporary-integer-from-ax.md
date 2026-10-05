---
id: src-a8c0-search-for-line-in-temporary-integer-from-ax
type: source
title: 'Source Summary: search for line # in temporary integer from (AX)'
aliases:
- 'search for line # in temporary integer from (AX)'
- a8c0-search-for-line-in-temporary-integer-from-ax.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a8c0-search-for-line-in-temporary-integer-from-ax.md
  sha256: 01c2648d8f3d4d62101424ec07cba42cd69aaef9aa0141b1ef6dc73970816c30
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: search for line # in temporary integer from (AX)

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a8c0-search-for-line-in-temporary-integer-from-ax.md`
**SHA256**: `01c2648d8f3d4d62101424ec07cba42cd69aaef9aa0141b1ef6dc73970816c30`

## Summary



# $A8C0 — search for line # in temporary integer from (AX)

## Disassemblatura
```assembly
.A8C0  20 17 A6 JSR $A617   ; search Basic for temp integer line number from AX
.A8C3  90 1E    BCC $A8E3   ; if carry clear go do unsdefined statement error carry all ready set for subtract
.A8C5  A5 5F    LDA $5F   ; get pointer low byte
.A8C7  E9 01    SBC #$01   ; -1
.A8C9  85 7A    STA $7A   ; save BASIC execute pointer low byte
.A8CB  A5 60    LDA $60   ; get pointer high byte
.A8CD  E9 00    SBC #...
