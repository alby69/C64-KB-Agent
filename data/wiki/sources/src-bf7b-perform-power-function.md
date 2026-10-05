---
id: src-bf7b-perform-power-function
type: source
title: 'Source Summary: perform power function'
aliases:
- perform power function
- bf7b-perform-power-function.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bf7b-perform-power-function.md
  sha256: 89bfa8b339fcac58650313a3aec626ec142e9ed2f09ca7b4b047089c800f553d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform power function

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bf7b-perform-power-function.md`
**SHA256**: `89bfa8b339fcac58650313a3aec626ec142e9ed2f09ca7b4b047089c800f553d`

## Summary



# $BF7B — perform power function

## Disassemblatura
```assembly
.BF7B  F0 70    BEQ $BFED   ; perform EXP()
.BF7D  A5 69    LDA $69   ; get FAC2 exponent
.BF7F  D0 03    BNE $BF84   ; branch if FAC2<>0
.BF81  4C F9 B8 JMP $B8F9   ; clear FAC1 exponent and sign and return
.BF84  A2 4E    LDX #$4E   ; set destination pointer low byte
.BF86  A0 00    LDY #$00   ; set destination pointer high byte
.BF88  20 D4 BB JSR $BBD4   ; pack FAC1 into (XY)
.BF8B  A5 6E    LDA $6E   ; get FAC2 sign (b7)
.BF...
