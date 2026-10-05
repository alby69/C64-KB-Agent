---
id: src-bb12-divide-operator
type: source
title: 'Source Summary: divide operator'
aliases:
- divide operator
- bb12-divide-operator.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bb12-divide-operator.md
  sha256: af2dd12cacf8a527d7548c37be006ae6ca4009b6747ffc31b3fa8c256a035e96
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: divide operator

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bb12-divide-operator.md`
**SHA256**: `af2dd12cacf8a527d7548c37be006ae6ca4009b6747ffc31b3fa8c256a035e96`

## Summary



# $BB12 — divide operator

## Disassemblatura
```assembly
.BB12  F0 76    BEQ $BB8A
.BB14  20 1B BC JSR $BC1B
.BB17  A9 00    LDA #$00
.BB19  38       SEC
.BB1A  E5 61    SBC $61
.BB1C  85 61    STA $61
.BB1E  20 B7 BA JSR $BAB7
.BB21  E6 61    INC $61
.BB23  F0 BA    BEQ $BADF
.BB25  A2 FC    LDX #$FC
.BB27  A9 01    LDA #$01
.BB29  A4 6A    LDY $6A
.BB2B  C4 62    CPY $62
.BB2D  D0 10    BNE $BB3F
.BB2F  A4 6B    LDY $6B
.BB31  C4 63    CPY $63
.BB33  D0 0A    BNE $BB3F
.BB35  A4 6C    LDY $...
