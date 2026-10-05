---
id: src-bcf3-get-fac1-from-string
type: source
title: 'Source Summary: get FAC1 from string'
aliases:
- get FAC1 from string
- bcf3-get-fac1-from-string.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bcf3-get-fac1-from-string.md
  sha256: 0388a8a5860c996e55b9a4eac4aa19da81fce626a09ed7b0ef58dd13c60a38f2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: get FAC1 from string

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bcf3-get-fac1-from-string.md`
**SHA256**: `0388a8a5860c996e55b9a4eac4aa19da81fce626a09ed7b0ef58dd13c60a38f2`

## Summary



# $BCF3 — get FAC1 from string

## Disassemblatura
```assembly
.BCF3  A0 00    LDY #$00   ; clear Y
.BCF5  A2 0A    LDX #$0A   ; set index
.BCF7  94 5D    STY $5D,X   ; clear byte
.BCF9  CA       DEX   ; decrement index
.BCFA  10 FB    BPL $BCF7   ; loop until numexp to negnum (and FAC1) = $00
.BCFC  90 0F    BCC $BD0D   ; branch if first character is numeric
.BCFE  C9 2D    CMP #$2D   ; else compare with "-"
.BD00  D0 04    BNE $BD06   ; branch if not "-"
.BD02  86 67    STX $67   ; set flag ...
