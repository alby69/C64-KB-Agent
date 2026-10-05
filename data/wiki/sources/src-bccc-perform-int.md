---
id: src-bccc-perform-int
type: source
title: 'Source Summary: perform INT()'
aliases:
- perform INT()
- bccc-perform-int.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bccc-perform-int.md
  sha256: 74acf986ffab9954e5da1a3e93035aac912dc8266bc1eb1008b06693a2158935
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform INT()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bccc-perform-int.md`
**SHA256**: `74acf986ffab9954e5da1a3e93035aac912dc8266bc1eb1008b06693a2158935`

## Summary



# $BCCC — perform INT()

## Disassemblatura
```assembly
.BCCC  A5 61    LDA $61   ; get FAC1 exponent
.BCCE  C9 A0    CMP #$A0   ; compare with max int
.BCD0  B0 20    BCS $BCF2   ; exit if >= (already int, too big for fractional part!)
.BCD2  20 9B BC JSR $BC9B   ; convert FAC1 floating to fixed
.BCD5  84 70    STY $70   ; save FAC1 rounding byte
.BCD7  A5 66    LDA $66   ; get FAC1 sign (b7)
.BCD9  84 66    STY $66   ; save FAC1 sign (b7)
.BCDB  49 80    EOR #$80   ; toggle FAC1 sign
.BCDD  ...
