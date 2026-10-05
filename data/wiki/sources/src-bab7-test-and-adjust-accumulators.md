---
id: src-bab7-test-and-adjust-accumulators
type: source
title: 'Source Summary: test and adjust accumulators'
aliases:
- test and adjust accumulators
- bab7-test-and-adjust-accumulators.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bab7-test-and-adjust-accumulators.md
  sha256: c33933a0c1a2cb949436a7147177ddc6317328904499f6676df7096810bcfdb4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: test and adjust accumulators

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bab7-test-and-adjust-accumulators.md`
**SHA256**: `c33933a0c1a2cb949436a7147177ddc6317328904499f6676df7096810bcfdb4`

## Summary



# $BAB7 — test and adjust accumulators

## Disassemblatura
```assembly
.BAB7  A5 69    LDA $69   ; get FAC2 exponent
.BAB9  F0 1F    BEQ $BADA   ; branch if FAC2 = $00 (handle underflow)
.BABB  18       CLC   ; clear carry for add
.BABC  65 61    ADC $61   ; add FAC1 exponent
.BABE  90 04    BCC $BAC4   ; branch if sum of exponents < $0100
.BAC0  30 1D    BMI $BADF   ; do overflow error
.BAC2  18       CLC   ; clear carry for the add
.BAC3  2C       .BYTE $2C   ; makes next line BIT $1410
.BAC...
