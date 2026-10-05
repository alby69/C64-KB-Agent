---
id: src-a831-perform-end
type: source
title: 'Source Summary: perform END'
aliases:
- perform END
- a831-perform-end.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a831-perform-end.md
  sha256: 330ed03b065f46435df0d61b6b9acb37c3a78b5eb9906d8db65321abf0bc09f9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform END

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a831-perform-end.md`
**SHA256**: `330ed03b065f46435df0d61b6b9acb37c3a78b5eb9906d8db65321abf0bc09f9`

## Summary



# $A831 — perform END

## Disassemblatura
```assembly
.A831  18       CLC   ; clear carry
.A832  D0 3C    BNE $A870   ; return if wasn't CTRL-C
.A834  A5 7A    LDA $7A   ; get BASIC execute pointer low byte
.A836  A4 7B    LDY $7B   ; get BASIC execute pointer high byte
.A838  A6 3A    LDX $3A   ; get current line number high byte
.A83A  E8       INX   ; increment it
.A83B  F0 0C    BEQ $A849   ; branch if was immediate mode
.A83D  85 3D    STA $3D   ; save continue pointer low byte
.A83F  84 ...
