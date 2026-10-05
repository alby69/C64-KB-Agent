---
id: src-aa2c-assign-value-to-numeric-variable-but-not-ti
type: source
title: 'Source Summary: assign value to numeric variable, but not TI$'
aliases:
- assign value to numeric variable, but not TI$
- aa2c-assign-value-to-numeric-variable-but-not-ti.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aa2c-assign-value-to-numeric-variable-but-not-ti.md
  sha256: 89e142121216ba015e083f802e8d4c0f403f123cd1b1ed66c82549c2ead72c78
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: assign value to numeric variable, but not TI$

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/aa2c-assign-value-to-numeric-variable-but-not-ti.md`
**SHA256**: `89e142121216ba015e083f802e8d4c0f403f123cd1b1ed66c82549c2ead72c78`

## Summary



# $AA2C — assign value to numeric variable, but not TI$

## Disassemblatura
```assembly
.AA2C  A0 02    LDY #$02   ; index to string pointer high byte
.AA2E  B1 64    LDA ($64),Y   ; get string pointer high byte
.AA30  C5 34    CMP $34   ; compare with bottom of string space high byte
.AA32  90 17    BCC $AA4B   ; branch if string pointer high byte is less than bottom of string space high byte
.AA34  D0 07    BNE $AA3D   ; branch if string pointer high byte is greater than bottom of string spa...
