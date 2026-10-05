---
id: src-kick-assembler-tips-tricks
type: source
title: 'Source Summary: Kick Assembler tips & tricks'
aliases:
- Kick Assembler tips & tricks
- kick_assembler_tips_tricks.md
tags:
- raster interrupts
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/kick_assembler_tips_tricks.md
  sha256: 6678ea3fe1d9e83cff466dff450d90e4cd7334fdf36fbff93574c9d605bb397c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Kick Assembler tips & tricks

**Raw Source File**: `data/docs/codebase_c64_org/base/kick_assembler_tips_tricks.md`
**SHA256**: `6678ea3fe1d9e83cff466dff450d90e4cd7334fdf36fbff93574c9d605bb397c`

## Summary




# Kick Assembler tips & tricks

### Table of Contents

# Kick Assembler tips & tricks

These tips & tricks have been extracted from various threads on the CSDb forum.
There's also [a page with a collection of macros](https://codebase.c64.org/doku.php?id=base:kick_assembler_macros) for Kick Assembler.

## Many interrupts

Suppose you have a routine that uses many IRQs. You might want create a macro to use at the end of each IRQ:

```
.macro endIrq(d012Value, irq) { 
        lda #d012Value
    ...
