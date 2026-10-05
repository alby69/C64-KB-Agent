---
id: src-b7ad-perform-val
type: source
title: 'Source Summary: perform VAL()'
aliases:
- perform VAL()
- b7ad-perform-val.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b7ad-perform-val.md
  sha256: f91133413573a5a9ffa48619094d64c28d651d6afd8852cc27fda2f68a36cf6d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform VAL()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b7ad-perform-val.md`
**SHA256**: `f91133413573a5a9ffa48619094d64c28d651d6afd8852cc27fda2f68a36cf6d`

## Summary



# $B7AD — perform VAL()

## Disassemblatura
```assembly
.B7AD  20 82 B7 JSR $B782   ; evaluate string, get length in A (and Y)
.B7B0  D0 03    BNE $B7B5   ; branch if not null string string was null so set result = $00
.B7B2  4C F7 B8 JMP $B8F7   ; clear FAC1 exponent and sign and return
.B7B5  A6 7A    LDX $7A   ; get BASIC execute pointer low byte
.B7B7  A4 7B    LDY $7B   ; get BASIC execute pointer high byte
.B7B9  86 71    STX $71   ; save BASIC execute pointer low byte
.B7BB  84 72    ST...
