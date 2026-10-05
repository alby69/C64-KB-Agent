---
id: src-a8a0-perform-goto
type: source
title: 'Source Summary: perform GOTO'
aliases:
- perform GOTO
- a8a0-perform-goto.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a8a0-perform-goto.md
  sha256: e6c26b0d6d0446b482f4e59ed346a59d3e71ba8093ebf840ef56473016f728c0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform GOTO

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a8a0-perform-goto.md`
**SHA256**: `e6c26b0d6d0446b482f4e59ed346a59d3e71ba8093ebf840ef56473016f728c0`

## Summary



# $A8A0 — perform GOTO

## Disassemblatura
```assembly
.A8A0  20 6B A9 JSR $A96B   ; get fixed-point number into temporary integer
.A8A3  20 09 A9 JSR $A909   ; scan for next BASIC line
.A8A6  38       SEC   ; set carry for subtract
.A8A7  A5 39    LDA $39   ; get current line number low byte
.A8A9  E5 14    SBC $14   ; subtract temporary integer low byte
.A8AB  A5 3A    LDA $3A   ; get current line number high byte
.A8AD  E5 15    SBC $15   ; subtract temporary integer high byte
.A8AF  B0 0B ...
