---
id: src-a742-perform-for
type: source
title: 'Source Summary: perform FOR'
aliases:
- perform FOR
- a742-perform-for.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a742-perform-for.md
  sha256: 75f4dbe70d30c2b7cfcf8c4b243f0f328f71ded165076ad53354c8f07753fb69
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform FOR

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a742-perform-for.md`
**SHA256**: `75f4dbe70d30c2b7cfcf8c4b243f0f328f71ded165076ad53354c8f07753fb69`

## Summary



# $A742 — perform FOR

## Disassemblatura
```assembly
.A742  A9 80    LDA #$80   ; set FNX
.A744  85 10    STA $10   ; set subscript/FNX flag
.A746  20 A5 A9 JSR $A9A5   ; perform LET
.A749  20 8A A3 JSR $A38A   ; search the stack for FOR or GOSUB activity
.A74C  D0 05    BNE $A753   ; branch if FOR, this variable, not found FOR, this variable, was found so first we dump the old one
.A74E  8A       TXA   ; copy index
.A74F  69 0F    ADC #$0F   ; add FOR structure size-2
.A751  AA       TAX   ;...
