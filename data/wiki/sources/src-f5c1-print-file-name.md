---
id: src-f5c1-print-file-name
type: source
title: 'Source Summary: print file name'
aliases:
- print file name
- f5c1-print-file-name.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f5c1-print-file-name.md
  sha256: f3d483d35d7f0e605ed844cb18249c5ba91a4f7f9a1e7d1adeae17ad2d1e4a03
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: print file name

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f5c1-print-file-name.md`
**SHA256**: `f3d483d35d7f0e605ed844cb18249c5ba91a4f7f9a1e7d1adeae17ad2d1e4a03`

## Summary



# $F5C1 — print file name

## Disassemblatura
```assembly
.F5C1  A4 B7    LDY $B7   ; get file name length
.F5C3  F0 0C    BEQ $F5D1   ; exit if null file name
.F5C5  A0 00    LDY #$00   ; clear index
.F5C7  B1 BB    LDA ($BB),Y   ; get file name byte
.F5C9  20 D2 FF JSR $FFD2   ; output character to channel
.F5CC  C8       INY   ; increment index
.F5CD  C4 B7    CPY $B7   ; compare with file name length
.F5CF  D0 F6    BNE $F5C7   ; loop if more to do
.F5D1  60       RTS
```


## Commenti

##...
