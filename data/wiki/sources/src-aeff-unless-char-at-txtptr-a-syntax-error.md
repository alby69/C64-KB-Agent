---
id: src-aeff-unless-char-at-txtptr-a-syntax-error
type: source
title: 'Source Summary: UNLESS CHAR AT TXTPTR = (A), SYNTAX ERROR'
aliases:
- UNLESS CHAR AT TXTPTR = (A), SYNTAX ERROR
- aeff-unless-char-at-txtptr-a-syntax-error.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aeff-unless-char-at-txtptr-a-syntax-error.md
  sha256: 2bcafafffdbf5b3fc661c7151a3eb5b8811187fd7cdac1a8e2ca141e2c57498f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: UNLESS CHAR AT TXTPTR = (A), SYNTAX ERROR

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/aeff-unless-char-at-txtptr-a-syntax-error.md`
**SHA256**: `2bcafafffdbf5b3fc661c7151a3eb5b8811187fd7cdac1a8e2ca141e2c57498f`

## Summary



# $AEFF — UNLESS CHAR AT TXTPTR = (A), SYNTAX ERROR

## Disassemblatura
```assembly
.AEFF  A0 00    LDY #$00
.AF01  D1 7A    CMP ($7A),Y
.AF03  D0 03    BNE $AF08
.AF05  4C 73 00 JMP $0073   ; MATCH, GET NEXT CHAR &amp; RETURN
.AF08  A2 0B    LDX #$0B
.AF0A  4C 37 A4 JMP $A437
.AF0D  A0 15    LDY #$15   ; POINT AT UNARY MINUS
.AF0F  68       PLA
.AF10  68       PLA
.AF11  4C FA AD JMP $ADFA
.AF14  38       SEC
.AF15  A5 64    LDA $64
.AF17  E9 00    SBC #$00
.AF19  A5 65    LDA $65
.AF1B  E9 A...
