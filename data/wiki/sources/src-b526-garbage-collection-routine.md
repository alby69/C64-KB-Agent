---
id: src-b526-garbage-collection-routine
type: source
title: 'Source Summary: garbage collection routine'
aliases:
- garbage collection routine
- b526-garbage-collection-routine.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b526-garbage-collection-routine.md
  sha256: d6a93db3114ac729c356c61b1db804bed875f04aac4c002d93bc883462319f28
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: garbage collection routine

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b526-garbage-collection-routine.md`
**SHA256**: `d6a93db3114ac729c356c61b1db804bed875f04aac4c002d93bc883462319f28`

## Summary



# $B526 — garbage collection routine

## Disassemblatura
```assembly
.B526  A6 37    LDX $37   ; get end of memory low byte
.B528  A5 38    LDA $38   ; get end of memory high byte re-run routine from last ending
.B52A  86 33    STX $33   ; set bottom of string space low byte
.B52C  85 34    STA $34   ; set bottom of string space high byte
.B52E  A0 00    LDY #$00   ; clear index
.B530  84 4F    STY $4F   ; clear working pointer high byte
.B532  84 4E    STY $4E   ; clear working pointer low by...
