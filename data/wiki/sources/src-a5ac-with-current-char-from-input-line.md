---
id: src-a5ac-with-current-char-from-input-line
type: source
title: 'Source Summary: WITH CURRENT CHAR FROM INPUT LINE'
aliases:
- WITH CURRENT CHAR FROM INPUT LINE
- a5ac-with-current-char-from-input-line.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a5ac-with-current-char-from-input-line.md
  sha256: 8537895bca3b6a72f404806d7cc6d28eb1d7b46cdacc03aa8c9a2da8f7cf1f20
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: WITH CURRENT CHAR FROM INPUT LINE

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a5ac-with-current-char-from-input-line.md`
**SHA256**: `8537895bca3b6a72f404806d7cc6d28eb1d7b46cdacc03aa8c9a2da8f7cf1f20`

## Summary



# $A5AC — WITH CURRENT CHAR FROM INPUT LINE

## Disassemblatura
```assembly
.A5AC  84 71    STY $71   ; SAVE INDEX TO OUTPUT LINE
.A5AE  A0 00    LDY #$00   ; USE Y-REG WITH (FAC) TO ADDRESS TABLE
.A5B0  84 0B    STY $0B   ; HOLDS CURRENT TOKEN-$80
.A5B2  88       DEY   ; PREPARE FOR "INY" A FEW LINES DOWN
.A5B3  86 7A    STX $7A   ; SAVE POSITION IN INPUT LINE
.A5B5  CA       DEX   ; PREPARE FOR "INX" A FEW LINES DOWN
.A5B6  C8       INY   ; ADVANCE POINTER TO TOKEN TABLE
.A5B7  E8       INX
...
