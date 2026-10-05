---
id: src-a5f5-advance-pointer-to-next-token-name
type: source
title: 'Source Summary: ADVANCE POINTER TO NEXT TOKEN NAME'
aliases:
- ADVANCE POINTER TO NEXT TOKEN NAME
- a5f5-advance-pointer-to-next-token-name.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a5f5-advance-pointer-to-next-token-name.md
  sha256: 9f96c20b7becfd6bb65904e24a8b1e760b225d30b609435e676da486259bb658
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ADVANCE POINTER TO NEXT TOKEN NAME

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a5f5-advance-pointer-to-next-token-name.md`
**SHA256**: `9f96c20b7becfd6bb65904e24a8b1e760b225d30b609435e676da486259bb658`

## Summary



# $A5F5 — ADVANCE POINTER TO NEXT TOKEN NAME

## Disassemblatura
```assembly
.A5F5  A6 7A    LDX $7A   ; GET POINTER TO INPUT LINE IN X-REG
.A5F7  E6 0B    INC $0B   ; BUMP (TOKEN # - $80)
.A5F9  C8       INY   ; NEXT TOKEN ONE BEYOND THAT
.A5FA  B9 9D A0 LDA $A09D,Y   ; YES, AT NEXT NAME.  END OF TABLE?
.A5FD  10 FA    BPL $A5F9
.A5FF  B9 9E A0 LDA $A09E,Y
.A602  D0 B4    BNE $A5B8   ; NO, NOT END OF TABLE
.A604  BD 00 02 LDA $0200,X   ; YES, SO NOT A KEYWORD
.A607  10 BE    BPL $A5C7   ; ......
