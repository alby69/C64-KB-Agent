---
id: src-e422-print-the-start-up-message-and-initialise-the-memory-pointers
type: source
title: 'Source Summary: print the start up message and initialise the memory pointers'
aliases:
- print the start up message and initialise the memory pointers
- e422-print-the-start-up-message-and-initialise-the-memory-pointers.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e422-print-the-start-up-message-and-initialise-the-memory-pointers.md
  sha256: 0c8bf7cf77677c20fed585a6ab5f75d4be2a191832b44b22be878d8133565f74
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: print the start up message and initialise the memory pointers

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e422-print-the-start-up-message-and-initialise-the-memory-pointers.md`
**SHA256**: `0c8bf7cf77677c20fed585a6ab5f75d4be2a191832b44b22be878d8133565f74`

## Summary



# $E422 — print the start up message and initialise the memory pointers

## Disassemblatura
```assembly
.E422  A5 2B    LDA $2B   ; get the start of memory low byte
.E424  A4 2C    LDY $2C   ; get the start of memory high byte
.E426  20 08 A4 JSR $A408   ; check available memory, do out of memory error if no room
.E429  A9 73    LDA #$73   ; set "**** COMMODORE 64 BASIC V2 ****" pointer low byte
.E42B  A0 E4    LDY #$E4   ; set "**** COMMODORE 64 BASIC V2 ****" pointer high byte
.E42D  20 1E A...
