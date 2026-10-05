---
id: src-f69b
type: source
title: 'Source Summary: ;**'
aliases:
- ;**
- f69b.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f69b.md
  sha256: 91f7841dea53f6222c529507f906a4195dc39535034b8bba7db4e964f5c0eeca
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ;**

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f69b.md`
**SHA256**: `91f7841dea53f6222c529507f906a4195dc39535034b8bba7db4e964f5c0eeca`

## Summary



# $F69B — ;**

## Disassemblatura
```assembly
.F69B  A2 00    LDX #$00   ; UDTIM  LDX #0          ;PRE-LOAD FOR LATER ; ;HERE WE PROCEED WITH AN INCREMENT ;OF THE TIME REGISTER. ;
.F69D  E6 A2    INC $A2   ; UD20   INC TIME+2
.F69F  D0 06    BNE $F6A7   ; BNE    UD30
.F6A1  E6 A1    INC $A1   ; INC    TIME+1
.F6A3  D0 02    BNE $F6A7   ; BNE    UD30
.F6A5  E6 A0    INC $A0   ; INC    TIME ; ;HERE WE CHECK FOR ROLL-OVER 23:59:59 ;AND RESET THE CLOCK TO ZERO IF TRUE ;
.F6A7  38       SEC   ; UD3...
