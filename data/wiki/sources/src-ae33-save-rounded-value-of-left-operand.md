---
id: src-ae33-save-rounded-value-of-left-operand
type: source
title: 'Source Summary: save rounded value of left operand'
aliases:
- save rounded value of left operand
- ae33-save-rounded-value-of-left-operand.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ae33-save-rounded-value-of-left-operand.md
  sha256: 1266dbe6fc51ae8939e093a6b1ad4f772cd66b186e77bed631ebeac805e96553
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: save rounded value of left operand

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ae33-save-rounded-value-of-left-operand.md`
**SHA256**: `1266dbe6fc51ae8939e093a6b1ad4f772cd66b186e77bed631ebeac805e96553`

## Summary



# $AE33 — save rounded value of left operand

## Disassemblatura
```assembly
.AE33  A5 66    LDA $66
.AE35  BE 80 A0 LDX $A080,Y
.AE38  A8       TAY
.AE39  68       PLA   ; pull return address
.AE3A  85 22    STA $22
.AE3C  E6 22    INC $22
.AE3E  68       PLA   ; and store in $22/$23
.AE3F  85 23    STA $23
.AE41  98       TYA
.AE42  48       PHA
.AE43  20 1B BC JSR $BC1B
.AE46  A5 65    LDA $65
.AE48  48       PHA
.AE49  A5 64    LDA $64
.AE4B  48       PHA
.AE4C  A5 63    LDA $63
.AE4E  48 ...
