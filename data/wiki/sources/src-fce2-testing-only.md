---
id: src-fce2-testing-only
type: source
title: 'Source Summary: ; TESTING ONLY'
aliases:
- ; TESTING ONLY
- fce2-testing-only.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fce2-testing-only.md
  sha256: 074cb2169838990c4a56c0c029700ea4b8636f5156203e45e36bbfb469da4925
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ; TESTING ONLY

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fce2-testing-only.md`
**SHA256**: `074cb2169838990c4a56c0c029700ea4b8636f5156203e45e36bbfb469da4925`

## Summary



# $FCE2 — ; TESTING ONLY

## Disassemblatura
```assembly
.FCE2  A2 FF    LDX #$FF   ; START  LDX #$FF
.FCE4  78       SEI   ; SEI
.FCE5  9A       TXS   ; TXS
.FCE6  D8       CLD   ; CLD
.FCE7  20 02 FD JSR $FD02   ; JSR A0INT       ;TEST FOR $A0 ROM IN
.FCEA  D0 03    BNE $FCEF   ; BNE START1
.FCEC  6C 00 80 JMP ($8000)   ; JMP ($8000)     ; GO INIT AS $A000 ROM WANTS
.FCEF  8E 16 D0 STX $D016   ; START1 STX VICREG+22   ;SET UP REFRESH (.X=<5)
.FCF2  20 A3 FD JSR $FDA3   ; JSR IOINIT      ;GO ...
