---
id: src-f76a-write-the-tape-header
type: source
title: 'Source Summary: write the tape header'
aliases:
- write the tape header
- f76a-write-the-tape-header.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f76a-write-the-tape-header.md
  sha256: e653df5ee3dc0930b7c4151eef4066ec6dfbd0365f7d5d6aeefc5be780ee4cd2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: write the tape header

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f76a-write-the-tape-header.md`
**SHA256**: `e653df5ee3dc0930b7c4151eef4066ec6dfbd0365f7d5d6aeefc5be780ee4cd2`

## Summary



# $F76A — write the tape header

## Disassemblatura
```assembly
.F76A  85 9E    STA $9E   ; save header type
.F76C  20 D0 F7 JSR $F7D0   ; get tape buffer start pointer in XY
.F76F  90 5E    BCC $F7CF   ; if < $0200 just exit ??
.F771  A5 C2    LDA $C2   ; get I/O start address high byte
.F773  48       PHA   ; save it
.F774  A5 C1    LDA $C1   ; get I/O start address low byte
.F776  48       PHA   ; save it
.F777  A5 AF    LDA $AF   ; get tape end address high byte
.F779  48       PHA   ; sav...
