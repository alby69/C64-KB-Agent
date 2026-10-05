---
id: src-b39e-perform-pos
type: source
title: 'Source Summary: perform POS()'
aliases:
- perform POS()
- b39e-perform-pos.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b39e-perform-pos.md
  sha256: 546ef0b83b3a39ce241a72a4a17b8e0586f5f66e82532e50eaf1d02690b3352d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform POS()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b39e-perform-pos.md`
**SHA256**: `546ef0b83b3a39ce241a72a4a17b8e0586f5f66e82532e50eaf1d02690b3352d`

## Summary



# $B39E — perform POS()

## Disassemblatura
```assembly
.B39E  38       SEC   ; set Cb for read cursor position
.B39F  20 F0 FF JSR $FFF0   ; read/set X,Y cursor position
.B3A2  A9 00    LDA #$00   ; clear high byte
.B3A4  F0 EB    BEQ $B391   ; convert fixed integer AY to float FAC1, branch always check not Direct, used by DEF and INPUT
.B3A6  A6 3A    LDX $3A   ; get current line number high byte
.B3A8  E8       INX   ; increment it
.B3A9  D0 A0    BNE $B34B   ; return if not direct mode els...
