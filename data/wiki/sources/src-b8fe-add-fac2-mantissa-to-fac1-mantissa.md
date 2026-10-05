---
id: src-b8fe-add-fac2-mantissa-to-fac1-mantissa
type: source
title: 'Source Summary: add FAC2 mantissa to FAC1 mantissa'
aliases:
- add FAC2 mantissa to FAC1 mantissa
- b8fe-add-fac2-mantissa-to-fac1-mantissa.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b8fe-add-fac2-mantissa-to-fac1-mantissa.md
  sha256: 3849f8fc107c88dc58a1268ea2ed776d3a6024d34fd1b619a973ad9727d9caeb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: add FAC2 mantissa to FAC1 mantissa

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b8fe-add-fac2-mantissa-to-fac1-mantissa.md`
**SHA256**: `3849f8fc107c88dc58a1268ea2ed776d3a6024d34fd1b619a973ad9727d9caeb`

## Summary



# $B8FE — add FAC2 mantissa to FAC1 mantissa

## Disassemblatura
```assembly
.B8FE  65 56    ADC $56   ; add FAC2 rounding byte
.B900  85 70    STA $70   ; save FAC1 rounding byte
.B902  A5 65    LDA $65   ; get FAC1 mantissa 4
.B904  65 6D    ADC $6D   ; add FAC2 mantissa 4
.B906  85 65    STA $65   ; save FAC1 mantissa 4
.B908  A5 64    LDA $64   ; get FAC1 mantissa 3
.B90A  65 6C    ADC $6C   ; add FAC2 mantissa 3
.B90C  85 64    STA $64   ; save FAC1 mantissa 3
.B90E  A5 63    LDA $63   ; ...
