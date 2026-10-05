---
id: src-a9e0-assign-to-ti
type: source
title: 'Source Summary: assign to TI$'
aliases:
- assign to TI$
- a9e0-assign-to-ti.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a9e0-assign-to-ti.md
  sha256: 88fc3580edf1120ddfaf602f29962eab027a27cf110bbc5946abf5543b1a3928
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: assign to TI$

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a9e0-assign-to-ti.md`
**SHA256**: `88fc3580edf1120ddfaf602f29962eab027a27cf110bbc5946abf5543b1a3928`

## Summary



# $A9E0 — assign to TI$

## Disassemblatura
```assembly
.A9E0  20 A6 B6 JSR $B6A6
.A9E3  C9 06    CMP #$06   ; length 6
.A9E5  D0 3D    BNE $AA24
.A9E7  A0 00    LDY #$00
.A9E9  84 61    STY $61
.A9EB  84 66    STY $66
.A9ED  84 71    STY $71
.A9EF  20 1D AA JSR $AA1D
.A9F2  20 E2 BA JSR $BAE2
.A9F5  E6 71    INC $71
.A9F7  A4 71    LDY $71
.A9F9  20 1D AA JSR $AA1D
.A9FC  20 0C BC JSR $BC0C
.A9FF  AA       TAX
.AA00  F0 05    BEQ $AA07
.AA02  E8       INX
.AA03  8A       TXA
.AA04  20 ED BA J...
