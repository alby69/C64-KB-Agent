---
id: src-a6c9-list-lines-from-5f60-to-1415
type: source
title: 'Source Summary: list lines from $5F/$60 to $14/$15'
aliases:
- list lines from $5F/$60 to $14/$15
- a6c9-list-lines-from-5f60-to-1415.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a6c9-list-lines-from-5f60-to-1415.md
  sha256: 8e63ba38e8e4203c8eb75348140be7cda68e18698df2ed51dd9b4cacbed024ba
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: list lines from $5F/$60 to $14/$15

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a6c9-list-lines-from-5f60-to-1415.md`
**SHA256**: `8e63ba38e8e4203c8eb75348140be7cda68e18698df2ed51dd9b4cacbed024ba`

## Summary



# $A6C9 — list lines from $5F/$60 to $14/$15

## Disassemblatura
```assembly
.A6C9  A0 01    LDY #$01
.A6CB  84 0F    STY $0F
.A6CD  B1 5F    LDA ($5F),Y
.A6CF  F0 43    BEQ $A714
.A6D1  20 2C A8 JSR $A82C
.A6D4  20 D7 AA JSR $AAD7
.A6D7  C8       INY
.A6D8  B1 5F    LDA ($5F),Y
.A6DA  AA       TAX
.A6DB  C8       INY
.A6DC  B1 5F    LDA ($5F),Y
.A6DE  C5 15    CMP $15
.A6E0  D0 04    BNE $A6E6
.A6E2  E4 14    CPX $14
.A6E4  F0 02    BEQ $A6E8
.A6E6  B0 2C    BCS $A714
.A6E8  84 49    STY $49
...
