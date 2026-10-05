---
id: src-a8d2-perform-return
type: source
title: 'Source Summary: perform RETURN'
aliases:
- perform RETURN
- a8d2-perform-return.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a8d2-perform-return.md
  sha256: f713ad5a3dd873afbda05ac8ca173f790b66a106254bc027b698f769f9819af0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform RETURN

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a8d2-perform-return.md`
**SHA256**: `f713ad5a3dd873afbda05ac8ca173f790b66a106254bc027b698f769f9819af0`

## Summary



# $A8D2 — perform RETURN

## Disassemblatura
```assembly
.A8D2  D0 FD    BNE $A8D1   ; exit if following token to allow syntax error
.A8D4  A9 FF    LDA #$FF   ; set byte so no match possible
.A8D6  85 4A    STA $4A   ; save FOR/NEXT variable pointer high byte
.A8D8  20 8A A3 JSR $A38A   ; search the stack for FOR or GOSUB activity, get token off stack
.A8DB  9A       TXS   ; correct the stack
.A8DC  C9 8D    CMP #$8D   ; compare with GOSUB token
.A8DE  F0 0B    BEQ $A8EB   ; if matching GOSUB...
