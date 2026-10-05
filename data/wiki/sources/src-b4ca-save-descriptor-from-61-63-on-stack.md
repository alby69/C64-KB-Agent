---
id: src-b4ca-save-descriptor-from-61-63-on-stack
type: source
title: 'Source Summary: save descriptor from $61-$63 on stack'
aliases:
- save descriptor from $61-$63 on stack
- b4ca-save-descriptor-from-61-63-on-stack.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b4ca-save-descriptor-from-61-63-on-stack.md
  sha256: b784c84659763f1146704d5b904dc7ffaaec2e44700468540c98e33d81d57503
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: save descriptor from $61-$63 on stack

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b4ca-save-descriptor-from-61-63-on-stack.md`
**SHA256**: `b784c84659763f1146704d5b904dc7ffaaec2e44700468540c98e33d81d57503`

## Summary



# $B4CA — save descriptor from $61-$63 on stack

## Disassemblatura
```assembly
.B4CA  A6 16    LDX $16
.B4CC  E0 22    CPX #$22
.B4CE  D0 05    BNE $B4D5
.B4D0  A2 19    LDX #$19
.B4D2  4C 37 A4 JMP $A437
.B4D5  A5 61    LDA $61
.B4D7  95 00    STA $00,X
.B4D9  A5 62    LDA $62
.B4DB  95 01    STA $01,X
.B4DD  A5 63    LDA $63
.B4DF  95 02    STA $02,X
.B4E1  A0 00    LDY #$00
.B4E3  86 64    STX $64
.B4E5  84 65    STY $65
.B4E7  84 70    STY $70
.B4E9  88       DEY
.B4EA  84 0D    STY $0D
....
