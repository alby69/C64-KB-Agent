---
id: src-fcdb-increment-readwrite-pointer
type: source
title: 'Source Summary: increment read/write pointer'
aliases:
- increment read/write pointer
- fcdb-increment-readwrite-pointer.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fcdb-increment-readwrite-pointer.md
  sha256: 163a02ef2e0b54558950858f3855cf9753a00d02af412455c74249cf02617a13
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: increment read/write pointer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fcdb-increment-readwrite-pointer.md`
**SHA256**: `163a02ef2e0b54558950858f3855cf9753a00d02af412455c74249cf02617a13`

## Summary



# $FCDB — increment read/write pointer

## Disassemblatura
```assembly
.FCDB  E6 AC    INC $AC   ; increment buffer address low byte
.FCDD  D0 02    BNE $FCE1   ; branch if no overflow
.FCDF  E6 AD    INC $AD   ; increment buffer address low byte
.FCE1  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FCDB**: increment buffer address low byte
- **$FCDD**: branch if no overflow
- **$FCDF**: increment buffer address low byte

### Marko Mäkelä (Marko Mäkelä)
Nessun commento dispo...
