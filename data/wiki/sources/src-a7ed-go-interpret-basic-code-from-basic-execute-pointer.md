---
id: src-a7ed-go-interpret-basic-code-from-basic-execute-pointer
type: source
title: 'Source Summary: go interpret BASIC code from BASIC execute pointer'
aliases:
- go interpret BASIC code from BASIC execute pointer
- a7ed-go-interpret-basic-code-from-basic-execute-pointer.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a7ed-go-interpret-basic-code-from-basic-execute-pointer.md
  sha256: 55654867033f6fe10579b25a9fbba574bbafb5204635f3933d23ad952cac2318
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: go interpret BASIC code from BASIC execute pointer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a7ed-go-interpret-basic-code-from-basic-execute-pointer.md`
**SHA256**: `55654867033f6fe10579b25a9fbba574bbafb5204635f3933d23ad952cac2318`

## Summary



# $A7ED — go interpret BASIC code from BASIC execute pointer

## Disassemblatura
```assembly
.A7ED  F0 3C    BEQ $A82B   ; if the first byte is null just exit
.A7EF  E9 80    SBC #$80   ; normalise the token
.A7F1  90 11    BCC $A804   ; if wasn't token go do LET
.A7F3  C9 23    CMP #$23   ; compare with token for TAB(-$80
.A7F5  B0 17    BCS $A80E   ; branch if >= TAB(
.A7F7  0A       ASL   ; *2 bytes per vector
.A7F8  A8       TAY   ; copy to index
.A7F9  B9 0D A0 LDA $A00D,Y   ; get vector ...
