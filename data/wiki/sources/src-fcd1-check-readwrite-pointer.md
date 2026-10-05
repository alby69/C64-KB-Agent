---
id: src-fcd1-check-readwrite-pointer
type: source
title: 'Source Summary: check read/write pointer'
aliases:
- check read/write pointer
- fcd1-check-readwrite-pointer.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fcd1-check-readwrite-pointer.md
  sha256: f01101e6f790bea6fd0486013679e249a23e063b01198a726bbef8e460cb9076
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: check read/write pointer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fcd1-check-readwrite-pointer.md`
**SHA256**: `f01101e6f790bea6fd0486013679e249a23e063b01198a726bbef8e460cb9076`

## Summary



# $FCD1 — check read/write pointer

## Disassemblatura
```assembly
.FCD1  38       SEC   ; set carry for subtract
.FCD2  A5 AC    LDA $AC   ; get buffer address low byte
.FCD4  E5 AE    SBC $AE   ; subtract buffer end low byte
.FCD6  A5 AD    LDA $AD   ; get buffer address high byte
.FCD8  E5 AF    SBC $AF   ; subtract buffer end high byte
.FCDA  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FCD1**: set carry for subtract
- **$FCD2**: get buffer address low byte
- **$FCD4**...
