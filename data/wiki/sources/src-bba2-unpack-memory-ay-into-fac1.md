---
id: src-bba2-unpack-memory-ay-into-fac1
type: source
title: 'Source Summary: unpack memory (AY) into FAC1'
aliases:
- unpack memory (AY) into FAC1
- bba2-unpack-memory-ay-into-fac1.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bba2-unpack-memory-ay-into-fac1.md
  sha256: 1da66b278a3d96aeb696708fb1342a42096d47303cc11054dbc5d2b1fdfce89c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: unpack memory (AY) into FAC1

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bba2-unpack-memory-ay-into-fac1.md`
**SHA256**: `1da66b278a3d96aeb696708fb1342a42096d47303cc11054dbc5d2b1fdfce89c`

## Summary



# $BBA2 — unpack memory (AY) into FAC1

## Disassemblatura
```assembly
.BBA2  85 22    STA $22   ; save pointer low byte
.BBA4  84 23    STY $23   ; save pointer high byte
.BBA6  A0 04    LDY #$04   ; 5 bytes to do
.BBA8  B1 22    LDA ($22),Y   ; get fifth byte
.BBAA  85 65    STA $65   ; save FAC1 mantissa 4
.BBAC  88       DEY   ; decrement index
.BBAD  B1 22    LDA ($22),Y   ; get fourth byte
.BBAF  85 64    STA $64   ; save FAC1 mantissa 3
.BBB1  88       DEY   ; decrement index
.BBB2  B1 ...
