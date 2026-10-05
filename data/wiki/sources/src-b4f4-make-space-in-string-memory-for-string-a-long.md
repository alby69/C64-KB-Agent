---
id: src-b4f4-make-space-in-string-memory-for-string-a-long
type: source
title: 'Source Summary: make space in string memory for string A long'
aliases:
- make space in string memory for string A long
- b4f4-make-space-in-string-memory-for-string-a-long.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b4f4-make-space-in-string-memory-for-string-a-long.md
  sha256: 8e4101042cbebb32c1a51c61cc2ea198647a3cc273d021c6aa739a07f02c3fb4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: make space in string memory for string A long

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b4f4-make-space-in-string-memory-for-string-a-long.md`
**SHA256**: `8e4101042cbebb32c1a51c61cc2ea198647a3cc273d021c6aa739a07f02c3fb4`

## Summary



# $B4F4 — make space in string memory for string A long

## Disassemblatura
```assembly
.B4F4  46 0F    LSR $0F   ; clear garbage collected flag (b7) make space for string A long
.B4F6  48       PHA   ; save string length
.B4F7  49 FF    EOR #$FF   ; complement it
.B4F9  38       SEC   ; set carry for subtract, two's complement add
.B4FA  65 33    ADC $33   ; add bottom of string space low byte, subtract length
.B4FC  A4 34    LDY $34   ; get bottom of string space high byte
.B4FE  B0 01    BC...
