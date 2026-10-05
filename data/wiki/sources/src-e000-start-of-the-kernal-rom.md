---
id: src-e000-start-of-the-kernal-rom
type: source
title: 'Source Summary: start of the kernal ROM'
aliases:
- start of the kernal ROM
- e000-start-of-the-kernal-rom.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e000-start-of-the-kernal-rom.md
  sha256: 869fbed4aceac25836afebca383f3c5b0aa7f97959bb107e3787f65132c74aa2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: start of the kernal ROM

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e000-start-of-the-kernal-rom.md`
**SHA256**: `869fbed4aceac25836afebca383f3c5b0aa7f97959bb107e3787f65132c74aa2`

## Summary



# $E000 — start of the kernal ROM

## Disassemblatura
```assembly
.E000  85 56    STA $56   ; save FAC2 rounding byte
.E002  20 0F BC JSR $BC0F   ; copy FAC1 to FAC2
.E005  A5 61    LDA $61   ; get FAC1 exponent
.E007  C9 88    CMP #$88   ; compare with EXP limit (256d)
.E009  90 03    BCC $E00E   ; branch if less
.E00B  20 D4 BA JSR $BAD4   ; handle overflow and underflow
.E00E  20 CC BC JSR $BCCC   ; perform INT()
.E011  A5 07    LDA $07   ; get mantissa 4 from INT()
.E013  18       CLC   ; ...
