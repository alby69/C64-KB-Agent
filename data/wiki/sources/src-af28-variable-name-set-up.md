---
id: src-af28-variable-name-set-up
type: source
title: 'Source Summary: variable name set-up'
aliases:
- variable name set-up
- af28-variable-name-set-up.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/af28-variable-name-set-up.md
  sha256: d18d86a09841be9a94c2e28d17d41dd20ff22148f3b03a80cd678833785a84ee
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: variable name set-up

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/af28-variable-name-set-up.md`
**SHA256**: `d18d86a09841be9a94c2e28d17d41dd20ff22148f3b03a80cd678833785a84ee`

## Summary



# $AF28 — variable name set-up

## Disassemblatura
```assembly
.AF28  20 8B B0 JSR $B08B   ; get variable address
.AF2B  85 64    STA $64   ; save variable pointer low byte
.AF2D  84 65    STY $65   ; save variable pointer high byte
.AF2F  A6 45    LDX $45   ; get current variable name first character
.AF31  A4 46    LDY $46   ; get current variable name second character
.AF33  A5 0D    LDA $0D   ; get data type flag, $FF = string, $00 = numeric
.AF35  F0 26    BEQ $AF5D   ; branch if numeric ...
