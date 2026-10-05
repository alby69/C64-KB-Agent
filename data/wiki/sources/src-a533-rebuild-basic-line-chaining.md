---
id: src-a533-rebuild-basic-line-chaining
type: source
title: 'Source Summary: rebuild BASIC line chaining'
aliases:
- rebuild BASIC line chaining
- a533-rebuild-basic-line-chaining.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a533-rebuild-basic-line-chaining.md
  sha256: 52ce7870215cd2281ed2cd8fe136010abb1042e9f56b5c97da2018763f7996c8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: rebuild BASIC line chaining

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a533-rebuild-basic-line-chaining.md`
**SHA256**: `52ce7870215cd2281ed2cd8fe136010abb1042e9f56b5c97da2018763f7996c8`

## Summary



# $A533 — rebuild BASIC line chaining

## Disassemblatura
```assembly
.A533  A5 2B    LDA $2B   ; get start of memory low byte
.A535  A4 2C    LDY $2C   ; get start of memory high byte
.A537  85 22    STA $22   ; set line start pointer low byte
.A539  84 23    STY $23   ; set line start pointer high byte
.A53B  18       CLC   ; clear carry for add
.A53C  A0 01    LDY #$01   ; set index to pointer to next line high byte
.A53E  B1 22    LDA ($22),Y   ; get pointer to next line high byte
.A540  F...
