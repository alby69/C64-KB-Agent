---
id: src-e6b6-advance-the-cursor
type: source
title: 'Source Summary: advance the cursor'
aliases:
- advance the cursor
- e6b6-advance-the-cursor.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e6b6-advance-the-cursor.md
  sha256: c28e431b13a08a82b631a23d0191389cdd1dff23380023762601be7b45293638
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: advance the cursor

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e6b6-advance-the-cursor.md`
**SHA256**: `c28e431b13a08a82b631a23d0191389cdd1dff23380023762601be7b45293638`

## Summary



# $E6B6 — advance the cursor

## Disassemblatura
```assembly
.E6B6  20 B3 E8 JSR $E8B3   ; test for line increment
.E6B9  E6 D3    INC $D3   ; increment the cursor column
.E6BB  A5 D5    LDA $D5   ; get current screen line length
.E6BD  C5 D3    CMP $D3   ; compare ?? with the cursor column
.E6BF  B0 3F    BCS $E700   ; exit if line length >= cursor column
.E6C1  C9 4F    CMP #$4F   ; compare with max length
.E6C3  F0 32    BEQ $E6F7   ; if at max clear column, back cursor up and do newline
.E...
