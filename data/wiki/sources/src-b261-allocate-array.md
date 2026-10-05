---
id: src-b261-allocate-array
type: source
title: 'Source Summary: allocate array'
aliases:
- allocate array
- b261-allocate-array.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b261-allocate-array.md
  sha256: 7532c46ad07050328b4e2faec62b1209453092d45848a3a3f237202b1c7e114b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: allocate array

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b261-allocate-array.md`
**SHA256**: `7532c46ad07050328b4e2faec62b1209453092d45848a3a3f237202b1c7e114b`

## Summary



# $B261 — allocate array

## Disassemblatura
```assembly
.B261  20 94 B1 JSR $B194
.B264  20 08 A4 JSR $A408
.B267  A0 00    LDY #$00
.B269  84 72    STY $72
.B26B  A2 05    LDX #$05
.B26D  A5 45    LDA $45
.B26F  91 5F    STA ($5F),Y
.B271  10 01    BPL $B274
.B273  CA       DEX
.B274  C8       INY
.B275  A5 46    LDA $46
.B277  91 5F    STA ($5F),Y
.B279  10 02    BPL $B27D
.B27B  CA       DEX
.B27C  CA       DEX
.B27D  86 71    STX $71
.B27F  A5 0B    LDA $0B
.B281  C8       INY
.B282  C8  ...
