---
id: src-b11d-variable-not-found
type: source
title: 'Source Summary: variable not found'
aliases:
- variable not found
- b11d-variable-not-found.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b11d-variable-not-found.md
  sha256: ff9ee0a5b2c191240ae2ecf6a2f76c47c641772e4a1a2a868968f035e02291e7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: variable not found

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b11d-variable-not-found.md`
**SHA256**: `ff9ee0a5b2c191240ae2ecf6a2f76c47c641772e4a1a2a868968f035e02291e7`

## Summary



# $B11D — variable not found

## Disassemblatura
```assembly
.B11D  68       PLA
.B11E  48       PHA
.B11F  C9 2A    CMP #$2A
.B121  D0 05    BNE $B128
.B123  A9 13    LDA #$13
.B125  A0 BF    LDY #$BF
.B127  60       RTS
.B128  A5 45    LDA $45
.B12A  A4 46    LDY $46
.B12C  C9 54    CMP #$54   ; T
.B12E  D0 0B    BNE $B13B
.B130  C0 C9    CPY #$C9   ; I$
.B132  F0 EF    BEQ $B123
.B134  C0 49    CPY #$49   ; I
.B136  D0 03    BNE $B13B
.B138  4C 08 AF JMP $AF08
.B13B  C9 53    CMP #$53   ; S...
