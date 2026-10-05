---
id: src-ba8c-unpack-memory-ay-into-fac2
type: source
title: 'Source Summary: unpack memory (AY) into FAC2'
aliases:
- unpack memory (AY) into FAC2
- ba8c-unpack-memory-ay-into-fac2.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ba8c-unpack-memory-ay-into-fac2.md
  sha256: 59013883b2e128d5cf8d826a45c83ae6117760ed007f5c21e3456a518e4a8cc7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: unpack memory (AY) into FAC2

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ba8c-unpack-memory-ay-into-fac2.md`
**SHA256**: `59013883b2e128d5cf8d826a45c83ae6117760ed007f5c21e3456a518e4a8cc7`

## Summary



# $BA8C — unpack memory (AY) into FAC2

## Disassemblatura
```assembly
.BA8C  85 22    STA $22   ; save pointer low byte
.BA8E  84 23    STY $23   ; save pointer high byte
.BA90  A0 04    LDY #$04   ; 5 bytes to get (0-4)
.BA92  B1 22    LDA ($22),Y   ; get mantissa 4
.BA94  85 6D    STA $6D   ; save FAC2 mantissa 4
.BA96  88       DEY   ; decrement index
.BA97  B1 22    LDA ($22),Y   ; get mantissa 3
.BA99  85 6C    STA $6C   ; save FAC2 mantissa 3
.BA9B  88       DEY   ; decrement index
.BA9...
