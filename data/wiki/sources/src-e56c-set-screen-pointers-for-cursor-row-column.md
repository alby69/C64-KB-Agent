---
id: src-e56c-set-screen-pointers-for-cursor-row-column
type: source
title: 'Source Summary: set screen pointers for cursor row, column'
aliases:
- set screen pointers for cursor row, column
- e56c-set-screen-pointers-for-cursor-row-column.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e56c-set-screen-pointers-for-cursor-row-column.md
  sha256: 18c5aa8c4a2eccf11de093feb03762b04dea517d04b2de75d8a0e2657723370c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set screen pointers for cursor row, column

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e56c-set-screen-pointers-for-cursor-row-column.md`
**SHA256**: `18c5aa8c4a2eccf11de093feb03762b04dea517d04b2de75d8a0e2657723370c`

## Summary



# $E56C — set screen pointers for cursor row, column

## Disassemblatura
```assembly
.E56C  A6 D6    LDX $D6   ; get the cursor row
.E56E  A5 D3    LDA $D3   ; get the cursor column
.E570  B4 D9    LDY $D9,X   ; get start of line X pointer high byte
.E572  30 08    BMI $E57C   ; if it is the logical line start continue
.E574  18       CLC   ; else clear carry for add
.E575  69 28    ADC #$28   ; add one line length
.E577  85 D3    STA $D3   ; save the cursor column
.E579  CA       DEX   ; decr...
