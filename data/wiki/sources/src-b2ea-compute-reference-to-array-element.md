---
id: src-b2ea-compute-reference-to-array-element
type: source
title: 'Source Summary: compute reference to array element'
aliases:
- compute reference to array element
- b2ea-compute-reference-to-array-element.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b2ea-compute-reference-to-array-element.md
  sha256: 8135ffab065603548b19f329774ce9c29ed8427f0b2ab3b33f60aa7658b228e7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: compute reference to array element

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b2ea-compute-reference-to-array-element.md`
**SHA256**: `8135ffab065603548b19f329774ce9c29ed8427f0b2ab3b33f60aa7658b228e7`

## Summary



# $B2EA — compute reference to array element

## Disassemblatura
```assembly
.B2EA  B1 5F    LDA ($5F),Y
.B2EC  85 0B    STA $0B
.B2EE  A9 00    LDA #$00
.B2F0  85 71    STA $71
.B2F2  85 72    STA $72
.B2F4  C8       INY
.B2F5  68       PLA
.B2F6  AA       TAX
.B2F7  85 64    STA $64
.B2F9  68       PLA
.B2FA  85 65    STA $65
.B2FC  D1 5F    CMP ($5F),Y
.B2FE  90 0E    BCC $B30E
.B300  D0 06    BNE $B308
.B302  C8       INY
.B303  8A       TXA
.B304  D1 5F    CMP ($5F),Y
.B306  90 07    BCC ...
