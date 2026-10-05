---
id: src-aebd-print-string-to-string-utility-area
type: source
title: 'Source Summary: print "..." string to string utility area'
aliases:
- print "..." string to string utility area
- aebd-print-string-to-string-utility-area.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aebd-print-string-to-string-utility-area.md
  sha256: e552a6a7820bb8d2c7f03390e7cb8b55a791c0eac6b5fe067a86ae2dd793f715
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: print "..." string to string utility area

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/aebd-print-string-to-string-utility-area.md`
**SHA256**: `e552a6a7820bb8d2c7f03390e7cb8b55a791c0eac6b5fe067a86ae2dd793f715`

## Summary



# $AEBD — print "..." string to string utility area

## Disassemblatura
```assembly
.AEBD  A5 7A    LDA $7A   ; get BASIC execute pointer low byte
.AEBF  A4 7B    LDY $7B   ; get BASIC execute pointer high byte
.AEC1  69 00    ADC #$00   ; add carry to low byte
.AEC3  90 01    BCC $AEC6   ; branch if no overflow
.AEC5  C8       INY   ; increment high byte
.AEC6  20 87 B4 JSR $B487   ; print " terminated string to utility pointer
.AEC9  4C E2 B7 JMP $B7E2   ; restore BASIC execute pointer from ...
