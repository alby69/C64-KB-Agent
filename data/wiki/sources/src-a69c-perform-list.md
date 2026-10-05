---
id: src-a69c-perform-list
type: source
title: 'Source Summary: perform LIST'
aliases:
- perform LIST
- a69c-perform-list.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a69c-perform-list.md
  sha256: 441a63b3bd79d0260449df9590e3f14390958ca21bafd68217302f0d8ee129e1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform LIST

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a69c-perform-list.md`
**SHA256**: `441a63b3bd79d0260449df9590e3f14390958ca21bafd68217302f0d8ee129e1`

## Summary



# $A69C — perform LIST

## Disassemblatura
```assembly
.A69C  90 06    BCC $A6A4   ; branch if next character not token (LIST n...)
.A69E  F0 04    BEQ $A6A4   ; branch if next character [NULL] (LIST)
.A6A0  C9 AB    CMP #$AB   ; compare with token for -
.A6A2  D0 E9    BNE $A68D   ; exit if not - (LIST -m) LIST [[n][-m]] this bit sets the n , if present, as the start and end
.A6A4  20 6B A9 JSR $A96B   ; get fixed-point number into temporary integer
.A6A7  20 13 A6 JSR $A613   ; search BASIC ...
