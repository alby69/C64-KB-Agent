---
id: src-a9a5-perform-let
type: source
title: 'Source Summary: perform LET'
aliases:
- perform LET
- a9a5-perform-let.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a9a5-perform-let.md
  sha256: c70314f0e242ad4e26ffcc2040313d6adbe866409d47dc48cb17cdffea244507
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform LET

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a9a5-perform-let.md`
**SHA256**: `c70314f0e242ad4e26ffcc2040313d6adbe866409d47dc48cb17cdffea244507`

## Summary



# $A9A5 — perform LET

## Disassemblatura
```assembly
.A9A5  20 8B B0 JSR $B08B   ; get variable address
.A9A8  85 49    STA $49   ; save variable address low byte
.A9AA  84 4A    STY $4A   ; save variable address high byte
.A9AC  A9 B2    LDA #$B2   ; $B2 is "=" token
.A9AE  20 FF AE JSR $AEFF   ; scan for CHR$(A), else do syntax error then warm start
.A9B1  A5 0E    LDA $0E   ; get data type flag, $80 = integer, $00 = float
.A9B3  48       PHA   ; push data type flag
.A9B4  A5 0D    LDA $0D ...
