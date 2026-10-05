---
id: src-bde7-str-function-enters-here-with-y0
type: source
title: 'Source Summary: "STR$" FUNCTION ENTERS HERE, WITH (Y)=0'
aliases:
- '"STR$" FUNCTION ENTERS HERE, WITH (Y)=0'
- bde7-str-function-enters-here-with-y0.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bde7-str-function-enters-here-with-y0.md
  sha256: 00a9db79f0a65067bd524f086fbd615237860d9950de14780bc771fabe3c28d9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: "STR$" FUNCTION ENTERS HERE, WITH (Y)=0

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bde7-str-function-enters-here-with-y0.md`
**SHA256**: `00a9db79f0a65067bd524f086fbd615237860d9950de14780bc771fabe3c28d9`

## Summary



# $BDE7 — "STR$" FUNCTION ENTERS HERE, WITH (Y)=0

## Disassemblatura
```assembly
.BDE7  99 FF 00 STA $00FF,Y   ; EMIT "-"
.BDEA  85 66    STA $66   ; MAKE FAC.SIGN POSITIVE ($2D)
.BDEC  84 71    STY $71   ; SAVE STRING PNTR
.BDEE  C8       INY
.BDEF  A9 30    LDA #$30   ; IN CASE (FAC)=0
.BDF1  A6 61    LDX $61   ; NUMBER=0?
.BDF3  D0 03    BNE $BDF8   ; NO, (FAC) NOT ZERO
.BDF5  4C 04 BF JMP $BF04   ; YES, FINISHED
.BDF8  A9 00    LDA #$00   ; STARTING VALUE FOR TMPEXP
.BDFA  E0 80    CPX #$...
