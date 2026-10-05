---
id: src-abbf-perform-input
type: source
title: 'Source Summary: perform INPUT'
aliases:
- perform INPUT
- abbf-perform-input.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/abbf-perform-input.md
  sha256: 635034daac850527f9cdc89c3fcffabc97fe980361b89fed8c39a38c78b19261
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform INPUT

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/abbf-perform-input.md`
**SHA256**: `635034daac850527f9cdc89c3fcffabc97fe980361b89fed8c39a38c78b19261`

## Summary



# $ABBF — perform INPUT

## Disassemblatura
```assembly
.ABBF  C9 22    CMP #$22   ; compare next byte with open quote
.ABC1  D0 0B    BNE $ABCE   ; if no prompt string just do INPUT
.ABC3  20 BD AE JSR $AEBD   ; print "..." string
.ABC6  A9 3B    LDA #$3B   ; load A with ";"
.ABC8  20 FF AE JSR $AEFF   ; scan for CHR$(A), else do syntax error then warm start
.ABCB  20 21 AB JSR $AB21   ; print string from utility pointer done with prompt, now get data
.ABCE  20 A6 B3 JSR $B3A6   ; check not D...
