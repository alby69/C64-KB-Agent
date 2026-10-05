---
id: src-b34c-xy-xa-length-limit-from-array-data
type: source
title: 'Source Summary: XY = XA = length * limit from array data'
aliases:
- XY = XA = length * limit from array data
- b34c-xy-xa-length-limit-from-array-data.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b34c-xy-xa-length-limit-from-array-data.md
  sha256: 24e92181b0b7e44a7fa7ff560efa5e53a9ba158a82a41713811b0ad05f36fdc8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: XY = XA = length * limit from array data

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b34c-xy-xa-length-limit-from-array-data.md`
**SHA256**: `24e92181b0b7e44a7fa7ff560efa5e53a9ba158a82a41713811b0ad05f36fdc8`

## Summary



# $B34C — XY = XA = length * limit from array data

## Disassemblatura
```assembly
.B34C  84 22    STY $22
.B34E  B1 5F    LDA ($5F),Y
.B350  85 28    STA $28
.B352  88       DEY
.B353  B1 5F    LDA ($5F),Y
.B355  85 29    STA $29
.B357  A9 10    LDA #$10
.B359  85 5D    STA $5D
.B35B  A2 00    LDX #$00
.B35D  A0 00    LDY #$00
.B35F  8A       TXA
.B360  0A       ASL
.B361  AA       TAX
.B362  98       TYA
.B363  2A       ROL
.B364  A8       TAY
.B365  B0 A4    BCS $B30B
.B367  06 71    ASL $7...
