---
id: src-b08b-search-for-variable
type: source
title: 'Source Summary: search for variable'
aliases:
- search for variable
- b08b-search-for-variable.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b08b-search-for-variable.md
  sha256: 01e8e42c9bf71c072b8bbee9336dad6b2ca4e6fb5d4521b1710ee29ca6780580
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: search for variable

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b08b-search-for-variable.md`
**SHA256**: `01e8e42c9bf71c072b8bbee9336dad6b2ca4e6fb5d4521b1710ee29ca6780580`

## Summary



# $B08B — search for variable

## Disassemblatura
```assembly
.B08B  A2 00    LDX #$00   ; set DIM flag = $00
.B08D  20 79 00 JSR $0079   ; scan memory, 1st character
.B090  86 0C    STX $0C   ; save DIM flag
.B092  85 45    STA $45   ; save 1st character
.B094  20 79 00 JSR $0079   ; scan memory
.B097  20 13 B1 JSR $B113   ; check byte, return Cb = 0 if<"A" or >"Z"
.B09A  B0 03    BCS $B09F   ; branch if ok
.B09C  4C 08 AF JMP $AF08   ; else syntax error then warm start was variable name so ....
