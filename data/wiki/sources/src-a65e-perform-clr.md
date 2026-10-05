---
id: src-a65e-perform-clr
type: source
title: 'Source Summary: perform CLR'
aliases:
- perform CLR
- a65e-perform-clr.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a65e-perform-clr.md
  sha256: 8e0d20dcb8c5df3db2cb5e487cf91bef72bae56cfa061c397d164d9a51f721ee
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform CLR

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a65e-perform-clr.md`
**SHA256**: `8e0d20dcb8c5df3db2cb5e487cf91bef72bae56cfa061c397d164d9a51f721ee`

## Summary



# $A65E — perform CLR

## Disassemblatura
```assembly
.A65E  D0 2D    BNE $A68D   ; exit if following byte to allow syntax error
.A660  20 E7 FF JSR $FFE7   ; close all channels and files
.A663  A5 37    LDA $37   ; get end of memory low byte
.A665  A4 38    LDY $38   ; get end of memory high byte
.A667  85 33    STA $33   ; set bottom of string space low byte, clear strings
.A669  84 34    STY $34   ; set bottom of string space high byte
.A66B  A5 2D    LDA $2D   ; get start of variables low ...
