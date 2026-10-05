---
id: src-b24d-found-the-array
type: source
title: 'Source Summary: found the array'
aliases:
- found the array
- b24d-found-the-array.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b24d-found-the-array.md
  sha256: 4ea0f85005f222b196e47b34a874b23b418cbd81f7377e4a2159a62e14a66ce4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: found the array

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b24d-found-the-array.md`
**SHA256**: `4ea0f85005f222b196e47b34a874b23b418cbd81f7377e4a2159a62e14a66ce4`

## Summary



# $B24D — found the array

## Disassemblatura
```assembly
.B24D  A2 13    LDX #$13   ; set error $13, double dimension error
.B24F  A5 0C    LDA $0C   ; get DIM flag
.B251  D0 F7    BNE $B24A   ; if we are trying to dimension it do error #X then warm start found the array and we're not dimensioning it so we must find an element in it
.B253  20 94 B1 JSR $B194   ; set-up array pointer to first element in array
.B256  A5 0B    LDA $0B   ; get dimensions count
.B258  A0 04    LDY #$04   ; set ind...
