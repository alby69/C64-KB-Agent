---
id: src-f5ed-save
type: source
title: 'Source Summary: save'
aliases:
- save
- f5ed-save.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f5ed-save.md
  sha256: d61fd770a55b2f678801fe6f4d18517866c42dd4b8617157b878359e14f04be7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: save

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f5ed-save.md`
**SHA256**: `d61fd770a55b2f678801fe6f4d18517866c42dd4b8617157b878359e14f04be7`

## Summary



# $F5ED — save

## Disassemblatura
```assembly
.F5ED  A5 BA    LDA $BA   ; get the device number
.F5EF  D0 03    BNE $F5F4   ; if not keyboard go ?? else ..
.F5F1  4C 13 F7 JMP $F713   ; else do 'illegal device number' and return
.F5F4  C9 03    CMP #$03   ; compare device number with screen
.F5F6  F0 F9    BEQ $F5F1   ; if screen do illegal device number and return
.F5F8  90 5F    BCC $F659   ; branch if < screen is greater than screen so is serial bus
.F5FA  A9 61    LDA #$61   ; set seconda...
