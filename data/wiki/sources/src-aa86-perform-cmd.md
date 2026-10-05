---
id: src-aa86-perform-cmd
type: source
title: 'Source Summary: perform CMD'
aliases:
- perform CMD
- aa86-perform-cmd.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aa86-perform-cmd.md
  sha256: c3900eeb343be5f3e45b2cd767547e2a653c85ac9900d3a5d028c59d9c101885
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform CMD

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/aa86-perform-cmd.md`
**SHA256**: `c3900eeb343be5f3e45b2cd767547e2a653c85ac9900d3a5d028c59d9c101885`

## Summary



# $AA86 — perform CMD

## Disassemblatura
```assembly
.AA86  20 9E B7 JSR $B79E   ; get byte parameter
.AA89  F0 05    BEQ $AA90   ; branch if following byte is ":" or [EOT]
.AA8B  A9 2C    LDA #$2C   ; set ","
.AA8D  20 FF AE JSR $AEFF   ; scan for CHR$(A), else do syntax error then warm start
.AA90  08       PHP   ; save status
.AA91  86 13    STX $13   ; set current I/O channel
.AA93  20 18 E1 JSR $E118   ; open channel for output with error check
.AA96  28       PLP   ; restore status
.AA9...
