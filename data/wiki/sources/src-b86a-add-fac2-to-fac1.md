---
id: src-b86a-add-fac2-to-fac1
type: source
title: 'Source Summary: add FAC2 to FAC1'
aliases:
- add FAC2 to FAC1
- b86a-add-fac2-to-fac1.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b86a-add-fac2-to-fac1.md
  sha256: bfa26915709210514674892d88031c8ac66c0ae9b848a869ca9be67b619a5b43
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: add FAC2 to FAC1

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b86a-add-fac2-to-fac1.md`
**SHA256**: `bfa26915709210514674892d88031c8ac66c0ae9b848a869ca9be67b619a5b43`

## Summary



# $B86A — add FAC2 to FAC1

## Disassemblatura
```assembly
.B86A  D0 03    BNE $B86F   ; branch if FAC1 is not zero
.B86C  4C FC BB JMP $BBFC   ; FAC1 was zero so copy FAC2 to FAC1 and return FAC1 is non zero
.B86F  A6 70    LDX $70   ; get FAC1 rounding byte
.B871  86 56    STX $56   ; save as FAC2 rounding byte
.B873  A2 69    LDX #$69   ; set index to FAC2 exponent address
.B875  A5 69    LDA $69   ; get FAC2 exponent
.B877  A8       TAY   ; copy exponent
.B878  F0 CE    BEQ $B848   ; exit ...
