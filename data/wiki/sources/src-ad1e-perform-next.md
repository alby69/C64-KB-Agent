---
id: src-ad1e-perform-next
type: source
title: 'Source Summary: perform NEXT'
aliases:
- perform NEXT
- ad1e-perform-next.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ad1e-perform-next.md
  sha256: f912093356b9d7e1d63cc497e9527eeeadcc8c1d84a75ca0c74bda38e6ae5ee2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform NEXT

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ad1e-perform-next.md`
**SHA256**: `f912093356b9d7e1d63cc497e9527eeeadcc8c1d84a75ca0c74bda38e6ae5ee2`

## Summary



# $AD1E — perform NEXT

## Disassemblatura
```assembly
.AD1E  D0 04    BNE $AD24   ; branch if NEXT variable
.AD20  A0 00    LDY #$00   ; else clear Y
.AD22  F0 03    BEQ $AD27   ; branch always NEXT variable
.AD24  20 8B B0 JSR $B08B   ; get variable address
.AD27  85 49    STA $49   ; save FOR/NEXT variable pointer low byte
.AD29  84 4A    STY $4A   ; save FOR/NEXT variable pointer high byte (high byte cleared if no variable defined)
.AD2B  20 8A A3 JSR $A38A   ; search the stack for FOR or ...
