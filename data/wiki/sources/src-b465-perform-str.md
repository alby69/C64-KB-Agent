---
id: src-b465-perform-str
type: source
title: 'Source Summary: perform STR$()'
aliases:
- perform STR$()
- b465-perform-str.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b465-perform-str.md
  sha256: 2c425c73ff7e576db19c71e3699fa4a10261e707b41e37541cc1fdacd137fb4b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform STR$()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b465-perform-str.md`
**SHA256**: `2c425c73ff7e576db19c71e3699fa4a10261e707b41e37541cc1fdacd137fb4b`

## Summary



# $B465 — perform STR$()

## Disassemblatura
```assembly
.B465  20 8D AD JSR $AD8D   ; check if source is numeric, else do type mismatch
.B468  A0 00    LDY #$00   ; set string index
.B46A  20 DF BD JSR $BDDF   ; convert FAC1 to string
.B46D  68       PLA   ; dump return address (skip type check)
.B46E  68       PLA   ; dump return address (skip type check)
.B46F  A9 FF    LDA #$FF   ; set result string low pointer
.B471  A0 00    LDY #$00   ; set result string high pointer
.B473  F0 12    BEQ...
