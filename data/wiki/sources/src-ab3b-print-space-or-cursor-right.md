---
id: src-ab3b-print-space-or-cursor-right
type: source
title: 'Source Summary: print [SPACE] or [CURSOR RIGHT]'
aliases:
- print [SPACE] or [CURSOR RIGHT]
- ab3b-print-space-or-cursor-right.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ab3b-print-space-or-cursor-right.md
  sha256: ee77d2b420e72f8935138bd8e02e4daac4562ff0dbd3b3706cd32c071311802e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: print [SPACE] or [CURSOR RIGHT]

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ab3b-print-space-or-cursor-right.md`
**SHA256**: `ee77d2b420e72f8935138bd8e02e4daac4562ff0dbd3b3706cd32c071311802e`

## Summary



# $AB3B — print [SPACE] or [CURSOR RIGHT]

## Disassemblatura
```assembly
.AB3B  A5 13    LDA $13   ; get current I/O channel
.AB3D  F0 03    BEQ $AB42   ; if default channel go output [CURSOR RIGHT]
.AB3F  A9 20    LDA #$20   ; else output [SPACE]
.AB41  2C       .BYTE $2C   ; makes next line BIT $1DA9
.AB42  A9 1D    LDA #$1D   ; set [CURSOR RIGHT]
.AB44  2C       .BYTE $2C   ; makes next line BIT $3FA9
```


## Commenti

### Original Disassembly (—)
- **$AB3B**: get current I/O channel
- **...
