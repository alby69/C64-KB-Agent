---
id: src-b1d1-find-or-make-array
type: source
title: 'Source Summary: find or make array'
aliases:
- find or make array
- b1d1-find-or-make-array.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b1d1-find-or-make-array.md
  sha256: ac553110aece96c63a30cd7441f566d09ef15f093a6d1dbb21a1643b6183319a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: find or make array

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b1d1-find-or-make-array.md`
**SHA256**: `ac553110aece96c63a30cd7441f566d09ef15f093a6d1dbb21a1643b6183319a`

## Summary



# $B1D1 — find or make array

## Disassemblatura
```assembly
.B1D1  A5 0C    LDA $0C   ; get DIM flag
.B1D3  05 0E    ORA $0E   ; OR with data type flag
.B1D5  48       PHA   ; push it
.B1D6  A5 0D    LDA $0D   ; get data type flag, $FF = string, $00 = numeric
.B1D8  48       PHA   ; push it
.B1D9  A0 00    LDY #$00   ; clear dimensions count now get the array dimension(s) and stack it (them) before the data type and DIM flag
.B1DB  98       TYA   ; copy dimensions count
.B1DC  48       PHA   ...
