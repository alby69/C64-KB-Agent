---
id: src-e059-compute-polynomials-according-to-table-indexed-by-ay
type: source
title: 'Source Summary: compute polynomials according to table indexed by AY'
aliases:
- compute polynomials according to table indexed by AY
- e059-compute-polynomials-according-to-table-indexed-by-ay.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e059-compute-polynomials-according-to-table-indexed-by-ay.md
  sha256: af11d0c6a6c6404d2dd188a8247617d534358ff598fea745d0d0d236f592cdf1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: compute polynomials according to table indexed by AY

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e059-compute-polynomials-according-to-table-indexed-by-ay.md`
**SHA256**: `af11d0c6a6c6404d2dd188a8247617d534358ff598fea745d0d0d236f592cdf1`

## Summary



# $E059 — compute polynomials according to table indexed by AY

## Disassemblatura
```assembly
.E059  85 71    STA $71
.E05B  84 72    STY $72
.E05D  20 C7 BB JSR $BBC7
.E060  B1 71    LDA ($71),Y
.E062  85 67    STA $67
.E064  A4 71    LDY $71
.E066  C8       INY
.E067  98       TYA
.E068  D0 02    BNE $E06C
.E06A  E6 72    INC $72
.E06C  85 71    STA $71
.E06E  A4 72    LDY $72
.E070  20 28 BA JSR $BA28
.E073  A5 71    LDA $71
.E075  A4 72    LDY $72
.E077  18       CLC
.E078  69 05    ADC #...
