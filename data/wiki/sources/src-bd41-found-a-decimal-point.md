---
id: src-bd41-found-a-decimal-point
type: source
title: 'Source Summary: FOUND A DECIMAL POINT'
aliases:
- FOUND A DECIMAL POINT
- bd41-found-a-decimal-point.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bd41-found-a-decimal-point.md
  sha256: c01e25b36a4da228b52646dfa1bb2049d62261f142efd9d70b6d8ccff47d778c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: FOUND A DECIMAL POINT

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bd41-found-a-decimal-point.md`
**SHA256**: `c01e25b36a4da228b52646dfa1bb2049d62261f142efd9d70b6d8ccff47d778c`

## Summary



# $BD41 — FOUND A DECIMAL POINT

## Disassemblatura
```assembly
.BD41  66 5F    ROR $5F   ; C=1, SET DPFLG FOR DECIMAL POINT
.BD43  24 5F    BIT $5F   ; CHECK IF PREVIOUS DEC. PT.
.BD45  50 C3    BVC $BD0A   ; NO PREVIOUS DECIMAL POINT A SECOND DECIMAL POINT IS TAKEN AS A TERMINATOR TO THE NUMERIC STRING. "A=11..22" WILL GIVE A SYNTAX ERROR, BECAUSE IT IS TWO NUMBERS WITH NO OPERATOR BETWEEN. "PRINT 11..22" GIVES NO ERROR, BECAUSE IT IS JUST THE CONCATENATION OF TWO NUMBERS. NUMBER TERMINATED,...
