---
id: src-bbfc-copy-fac2-to-fac1
type: source
title: 'Source Summary: copy FAC2 to FAC1'
aliases:
- copy FAC2 to FAC1
- bbfc-copy-fac2-to-fac1.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bbfc-copy-fac2-to-fac1.md
  sha256: b092c40aa1f8cc1fbc692db5f77a367a9514e74f87e828da4af50a2be3fb3966
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: copy FAC2 to FAC1

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bbfc-copy-fac2-to-fac1.md`
**SHA256**: `b092c40aa1f8cc1fbc692db5f77a367a9514e74f87e828da4af50a2be3fb3966`

## Summary



# $BBFC — copy FAC2 to FAC1

## Disassemblatura
```assembly
.BBFC  A5 6E    LDA $6E   ; get FAC2 sign (b7) save FAC1 sign and copy ABS(FAC2) to FAC1
.BBFE  85 66    STA $66   ; save FAC1 sign (b7)
.BC00  A2 05    LDX #$05   ; 5 bytes to copy
.BC02  B5 68    LDA $68,X   ; get byte from FAC2,X
.BC04  95 60    STA $60,X   ; save byte at FAC1,X
.BC06  CA       DEX   ; decrement count
.BC07  D0 F9    BNE $BC02   ; loop if not all done
.BC09  86 70    STX $70   ; clear FAC1 rounding byte
.BC0B  60  ...
