---
id: src-b6ec-perform-chr
type: source
title: 'Source Summary: perform CHR$()'
aliases:
- perform CHR$()
- b6ec-perform-chr.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b6ec-perform-chr.md
  sha256: 9ea77fb4770c008e81cde06c665f0768807b245f74a0996d91241b70f5725005
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform CHR$()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b6ec-perform-chr.md`
**SHA256**: `9ea77fb4770c008e81cde06c665f0768807b245f74a0996d91241b70f5725005`

## Summary



# $B6EC — perform CHR$()

## Disassemblatura
```assembly
.B6EC  20 A1 B7 JSR $B7A1   ; evaluate byte expression, result in X
.B6EF  8A       TXA   ; copy to A
.B6F0  48       PHA   ; save character
.B6F1  A9 01    LDA #$01   ; string is single byte
.B6F3  20 7D B4 JSR $B47D   ; make string space A bytes long
.B6F6  68       PLA   ; get character back
.B6F7  A0 00    LDY #$00   ; clear index
.B6F9  91 62    STA ($62),Y   ; save byte in string - byte IS string!
.B6FB  68       PLA   ; dump retur...
