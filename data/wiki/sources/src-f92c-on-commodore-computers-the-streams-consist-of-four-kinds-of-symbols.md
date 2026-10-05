---
id: src-f92c-on-commodore-computers-the-streams-consist-of-four-kinds-of-symbols
type: source
title: 'Source Summary: On Commodore computers, the streams consist of four kinds
  of symbols'
aliases:
- On Commodore computers, the streams consist of four kinds of symbols
- f92c-on-commodore-computers-the-streams-consist-of-four-kinds-of-symbols.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f92c-on-commodore-computers-the-streams-consist-of-four-kinds-of-symbols.md
  sha256: d65e5c6a1d0f51c4f6bb4e9bda1b5aeeaf5d2bd3936c67486670e5462249e9a7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: On Commodore computers, the streams consist of four kinds of symbols

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f92c-on-commodore-computers-the-streams-consist-of-four-kinds-of-symbols.md`
**SHA256**: `d65e5c6a1d0f51c4f6bb4e9bda1b5aeeaf5d2bd3936c67486670e5462249e9a7`

## Summary



# $F92C — On Commodore computers, the streams consist of four kinds of symbols

## Disassemblatura
```assembly
.F92C  AE 07 DC LDX $DC07   ; read VIA 1 timer B high byte
.F92F  A0 FF    LDY #$FF   ; set $FF
.F931  98       TYA   ; A = $FF
.F932  ED 06 DC SBC $DC06   ; subtract VIA 1 timer B low byte
.F935  EC 07 DC CPX $DC07   ; compare it with VIA 1 timer B high byte
.F938  D0 F2    BNE $F92C   ; if timer low byte rolled over loop
.F93A  86 B1    STX $B1   ; save tape timing constant max byte...
