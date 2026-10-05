---
id: src-ba28-do-convert-ay-fca1ay
type: source
title: 'Source Summary: do convert AY, FCA1*(AY)'
aliases:
- do convert AY, FCA1*(AY)
- ba28-do-convert-ay-fca1ay.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ba28-do-convert-ay-fca1ay.md
  sha256: 83e9c12fa684150f9d70834c8011b8f74682e312cd57145b4fdcda86dc5db33c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: do convert AY, FCA1*(AY)

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ba28-do-convert-ay-fca1ay.md`
**SHA256**: `83e9c12fa684150f9d70834c8011b8f74682e312cd57145b4fdcda86dc5db33c`

## Summary



# $BA28 — do convert AY, FCA1*(AY)

## Disassemblatura
```assembly
.BA28  20 8C BA JSR $BA8C   ; unpack memory (AY) into FAC2
.BA2B  D0 03    BNE $BA30   ; multiply FAC1 by FAC2 ??
.BA2D  4C 8B BA JMP $BA8B   ; exit if zero
.BA30  20 B7 BA JSR $BAB7   ; test and adjust accumulators
.BA33  A9 00    LDA #$00   ; clear A
.BA35  85 26    STA $26   ; clear temp mantissa 1
.BA37  85 27    STA $27   ; clear temp mantissa 2
.BA39  85 28    STA $28   ; clear temp mantissa 3
.BA3B  85 29    STA $29   ; ...
