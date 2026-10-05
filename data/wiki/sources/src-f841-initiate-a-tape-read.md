---
id: src-f841-initiate-a-tape-read
type: source
title: 'Source Summary: initiate a tape read'
aliases:
- initiate a tape read
- f841-initiate-a-tape-read.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f841-initiate-a-tape-read.md
  sha256: e550dc7370901e64be4ecbb42c5fba0e2741a33b500a9f82813457d79e9b9af6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: initiate a tape read

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f841-initiate-a-tape-read.md`
**SHA256**: `e550dc7370901e64be4ecbb42c5fba0e2741a33b500a9f82813457d79e9b9af6`

## Summary



# $F841 — initiate a tape read

## Disassemblatura
```assembly
.F841  A9 00    LDA #$00   ; clear A
.F843  85 90    STA $90   ; clear serial status byte
.F845  85 93    STA $93   ; clear the load/verify flag
.F847  20 D7 F7 JSR $F7D7   ; set the tape buffer start and end pointers
.F84A  20 17 F8 JSR $F817   ; wait for PLAY
.F84D  B0 1F    BCS $F86E   ; exit if STOP was pressed, uses a further BCS at the target address to reach final target at $F8DC
.F84F  78       SEI   ; disable interrupts
.F...
