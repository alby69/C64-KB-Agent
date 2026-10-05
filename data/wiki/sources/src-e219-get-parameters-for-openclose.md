---
id: src-e219-get-parameters-for-openclose
type: source
title: 'Source Summary: get parameters for OPEN/CLOSE'
aliases:
- get parameters for OPEN/CLOSE
- e219-get-parameters-for-openclose.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e219-get-parameters-for-openclose.md
  sha256: 2a0c92b7aa2695713cdfc3bf003fc8c1c1a97b5fb71a7516c2b599a557fde35e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: get parameters for OPEN/CLOSE

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e219-get-parameters-for-openclose.md`
**SHA256**: `2a0c92b7aa2695713cdfc3bf003fc8c1c1a97b5fb71a7516c2b599a557fde35e`

## Summary



# $E219 — get parameters for OPEN/CLOSE

## Disassemblatura
```assembly
.E219  A9 00    LDA #$00   ; clear the filename length
.E21B  20 BD FF JSR $FFBD   ; clear the filename
.E21E  20 11 E2 JSR $E211   ; scan for valid byte, else do syntax error then warm start
.E221  20 9E B7 JSR $B79E   ; get byte parameter, logical file number
.E224  86 49    STX $49   ; save logical file number
.E226  8A       TXA   ; copy logical file number to A
.E227  A2 01    LDX #$01   ; set default device number, c...
