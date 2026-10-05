---
id: src-bddd-convert-fac1-to-ascii-string-result-in-ay
type: source
title: 'Source Summary: convert FAC1 to ASCII string result in (AY)'
aliases:
- convert FAC1 to ASCII string result in (AY)
- bddd-convert-fac1-to-ascii-string-result-in-ay.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bddd-convert-fac1-to-ascii-string-result-in-ay.md
  sha256: 6c159825b2a00b776ca5c13c94e5b1a26483a309018a6b525ac4b6a97e776033
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: convert FAC1 to ASCII string result in (AY)

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bddd-convert-fac1-to-ascii-string-result-in-ay.md`
**SHA256**: `6c159825b2a00b776ca5c13c94e5b1a26483a309018a6b525ac4b6a97e776033`

## Summary



# $BDDD — convert FAC1 to ASCII string result in (AY)

## Disassemblatura
```assembly
.BDDD  A0 01    LDY #$01   ; set index = 1
.BDDF  A9 20    LDA #$20   ; character = " " (assume +ve)
.BDE1  24 66    BIT $66   ; test FAC1 sign (b7)
.BDE3  10 02    BPL $BDE7   ; branch if +ve
.BDE5  A9 2D    LDA #$2D   ; else character = "-"
.BDE7  99 FF 00 STA $00FF,Y   ; save leading character (" " or "-")
.BDEA  85 66    STA $66   ; save FAC1 sign (b7)
.BDEC  84 71    STY $71   ; save index
.BDEE  C8     ...
