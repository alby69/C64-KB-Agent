---
id: src-a52a-clear-all-variables
type: source
title: 'Source Summary: CLEAR ALL VARIABLES'
aliases:
- CLEAR ALL VARIABLES
- a52a-clear-all-variables.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a52a-clear-all-variables.md
  sha256: f639f525817e8d1136cd758f408ee559220db5bfa79d819148ed3ef95c678a57
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: CLEAR ALL VARIABLES

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a52a-clear-all-variables.md`
**SHA256**: `f639f525817e8d1136cd758f408ee559220db5bfa79d819148ed3ef95c678a57`

## Summary



# $A52A — CLEAR ALL VARIABLES

## Disassemblatura
```assembly
.A52A  20 59 A6 JSR $A659   ; CLEAR ALL VARIABLES
.A52D  20 33 A5 JSR $A533
.A530  4C 80 A4 JMP $A480
.A533  A5 2B    LDA $2B   ; POINT INDEX AT START OF PROGRAM
.A535  A4 2C    LDY $2C
.A537  85 22    STA $22
.A539  84 23    STY $23
.A53B  18       CLC
.A53C  A0 01    LDY #$01   ; HI-BYTE OF NEXT FORWARD PNTR
.A53E  B1 22    LDA ($22),Y   ; END OF PROGRAM YET?
.A540  F0 1D    BEQ $A55F
.A542  A0 04    LDY #$04   ; FIND END OF THIS ...
