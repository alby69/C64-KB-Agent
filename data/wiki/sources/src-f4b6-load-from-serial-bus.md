---
id: src-f4b6-load-from-serial-bus
type: source
title: 'Source Summary: LOAD FROM SERIAL BUS'
aliases:
- LOAD FROM SERIAL BUS
- f4b6-load-from-serial-bus.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f4b6-load-from-serial-bus.md
  sha256: dc5215d44a0d9f164e8f9919acf4d79fa2025d22b6eee049645babd25a8d82bd
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: LOAD FROM SERIAL BUS

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f4b6-load-from-serial-bus.md`
**SHA256**: `dc5215d44a0d9f164e8f9919acf4d79fa2025d22b6eee049645babd25a8d82bd`

## Summary



# $F4B6 — LOAD FROM SERIAL BUS

## Disassemblatura
```assembly
.F4B6  90 7B    BCC $F533   ; device < 3, e.g. tape or RS232, illegal device
.F4B8  A4 B7    LDY $B7   ; FNLEN, length of filename
.F4BA  D0 03    BNE $F4BF   ; if length not is zero
.F4BC  4C 10 F7 JMP $F710   ; 'MISSING FILENAME'
.F4BF  A6 B9    LDX $B9   ; SA, current secondary address
.F4C1  20 AF F5 JSR $F5AF   ; print "SEARCHING"
.F4C4  A9 60    LDA #$60
.F4C6  85 B9    STA $B9   ; set SA to $60
.F4C8  20 D5 F3 JSR $F3D5   ; ...
