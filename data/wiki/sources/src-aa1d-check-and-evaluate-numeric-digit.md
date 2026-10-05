---
id: src-aa1d-check-and-evaluate-numeric-digit
type: source
title: 'Source Summary: check and evaluate numeric digit'
aliases:
- check and evaluate numeric digit
- aa1d-check-and-evaluate-numeric-digit.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aa1d-check-and-evaluate-numeric-digit.md
  sha256: 9a1fe3ad72ffd4f071a09c198fb5822e3b4ab20dfeb5253bf0fae4f34d879660
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: check and evaluate numeric digit

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/aa1d-check-and-evaluate-numeric-digit.md`
**SHA256**: `9a1fe3ad72ffd4f071a09c198fb5822e3b4ab20dfeb5253bf0fae4f34d879660`

## Summary



# $AA1D — check and evaluate numeric digit

## Disassemblatura
```assembly
.AA1D  B1 22    LDA ($22),Y   ; get byte from string
.AA1F  20 80 00 JSR $0080   ; clear Cb if numeric. this call should be to $84 as the code from $80 first compares the byte with [SPACE] and does a BASIC increment and get if it is
.AA22  90 03    BCC $AA27   ; branch if numeric
.AA24  4C 48 B2 JMP $B248   ; do illegal quantity error then warm start
.AA27  E9 2F    SBC #$2F   ; subtract $2F + carry to convert ASCII to ...
