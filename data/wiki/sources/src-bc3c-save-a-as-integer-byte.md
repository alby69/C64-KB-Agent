---
id: src-bc3c-save-a-as-integer-byte
type: source
title: 'Source Summary: save A as integer byte'
aliases:
- save A as integer byte
- bc3c-save-a-as-integer-byte.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bc3c-save-a-as-integer-byte.md
  sha256: 1f39a6e445e2a8d891b4ee5ebe3a5cd00d2a8b2f934cc1d078a66b86fa7d7f01
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: save A as integer byte

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bc3c-save-a-as-integer-byte.md`
**SHA256**: `1f39a6e445e2a8d891b4ee5ebe3a5cd00d2a8b2f934cc1d078a66b86fa7d7f01`

## Summary



# $BC3C — save A as integer byte

## Disassemblatura
```assembly
.BC3C  85 62    STA $62   ; save FAC1 mantissa 1
.BC3E  A9 00    LDA #$00   ; clear A
.BC40  85 63    STA $63   ; clear FAC1 mantissa 2
.BC42  A2 88    LDX #$88   ; set exponent set exponent = X, clear FAC1 3 and 4 and normalise
.BC44  A5 62    LDA $62   ; get FAC1 mantissa 1
.BC46  49 FF    EOR #$FF   ; complement it
.BC48  2A       ROL   ; sign bit into carry set exponent = X, clear mantissa 4 and 3 and normalise FAC1
.BC49  A9...
