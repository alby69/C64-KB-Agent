---
id: src-a3b8-open-up-a-space-in-the-memory-set-the-end-of-arrays
type: source
title: 'Source Summary: open up a space in the memory, set the end of arrays'
aliases:
- open up a space in the memory, set the end of arrays
- a3b8-open-up-a-space-in-the-memory-set-the-end-of-arrays.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a3b8-open-up-a-space-in-the-memory-set-the-end-of-arrays.md
  sha256: dcf1fa339ad60de53198063ddc69c0692b348fd44f13bc8897733f1c8fddd9c9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: open up a space in the memory, set the end of arrays

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a3b8-open-up-a-space-in-the-memory-set-the-end-of-arrays.md`
**SHA256**: `dcf1fa339ad60de53198063ddc69c0692b348fd44f13bc8897733f1c8fddd9c9`

## Summary



# $A3B8 — open up a space in the memory, set the end of arrays

## Disassemblatura
```assembly
.A3B8  20 08 A4 JSR $A408   ; check available memory, do out of memory error if no room
.A3BB  85 31    STA $31   ; set end of arrays low byte
.A3BD  84 32    STY $32   ; set end of arrays high byte open up a space in the memory, don't set the array end
.A3BF  38       SEC   ; set carry for subtract
.A3C0  A5 5A    LDA $5A   ; get block end low byte
.A3C2  E5 5F    SBC $5F   ; subtract block start lo...
