---
id: src-a642-perform-new
type: source
title: 'Source Summary: perform NEW'
aliases:
- perform NEW
- a642-perform-new.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a642-perform-new.md
  sha256: 6b73323d61df8fd4c9a465349860e78add96c44e728694c0c4d647eec2084cfa
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform NEW

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a642-perform-new.md`
**SHA256**: `6b73323d61df8fd4c9a465349860e78add96c44e728694c0c4d647eec2084cfa`

## Summary



# $A642 — perform NEW

## Disassemblatura
```assembly
.A642  D0 FD    BNE $A641   ; exit if following byte to allow syntax error
.A644  A9 00    LDA #$00   ; clear A
.A646  A8       TAY   ; clear index
.A647  91 2B    STA ($2B),Y   ; clear pointer to next line low byte
.A649  C8       INY   ; increment index
.A64A  91 2B    STA ($2B),Y   ; clear pointer to next line high byte, erase program
.A64C  A5 2B    LDA $2B   ; get start of memory low byte
.A64E  18       CLC   ; clear carry for add
.A6...
