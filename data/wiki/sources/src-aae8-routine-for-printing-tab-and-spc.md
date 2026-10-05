---
id: src-aae8-routine-for-printing-tab-and-spc
type: source
title: 'Source Summary: routine for printing TAB( and SPC('
aliases:
- routine for printing TAB( and SPC(
- aae8-routine-for-printing-tab-and-spc.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aae8-routine-for-printing-tab-and-spc.md
  sha256: 34d6b2f067263ce8cde8843019249f0436b3f40c018d5357b540952a504bdd18
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: routine for printing TAB( and SPC(

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/aae8-routine-for-printing-tab-and-spc.md`
**SHA256**: `34d6b2f067263ce8cde8843019249f0436b3f40c018d5357b540952a504bdd18`

## Summary



# $AAE8 — routine for printing TAB( and SPC(

## Disassemblatura
```assembly
.AAE8  38       SEC
.AAE9  20 F0 FF JSR $FFF0
.AAEC  98       TYA
.AAED  38       SEC
.AAEE  E9 0A    SBC #$0A
.AAF0  B0 FC    BCS $AAEE
.AAF2  49 FF    EOR #$FF
.AAF4  69 01    ADC #$01
.AAF6  D0 16    BNE $AB0E
.AAF8  08       PHP
.AAF9  38       SEC
.AAFA  20 F0 FF JSR $FFF0
.AAFD  84 09    STY $09
.AAFF  20 9B B7 JSR $B79B
.AB02  C9 29    CMP #$29   ; )
.AB04  D0 59    BNE $AB5F
.AB06  28       PLP
.AB07  90 06   ...
