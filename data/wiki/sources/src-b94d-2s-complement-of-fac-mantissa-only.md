---
id: src-b94d-2s-complement-of-fac-mantissa-only
type: source
title: 'Source Summary: 2''S COMPLEMENT OF FAC MANTISSA ONLY'
aliases:
- 2'S COMPLEMENT OF FAC MANTISSA ONLY
- b94d-2s-complement-of-fac-mantissa-only.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b94d-2s-complement-of-fac-mantissa-only.md
  sha256: f9f0e4e6b5918ba87bf3f01eb8b31bee973fc753748597f851b9795601829186
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 2'S COMPLEMENT OF FAC MANTISSA ONLY

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b94d-2s-complement-of-fac-mantissa-only.md`
**SHA256**: `f9f0e4e6b5918ba87bf3f01eb8b31bee973fc753748597f851b9795601829186`

## Summary



# $B94D — 2'S COMPLEMENT OF FAC MANTISSA ONLY

## Disassemblatura
```assembly
.B94D  A5 62    LDA $62
.B94F  49 FF    EOR #$FF
.B951  85 62    STA $62
.B953  A5 63    LDA $63
.B955  49 FF    EOR #$FF
.B957  85 63    STA $63
.B959  A5 64    LDA $64
.B95B  49 FF    EOR #$FF
.B95D  85 64    STA $64
.B95F  A5 65    LDA $65
.B961  49 FF    EOR #$FF
.B963  85 65    STA $65
.B965  A5 70    LDA $70
.B967  49 FF    EOR #$FF
.B969  85 70    STA $70
.B96B  E6 70    INC $70   ; START INCREMENTING MANTISSA...
