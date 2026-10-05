---
id: fcdb-increment-readwrite-pointer
type: entity
title: increment read/write pointer
aliases:
- increment read/write pointer
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fcdb-increment-readwrite-pointer.md
  sha256: 163a02ef2e0b54558950858f3855cf9753a00d02af412455c74249cf02617a13
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fcdb-increment-readwrite-pointer
---

# increment read/write pointer



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
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fcdb-increment-readwrite-pointer]]
