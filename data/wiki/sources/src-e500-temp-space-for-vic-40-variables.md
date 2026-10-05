---
id: src-e500-temp-space-for-vic-40-variables
type: source
title: 'Source Summary: ; TEMP SPACE FOR VIC-40 VARIABLES *'
aliases:
- ; TEMP SPACE FOR VIC-40 VARIABLES *
- e500-temp-space-for-vic-40-variables.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e500-temp-space-for-vic-40-variables.md
  sha256: f382ccbddde95175530cf3899bfa2251c0ac3ffa9c19217302b92ea485637afa
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ; TEMP SPACE FOR VIC-40 VARIABLES *

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e500-temp-space-for-vic-40-variables.md`
**SHA256**: `f382ccbddde95175530cf3899bfa2251c0ac3ffa9c19217302b92ea485637afa`

## Summary



# $E500 — ; TEMP SPACE FOR VIC-40 VARIABLES *

## Disassemblatura
```assembly
.E500  A2 00    LDX #$00   ; IOBASE LDX #<D1PRA
.E502  A0 DC    LDY #$DC   ; LDY    #>D1PRA
.E504  60       RTS   ; RTS ; ;RETURN MAX ROWS,COLS OF SCREEN ;
.E505  A2 28    LDX #$28   ; SCRORG LDX #LLEN
.E507  A0 19    LDY #$19   ; LDY    #NLINES
.E509  60       RTS   ; RTS ; ;READ/PLOT CURSOR POSITION ;
.E50A  B0 07    BCS $E513   ; PLOT   BCS PLOT10
.E50C  86 D6    STX $D6   ; STX    TBLX
.E50E  84 D3    STY $D3   ;...
