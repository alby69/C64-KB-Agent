---
id: src-f7ea-find-specific-tape-header
type: source
title: 'Source Summary: find specific tape header'
aliases:
- find specific tape header
- f7ea-find-specific-tape-header.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f7ea-find-specific-tape-header.md
  sha256: a2d088f46fd5651af34822d6af3c9d430f2fb18cfddb24fb618640d13273afd3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: find specific tape header

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f7ea-find-specific-tape-header.md`
**SHA256**: `a2d088f46fd5651af34822d6af3c9d430f2fb18cfddb24fb618640d13273afd3`

## Summary



# $F7EA — find specific tape header

## Disassemblatura
```assembly
.F7EA  20 2C F7 JSR $F72C   ; find tape header, exit with header in buffer
.F7ED  B0 1D    BCS $F80C   ; just exit if error
.F7EF  A0 05    LDY #$05   ; index to name
.F7F1  84 9F    STY $9F   ; save as tape buffer index
.F7F3  A0 00    LDY #$00   ; clear Y
.F7F5  84 9E    STY $9E   ; save as name buffer index
.F7F7  C4 B7    CPY $B7   ; compare with file name length
.F7F9  F0 10    BEQ $F80B   ; ok exit if match
.F7FB  B1 BB ...
