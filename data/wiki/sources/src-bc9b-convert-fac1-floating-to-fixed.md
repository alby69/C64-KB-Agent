---
id: src-bc9b-convert-fac1-floating-to-fixed
type: source
title: 'Source Summary: convert FAC1 floating to fixed'
aliases:
- convert FAC1 floating to fixed
- bc9b-convert-fac1-floating-to-fixed.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bc9b-convert-fac1-floating-to-fixed.md
  sha256: 17246f505e2a46605d372d3195c2468510e85ec99a52e9a823b7c6b7421232be
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: convert FAC1 floating to fixed

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bc9b-convert-fac1-floating-to-fixed.md`
**SHA256**: `17246f505e2a46605d372d3195c2468510e85ec99a52e9a823b7c6b7421232be`

## Summary



# $BC9B — convert FAC1 floating to fixed

## Disassemblatura
```assembly
.BC9B  A5 61    LDA $61   ; get FAC1 exponent
.BC9D  F0 4A    BEQ $BCE9   ; if zero go clear FAC1 and return
.BC9F  38       SEC   ; set carry for subtract
.BCA0  E9 A0    SBC #$A0   ; subtract maximum integer range exponent
.BCA2  24 66    BIT $66   ; test FAC1 sign (b7)
.BCA4  10 09    BPL $BCAF   ; branch if FAC1 +ve FAC1 was -ve
.BCA6  AA       TAX   ; copy subtracted exponent
.BCA7  A9 FF    LDA #$FF   ; overflow for...
