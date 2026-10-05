---
id: src-a617-search-basic-for-temp-integer-line-number-from-ax
type: source
title: 'Source Summary: search Basic for temp integer line number from AX'
aliases:
- search Basic for temp integer line number from AX
- a617-search-basic-for-temp-integer-line-number-from-ax.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a617-search-basic-for-temp-integer-line-number-from-ax.md
  sha256: f33eda4177ccd309d9c9e5a25b117ded648150ebe60f14d89a107e6fe58bf841
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: search Basic for temp integer line number from AX

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a617-search-basic-for-temp-integer-line-number-from-ax.md`
**SHA256**: `f33eda4177ccd309d9c9e5a25b117ded648150ebe60f14d89a107e6fe58bf841`

## Summary



# $A617 — search Basic for temp integer line number from AX

## Disassemblatura
```assembly
.A617  A0 01    LDY #$01   ; set index to next line pointer high byte
.A619  85 5F    STA $5F   ; save low byte as current
.A61B  86 60    STX $60   ; save high byte as current
.A61D  B1 5F    LDA ($5F),Y   ; get next line pointer high byte from address
.A61F  F0 1F    BEQ $A640   ; pointer was zero so done, exit
.A621  C8       INY   ; increment index ...
.A622  C8       INY   ; ... to line # high byte...
