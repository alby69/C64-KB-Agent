---
id: src-e195-do-ready-return-to-basic
type: source
title: 'Source Summary: do READY return to BASIC'
aliases:
- do READY return to BASIC
- e195-do-ready-return-to-basic.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e195-do-ready-return-to-basic.md
  sha256: 091ac220c0563e372f0ccdc1552de64a6aa9a1ad799c8e67d0bc4e7502ba34cf
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: do READY return to BASIC

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e195-do-ready-return-to-basic.md`
**SHA256**: `091ac220c0563e372f0ccdc1552de64a6aa9a1ad799c8e67d0bc4e7502ba34cf`

## Summary



# $E195 — do READY return to BASIC

## Disassemblatura
```assembly
.E195  20 B7 FF JSR $FFB7   ; read I/O status word
.E198  29 BF    AND #$BF   ; mask x0xx xxxx, clear read error
.E19A  F0 05    BEQ $E1A1   ; branch if no errors
.E19C  A2 1D    LDX #$1D   ; error $1D, load error
.E19E  4C 37 A4 JMP $A437   ; do error #X then warm start
.E1A1  A5 7B    LDA $7B   ; get BASIC execute pointer high byte
.E1A3  C9 02    CMP #$02   ; compare with $02xx
.E1A5  D0 0E    BNE $E1B5   ; branch if not imm...
