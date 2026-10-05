---
id: src-e9ff-clear-screen-line-x
type: source
title: 'Source Summary: clear screen line X'
aliases:
- clear screen line X
- e9ff-clear-screen-line-x.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e9ff-clear-screen-line-x.md
  sha256: b1d7404dd17736994fecb4f4f7de4f38c6e0a9cb1cad7539d3f6a7ac652112a1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: clear screen line X

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e9ff-clear-screen-line-x.md`
**SHA256**: `b1d7404dd17736994fecb4f4f7de4f38c6e0a9cb1cad7539d3f6a7ac652112a1`

## Summary



# $E9FF — clear screen line X

## Disassemblatura
```assembly
.E9FF  A0 27    LDY #$27   ; set number of columns to clear
.EA01  20 F0 E9 JSR $E9F0   ; fetch a screen address
.EA04  20 24 EA JSR $EA24   ; calculate the pointer to colour RAM
.EA07  20 DA E4 JSR $E4DA   ; save the current colour to the colour RAM
.EA0A  A9 20    LDA #$20   ; set [SPACE]
.EA0C  91 D1    STA ($D1),Y   ; clear character in current screen line
.EA0E  88       DEY   ; decrement index
.EA0F  10 F6    BPL $EA07   ; loo...
