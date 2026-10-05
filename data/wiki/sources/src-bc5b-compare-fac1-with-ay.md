---
id: src-bc5b-compare-fac1-with-ay
type: source
title: 'Source Summary: compare FAC1 with (AY)'
aliases:
- compare FAC1 with (AY)
- bc5b-compare-fac1-with-ay.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bc5b-compare-fac1-with-ay.md
  sha256: db7b31e286b7cf4a2f0263aca0ca66c739418577e160a7dbac70017b6181f836
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: compare FAC1 with (AY)

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bc5b-compare-fac1-with-ay.md`
**SHA256**: `db7b31e286b7cf4a2f0263aca0ca66c739418577e160a7dbac70017b6181f836`

## Summary



# $BC5B — compare FAC1 with (AY)

## Disassemblatura
```assembly
.BC5B  85 24    STA $24   ; save pointer low byte
.BC5D  84 25    STY $25   ; save pointer high byte
.BC5F  A0 00    LDY #$00   ; clear index
.BC61  B1 24    LDA ($24),Y   ; get exponent
.BC63  C8       INY   ; increment index
.BC64  AA       TAX   ; copy (AY) exponent to X
.BC65  F0 C4    BEQ $BC2B   ; branch if (AY) exponent=0 and get FAC1 sign A = $FF, Cb = 1/-ve A = $01, Cb = 0/+ve
.BC67  B1 24    LDA ($24),Y   ; get (AY) man...
