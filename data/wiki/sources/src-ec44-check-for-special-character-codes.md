---
id: src-ec44-check-for-special-character-codes
type: source
title: 'Source Summary: check for special character codes'
aliases:
- check for special character codes
- ec44-check-for-special-character-codes.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ec44-check-for-special-character-codes.md
  sha256: a460731e5aacbeb623da5dd905658a349385bed08d8ca06e5865441b7564f762
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: check for special character codes

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ec44-check-for-special-character-codes.md`
**SHA256**: `a460731e5aacbeb623da5dd905658a349385bed08d8ca06e5865441b7564f762`

## Summary



# $EC44 — check for special character codes

## Disassemblatura
```assembly
.EC44  C9 0E    CMP #$0E   ; compare with [SWITCH TO LOWER CASE]
.EC46  D0 07    BNE $EC4F   ; if not [SWITCH TO LOWER CASE] skip the switch
.EC48  AD 18 D0 LDA $D018   ; get the start of character memory address
.EC4B  09 02    ORA #$02   ; mask xxxx xx1x, set lower case characters
.EC4D  D0 09    BNE $EC58   ; go save the new value, branch always check for special character codes except fro switch to lower case
.EC4F...
