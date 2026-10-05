---
id: src-a000-start-of-the-rom
type: source
title: 'Source Summary: start of the ROM'
aliases:
- start of the ROM
- a000-start-of-the-rom.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a000-start-of-the-rom.md
  sha256: b7e9acc383f93c9d31e90043cc548986ea7e5e0376046cbfba0940f2797a6ed7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: start of the ROM

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a000-start-of-the-rom.md`
**SHA256**: `b7e9acc383f93c9d31e90043cc548986ea7e5e0376046cbfba0940f2797a6ed7`

## Summary



# $A000 — start of the ROM

## Disassemblatura
```assembly
.A000  94 E3
.A002  7B E3
.A004  43 42 4D 42 41 53 49 43   ; PAGE SUBTTL  DISPATCH TABLES, RESERVED WORDS, AND ERROR TEXTS. ORG     ROMLOC
.A00C  30 A8   ; STMDSP: ADR(END-1)
.A00E  41 A7   ; ADR(FOR-1)
.A010  1D AD   ; ADR(NEXT-1)
.A012  F7 A8   ; ADR(DATA-1) IFN     EXTIO,<
.A014  A4 AB   ; ADR(INPUTN-1)>
.A016  BE AB   ; ADR(INPUT-1)
.A018  80 B0   ; ADR(DIM-1)
.A01A  05 AC   ; ADR(READ-1)
.A01C  A4 A9   ; ADR(LET-1)
.A01E  9F A8   ...
