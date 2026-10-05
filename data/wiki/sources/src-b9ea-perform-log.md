---
id: src-b9ea-perform-log
type: source
title: 'Source Summary: perform LOG()'
aliases:
- perform LOG()
- b9ea-perform-log.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b9ea-perform-log.md
  sha256: 46f2d58c8a43ecf1e983677bfd23d57199c010d0e9c781e9c35ce54363dcaa8d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform LOG()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b9ea-perform-log.md`
**SHA256**: `46f2d58c8a43ecf1e983677bfd23d57199c010d0e9c781e9c35ce54363dcaa8d`

## Summary



# $B9EA — perform LOG()

## Disassemblatura
```assembly
.B9EA  20 2B BC JSR $BC2B   ; test sign and zero
.B9ED  F0 02    BEQ $B9F1   ; if zero do illegal quantity error then warm start
.B9EF  10 03    BPL $B9F4   ; skip error if +ve
.B9F1  4C 48 B2 JMP $B248   ; do illegal quantity error then warm start
.B9F4  A5 61    LDA $61   ; get FAC1 exponent
.B9F6  E9 7F    SBC #$7F   ; normalise it
.B9F8  48       PHA   ; save it
.B9F9  A9 80    LDA #$80   ; set exponent to zero
.B9FB  85 61    STA $61...
