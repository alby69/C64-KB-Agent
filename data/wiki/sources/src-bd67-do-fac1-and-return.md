---
id: src-bd67-do-fac1-and-return
type: source
title: 'Source Summary: do - FAC1 and return'
aliases:
- do - FAC1 and return
- bd67-do-fac1-and-return.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bd67-do-fac1-and-return.md
  sha256: 1ab02942f92a7288ad43902b41bc4f45feec232dc4393ad57d159f20fe1192b6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: do - FAC1 and return

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bd67-do-fac1-and-return.md`
**SHA256**: `1ab02942f92a7288ad43902b41bc4f45feec232dc4393ad57d159f20fe1192b6`

## Summary



# $BD67 — do - FAC1 and return

## Disassemblatura
```assembly
.BD67  4C B4 BF JMP $BFB4   ; do - FAC1 do unsigned FAC1*10+number
.BD6A  48       PHA   ; save character
.BD6B  24 5F    BIT $5F   ; test decimal point flag
.BD6D  10 02    BPL $BD71   ; skip exponent increment if not set
.BD6F  E6 5D    INC $5D   ; else increment number exponent
.BD71  20 E2 BA JSR $BAE2   ; multiply FAC1 by 10
.BD74  68       PLA   ; restore character
.BD75  38       SEC   ; set carry for subtract
.BD76  E9 30  ...
