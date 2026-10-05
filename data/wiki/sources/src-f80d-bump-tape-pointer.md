---
id: src-f80d-bump-tape-pointer
type: source
title: 'Source Summary: bump tape pointer'
aliases:
- bump tape pointer
- f80d-bump-tape-pointer.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f80d-bump-tape-pointer.md
  sha256: 04c5bd39ee81f0d1ba22078a3985b4179b731aba8c494e2e169a7fa1d7681561
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: bump tape pointer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f80d-bump-tape-pointer.md`
**SHA256**: `04c5bd39ee81f0d1ba22078a3985b4179b731aba8c494e2e169a7fa1d7681561`

## Summary



# $F80D — bump tape pointer

## Disassemblatura
```assembly
.F80D  20 D0 F7 JSR $F7D0   ; get tape buffer start pointer in XY
.F810  E6 A6    INC $A6   ; increment tape buffer index
.F812  A4 A6    LDY $A6   ; get tape buffer index
.F814  C0 C0    CPY #$C0   ; compare with buffer length
.F816  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F80D**: get tape buffer start pointer in XY
- **$F810**: increment tape buffer index
- **$F812**: get tape buffer index
- **$F814**: comp...
