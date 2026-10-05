---
id: src-f533
type: source
title: 'Source Summary: ??'
aliases:
- ??
- f533.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f533.md
  sha256: 2950a18ad673bab26cf0a86c71aa94d969c33e2aa1b45089b33867cbdc2f38fe
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ??

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f533.md`
**SHA256**: `2950a18ad673bab26cf0a86c71aa94d969c33e2aa1b45089b33867cbdc2f38fe`

## Summary



# $F533 — ??

## Disassemblatura
```assembly
.F533  4A       LSR
.F534  B0 03    BCS $F539
.F536  4C 13 F7 JMP $F713   ; else do 'illegal device number' and return
.F539  20 D0 F7 JSR $F7D0   ; get tape buffer start pointer in XY
.F53C  B0 03    BCS $F541   ; if ??
.F53E  4C 13 F7 JMP $F713   ; else do 'illegal device number' and return
.F541  20 17 F8 JSR $F817   ; wait for PLAY
.F544  B0 68    BCS $F5AE   ; exit if STOP was pressed
.F546  20 AF F5 JSR $F5AF   ; print "Searching..."
.F549  A5...
