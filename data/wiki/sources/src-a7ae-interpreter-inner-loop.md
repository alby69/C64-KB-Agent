---
id: src-a7ae-interpreter-inner-loop
type: source
title: 'Source Summary: interpreter inner loop'
aliases:
- interpreter inner loop
- a7ae-interpreter-inner-loop.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a7ae-interpreter-inner-loop.md
  sha256: 4219d05ce03c476bcdc4ac265f4a51c5e9e9693c66315ee941e98d0803faaf1a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: interpreter inner loop

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a7ae-interpreter-inner-loop.md`
**SHA256**: `4219d05ce03c476bcdc4ac265f4a51c5e9e9693c66315ee941e98d0803faaf1a`

## Summary



# $A7AE — interpreter inner loop

## Disassemblatura
```assembly
.A7AE  20 2C A8 JSR $A82C   ; do CRTL-C check vector
.A7B1  A5 7A    LDA $7A   ; get the BASIC execute pointer low byte
.A7B3  A4 7B    LDY $7B   ; get the BASIC execute pointer high byte
.A7B5  C0 02    CPY #$02   ; compare the high byte with $02xx
.A7B7  EA       NOP   ; unused byte
.A7B8  F0 04    BEQ $A7BE   ; if immediate mode skip the continue pointer save
.A7BA  85 3D    STA $3D   ; save the continue pointer low byte
.A7BC...
