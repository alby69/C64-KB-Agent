---
id: src-b3b3-perform-def
type: source
title: 'Source Summary: perform DEF'
aliases:
- perform DEF
- b3b3-perform-def.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b3b3-perform-def.md
  sha256: 0016d642eaaa6987ed7b556f29c23a781bb76aa6f3f4c77c4d52a6b8c188f630
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform DEF

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b3b3-perform-def.md`
**SHA256**: `0016d642eaaa6987ed7b556f29c23a781bb76aa6f3f4c77c4d52a6b8c188f630`

## Summary



# $B3B3 — perform DEF

## Disassemblatura
```assembly
.B3B3  20 E1 B3 JSR $B3E1   ; check FNx syntax
.B3B6  20 A6 B3 JSR $B3A6   ; check not direct, back here if ok
.B3B9  20 FA AE JSR $AEFA   ; scan for "(", else do syntax error then warm start
.B3BC  A9 80    LDA #$80   ; set flag for FNx
.B3BE  85 10    STA $10   ; save subscript/FNx flag
.B3C0  20 8B B0 JSR $B08B   ; get variable address
.B3C3  20 8D AD JSR $AD8D   ; check if source is numeric, else do type mismatch
.B3C6  20 F7 AE JSR $AE...
