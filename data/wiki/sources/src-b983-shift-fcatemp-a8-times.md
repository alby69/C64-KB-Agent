---
id: src-b983-shift-fcatemp-a8-times
type: source
title: 'Source Summary: shift FCAtemp << A+8 times'
aliases:
- shift FCAtemp << A+8 times
- b983-shift-fcatemp-a8-times.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b983-shift-fcatemp-a8-times.md
  sha256: 92fd8c381d15fd9ee6880cdcd223c53a1b3842588828cf382dda50c41917720f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: shift FCAtemp << A+8 times

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b983-shift-fcatemp-a8-times.md`
**SHA256**: `92fd8c381d15fd9ee6880cdcd223c53a1b3842588828cf382dda50c41917720f`

## Summary



# $B983 — shift FCAtemp << A+8 times

## Disassemblatura
```assembly
.B983  A2 25    LDX #$25   ; set the offset to FACtemp
.B985  B4 04    LDY $04,X   ; get FACX mantissa 4
.B987  84 70    STY $70   ; save as FAC1 rounding byte
.B989  B4 03    LDY $03,X   ; get FACX mantissa 3
.B98B  94 04    STY $04,X   ; save FACX mantissa 4
.B98D  B4 02    LDY $02,X   ; get FACX mantissa 2
.B98F  94 03    STY $03,X   ; save FACX mantissa 3
.B991  B4 01    LDY $01,X   ; get FACX mantissa 1
.B993  94 02    S...
