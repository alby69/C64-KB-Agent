---
id: src-e12a-perform-sys
type: source
title: 'Source Summary: perform SYS'
aliases:
- perform SYS
- e12a-perform-sys.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e12a-perform-sys.md
  sha256: 53302f260e57c998e1e12a72f48380e114985cdec7d581afef2b4b3d6d9575ce
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform SYS

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e12a-perform-sys.md`
**SHA256**: `53302f260e57c998e1e12a72f48380e114985cdec7d581afef2b4b3d6d9575ce`

## Summary



# $E12A — perform SYS

## Disassemblatura
```assembly
.E12A  20 8A AD JSR $AD8A   ; evaluate expression and check is numeric, else do type mismatch
.E12D  20 F7 B7 JSR $B7F7   ; convert FAC_1 to integer in temporary integer
.E130  A9 E1    LDA #$E1   ; get return address high byte
.E132  48       PHA   ; push as return address
.E133  A9 46    LDA #$46   ; get return address low byte
.E135  48       PHA   ; push as return address
.E136  AD 0F 03 LDA $030F   ; get saved status register
.E139  48...
