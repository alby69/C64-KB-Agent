---
id: src-b128-make-a-new-simple-variable
type: source
title: 'Source Summary: MAKE A NEW SIMPLE VARIABLE'
aliases:
- MAKE A NEW SIMPLE VARIABLE
- b128-make-a-new-simple-variable.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b128-make-a-new-simple-variable.md
  sha256: 81cfeafc7cfaf7d48f6c7cb150dbd03e2065381b77147aa6ed97a42d75d8dd6a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: MAKE A NEW SIMPLE VARIABLE

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b128-make-a-new-simple-variable.md`
**SHA256**: `81cfeafc7cfaf7d48f6c7cb150dbd03e2065381b77147aa6ed97a42d75d8dd6a`

## Summary



# $B128 — MAKE A NEW SIMPLE VARIABLE

## Disassemblatura
```assembly
.B128  A5 45    LDA $45
.B12A  A4 46    LDY $46
.B12C  C9 54    CMP #$54
.B12E  D0 0B    BNE $B13B
.B130  C0 C9    CPY #$C9
.B132  F0 EF    BEQ $B123
.B134  C0 49    CPY #$49
.B136  D0 03    BNE $B13B
.B138  4C 08 AF JMP $AF08
.B13B  C9 53    CMP #$53
.B13D  D0 04    BNE $B143
.B13F  C0 54    CPY #$54
.B141  F0 F5    BEQ $B138
.B143  A5 2F    LDA $2F   ; SET UP CALL TO BLTU TO
.B145  A4 30    LDY $30   ; TO MOVE FROM ARYTAB T...
