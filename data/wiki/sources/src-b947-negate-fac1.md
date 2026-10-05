---
id: src-b947-negate-fac1
type: source
title: 'Source Summary: negate FAC1'
aliases:
- negate FAC1
- b947-negate-fac1.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b947-negate-fac1.md
  sha256: bb91f4a1f8cb5f13e520945e855c1dfc2a753484d25215a3f1a27e2e2cf60597
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: negate FAC1

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b947-negate-fac1.md`
**SHA256**: `bb91f4a1f8cb5f13e520945e855c1dfc2a753484d25215a3f1a27e2e2cf60597`

## Summary



# $B947 — negate FAC1

## Disassemblatura
```assembly
.B947  A5 66    LDA $66   ; get FAC1 sign (b7)
.B949  49 FF    EOR #$FF   ; complement it
.B94B  85 66    STA $66   ; save FAC1 sign (b7) twos complement FAC1 mantissa
.B94D  A5 62    LDA $62   ; get FAC1 mantissa 1
.B94F  49 FF    EOR #$FF   ; complement it
.B951  85 62    STA $62   ; save FAC1 mantissa 1
.B953  A5 63    LDA $63   ; get FAC1 mantissa 2
.B955  49 FF    EOR #$FF   ; complement it
.B957  85 63    STA $63   ; save FAC1 mantiss...
