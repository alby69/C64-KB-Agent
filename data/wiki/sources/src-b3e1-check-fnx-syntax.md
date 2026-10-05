---
id: src-b3e1-check-fnx-syntax
type: source
title: 'Source Summary: check FNx syntax'
aliases:
- check FNx syntax
- b3e1-check-fnx-syntax.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b3e1-check-fnx-syntax.md
  sha256: 6a1ae25dad8d24ebcaf500b004a235bad9aed44079bd2254e14ab5e226900409
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: check FNx syntax

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b3e1-check-fnx-syntax.md`
**SHA256**: `6a1ae25dad8d24ebcaf500b004a235bad9aed44079bd2254e14ab5e226900409`

## Summary



# $B3E1 — check FNx syntax

## Disassemblatura
```assembly
.B3E1  A9 A5    LDA #$A5   ; set FN token
.B3E3  20 FF AE JSR $AEFF   ; scan for CHR$(A), else do syntax error then warm start
.B3E6  09 80    ORA #$80   ; set FN flag bit
.B3E8  85 10    STA $10   ; save FN name
.B3EA  20 92 B0 JSR $B092   ; search for FN variable
.B3ED  85 4E    STA $4E   ; save function pointer low byte
.B3EF  84 4F    STY $4F   ; save function pointer high byte
.B3F1  4C 8D AD JMP $AD8D   ; check if source is numer...
