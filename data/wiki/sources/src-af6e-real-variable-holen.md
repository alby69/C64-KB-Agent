---
id: src-af6e-real-variable-holen
type: source
title: 'Source Summary: REAL-Variable holen'
aliases:
- REAL-Variable holen
- af6e-real-variable-holen.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/af6e-real-variable-holen.md
  sha256: 90623c611ad2a2314ac3728850bdaca57c838ea079d5a8bc618fb1e7e37f0879
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: REAL-Variable holen

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/af6e-real-variable-holen.md`
**SHA256**: `90623c611ad2a2314ac3728850bdaca57c838ea079d5a8bc618fb1e7e37f0879`

## Summary



# $AF6E — REAL-Variable holen

## Disassemblatura
```assembly
.AF6E  20 14 AF JSR $AF14   ; Descriptor im Interpreter?
.AF71  90 2D    BCC $AFA0   ; nein
.AF73  E0 54    CPX #$54   ; 'T'? (von TI)
.AF75  D0 1B    BNE $AF92   ; nein: $AF92
.AF77  C0 49    CPY #$49   ; 'I'? (von TI)
.AF79  D0 25    BNE $AFA0   ; nein: $AFA0
.AF7B  20 84 AF JSR $AF84   ; TIME in FAC holen
.AF7E  98       TYA   ; Akku =0 setzen
.AF7F  A2 A0    LDX #$A0   ; Exponentbyte für FAC
.AF81  4C 4F BC JMP $BC4F   ; FAC lin...
