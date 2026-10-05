---
id: src-e701-back-onto-the-previous-line-if-possible
type: source
title: 'Source Summary: back onto the previous line if possible'
aliases:
- back onto the previous line if possible
- e701-back-onto-the-previous-line-if-possible.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e701-back-onto-the-previous-line-if-possible.md
  sha256: a55a0c1294a9153a5895484c1558d68ce2af96941ade27b05f88a47ed86f4210
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: back onto the previous line if possible

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e701-back-onto-the-previous-line-if-possible.md`
**SHA256**: `a55a0c1294a9153a5895484c1558d68ce2af96941ade27b05f88a47ed86f4210`

## Summary



# $E701 — back onto the previous line if possible

## Disassemblatura
```assembly
.E701  A6 D6    LDX $D6   ; get the cursor row
.E703  D0 06    BNE $E70B   ; branch if not top row
.E705  86 D3    STX $D3   ; clear cursor column
.E707  68       PLA   ; dump return address low byte
.E708  68       PLA   ; dump return address high byte
.E709  D0 9D    BNE $E6A8   ; restore registers, set quote flag and exit, branch always
.E70B  CA       DEX   ; decrement the cursor row
.E70C  86 D6    STX $D6  ...
