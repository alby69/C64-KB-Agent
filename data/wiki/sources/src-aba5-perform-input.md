---
id: src-aba5-perform-input
type: source
title: 'Source Summary: perform INPUT#'
aliases:
- perform INPUT#
- aba5-perform-input.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aba5-perform-input.md
  sha256: 23b2b470aaa37312cb1df42dd04356d93cee2b15b9fb6826f6a3674c2c8ecd14
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform INPUT#

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/aba5-perform-input.md`
**SHA256**: `23b2b470aaa37312cb1df42dd04356d93cee2b15b9fb6826f6a3674c2c8ecd14`

## Summary



# $ABA5 — perform INPUT#

## Disassemblatura
```assembly
.ABA5  20 9E B7 JSR $B79E   ; get byte parameter
.ABA8  A9 2C    LDA #$2C   ; set ","
.ABAA  20 FF AE JSR $AEFF   ; scan for CHR$(A), else do syntax error then warm start
.ABAD  86 13    STX $13   ; set current I/O channel
.ABAF  20 1E E1 JSR $E11E   ; open channel for input with error check
.ABB2  20 CE AB JSR $ABCE   ; perform INPUT with no prompt string
```


## Commenti

### Original Disassembly (—)
- **$ABA5**: get byte parameter
- ...
