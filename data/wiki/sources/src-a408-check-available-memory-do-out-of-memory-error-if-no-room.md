---
id: src-a408-check-available-memory-do-out-of-memory-error-if-no-room
type: source
title: 'Source Summary: check available memory, do out of memory error if no room'
aliases:
- check available memory, do out of memory error if no room
- a408-check-available-memory-do-out-of-memory-error-if-no-room.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a408-check-available-memory-do-out-of-memory-error-if-no-room.md
  sha256: 14f4529980c51724111cac21f72f865c6e853db2d2c3767d4189a41051127cd0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: check available memory, do out of memory error if no room

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a408-check-available-memory-do-out-of-memory-error-if-no-room.md`
**SHA256**: `14f4529980c51724111cac21f72f865c6e853db2d2c3767d4189a41051127cd0`

## Summary



# $A408 — check available memory, do out of memory error if no room

## Disassemblatura
```assembly
.A408  C4 34    CPY $34   ; compare with bottom of string space high byte
.A40A  90 28    BCC $A434   ; if less then exit (is ok)
.A40C  D0 04    BNE $A412   ; skip next test if greater (tested <) high byte was =, now do low byte
.A40E  C5 33    CMP $33   ; compare with bottom of string space low byte
.A410  90 22    BCC $A434   ; if less then exit (is ok) address is > string storage ptr (oops!)...
