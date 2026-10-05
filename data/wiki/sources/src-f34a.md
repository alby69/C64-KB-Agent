---
id: src-f34a
type: source
title: 'Source Summary: ;**'
aliases:
- ;**
- f34a.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f34a.md
  sha256: c3ad9042047f602d636003fddb8549f8ccb21dd89f05585439ffc48eac568174
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ;**

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f34a.md`
**SHA256**: `c3ad9042047f602d636003fddb8549f8ccb21dd89f05585439ffc48eac568174`

## Summary



# $F34A — ;**

## Disassemblatura
```assembly
.F34A  A6 B8    LDX $B8   ; NOPEN  LDX LA          ;CHECK FILE #
.F34C  D0 03    BNE $F351   ; BNE    OP98            ;IS NOT THE KEYBOARD ;
.F34E  4C 0A F7 JMP $F70A   ; JMP    ERROR6          ;NOT INPUT FILE... ;
.F351  20 0F F3 JSR $F30F   ; OP98   JSR LOOKUP      ;SEE IF IN TABLE
.F354  D0 03    BNE $F359   ; BNE    OP100           ;NOT FOUND...O.K. ;
.F356  4C FE F6 JMP $F6FE   ; JMP    ERROR2          ;FILE OPEN ;
.F359  A6 98    LDX $98   ; ...
