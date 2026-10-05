---
id: src-b7f7-convert-fac1-to-integer-in-temporary-integer
type: source
title: 'Source Summary: convert FAC_1 to integer in temporary integer'
aliases:
- convert FAC_1 to integer in temporary integer
- b7f7-convert-fac1-to-integer-in-temporary-integer.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b7f7-convert-fac1-to-integer-in-temporary-integer.md
  sha256: b8720da695f8eb29a99ca21de2c4b3033beb36983069084f966e597bba3c8285
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: convert FAC_1 to integer in temporary integer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b7f7-convert-fac1-to-integer-in-temporary-integer.md`
**SHA256**: `b8720da695f8eb29a99ca21de2c4b3033beb36983069084f966e597bba3c8285`

## Summary



# $B7F7 — convert FAC_1 to integer in temporary integer

## Disassemblatura
```assembly
.B7F7  A5 66    LDA $66   ; get FAC1 sign
.B7F9  30 9D    BMI $B798   ; if -ve do illegal quantity error then warm start
.B7FB  A5 61    LDA $61   ; get FAC1 exponent
.B7FD  C9 91    CMP #$91   ; compare with exponent = 2^16
.B7FF  B0 97    BCS $B798   ; if >= do illegal quantity error then warm start
.B801  20 9B BC JSR $BC9B   ; convert FAC1 floating to fixed
.B804  A5 64    LDA $64   ; get FAC1 mantissa ...
