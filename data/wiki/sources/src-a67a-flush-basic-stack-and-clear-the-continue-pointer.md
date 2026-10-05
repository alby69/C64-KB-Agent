---
id: src-a67a-flush-basic-stack-and-clear-the-continue-pointer
type: source
title: 'Source Summary: flush BASIC stack and clear the continue pointer'
aliases:
- flush BASIC stack and clear the continue pointer
- a67a-flush-basic-stack-and-clear-the-continue-pointer.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a67a-flush-basic-stack-and-clear-the-continue-pointer.md
  sha256: dacc740118dd84f2e76b076b145d2a33ca24c4a8c3ed2d16b5407578c41f2178
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: flush BASIC stack and clear the continue pointer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a67a-flush-basic-stack-and-clear-the-continue-pointer.md`
**SHA256**: `dacc740118dd84f2e76b076b145d2a33ca24c4a8c3ed2d16b5407578c41f2178`

## Summary



# $A67A — flush BASIC stack and clear the continue pointer

## Disassemblatura
```assembly
.A67A  A2 19    LDX #$19   ; get the descriptor stack start
.A67C  86 16    STX $16   ; set the descriptor stack pointer
.A67E  68       PLA   ; pull the return address low byte
.A67F  A8       TAY   ; copy it
.A680  68       PLA   ; pull the return address high byte
.A681  A2 FA    LDX #$FA   ; set the cleared stack pointer
.A683  9A       TXS   ; set the stack
.A684  48       PHA   ; push the return ad...
