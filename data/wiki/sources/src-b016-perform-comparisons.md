---
id: src-b016-perform-comparisons
type: source
title: 'Source Summary: perform comparisons'
aliases:
- perform comparisons
- b016-perform-comparisons.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b016-perform-comparisons.md
  sha256: ca61b6de481ceda755ed1d7cf50fdc50b5f052e7f039c9fc1d2d0829c42b3c49
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform comparisons

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b016-perform-comparisons.md`
**SHA256**: `ca61b6de481ceda755ed1d7cf50fdc50b5f052e7f039c9fc1d2d0829c42b3c49`

## Summary



# $B016 — perform comparisons

## Disassemblatura
```assembly
.B016  20 90 AD JSR $AD90   ; type match check, set C for string
.B019  B0 13    BCS $B02E   ; branch if string do numeric < compare
.B01B  A5 6E    LDA $6E   ; get FAC2 sign (b7)
.B01D  09 7F    ORA #$7F   ; set all non sign bits
.B01F  25 6A    AND $6A   ; and FAC2 mantissa 1 (AND in sign bit)
.B021  85 6A    STA $6A   ; save FAC2 mantissa 1
.B023  A9 69    LDA #$69   ; set pointer low byte to FAC2
.B025  A0 00    LDY #$00   ; set...
