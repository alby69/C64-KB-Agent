---
id: src-aa52-and-descriptor-is-a-variable
type: source
title: 'Source Summary: AND DESCRIPTOR IS A VARIABLE'
aliases:
- AND DESCRIPTOR IS A VARIABLE
- aa52-and-descriptor-is-a-variable.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aa52-and-descriptor-is-a-variable.md
  sha256: f308ba0132bd03ab8e948e313b69c2e9cfe343b6e2fb9967ee92eeca7344b008
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: AND DESCRIPTOR IS A VARIABLE

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/aa52-and-descriptor-is-a-variable.md`
**SHA256**: `f308ba0132bd03ab8e948e313b69c2e9cfe343b6e2fb9967ee92eeca7344b008`

## Summary



# $AA52 — AND DESCRIPTOR IS A VARIABLE

## Disassemblatura
```assembly
.AA52  A0 00    LDY #$00   ; POINT AT LENGTH IN DESCRIPTOR
.AA54  B1 64    LDA ($64),Y   ; GET LENGTH
.AA56  20 75 B4 JSR $B475   ; MAKE A STRING THAT LONG UP ABOVE
.AA59  A5 50    LDA $50   ; SET UP SOURCE PNTR FOR MONINS
.AA5B  A4 51    LDY $51
.AA5D  85 6F    STA $6F
.AA5F  84 70    STY $70
.AA61  20 7A B6 JSR $B67A   ; MOVE STRING DATA TO NEW AREA
.AA64  A9 61    LDA #$61   ; ADDRESS OF DESCRIPTOR IS IN FAC
.AA66  A0 00...
