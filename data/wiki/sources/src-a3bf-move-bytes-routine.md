---
id: src-a3bf-move-bytes-routine
type: source
title: 'Source Summary: move bytes routine'
aliases:
- move bytes routine
- a3bf-move-bytes-routine.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a3bf-move-bytes-routine.md
  sha256: 7a338c11a3ed6f3f69245f94c61d614e3750e62387591af52f039842f92abed4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: move bytes routine

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a3bf-move-bytes-routine.md`
**SHA256**: `7a338c11a3ed6f3f69245f94c61d614e3750e62387591af52f039842f92abed4`

## Summary



# $A3BF — move bytes routine

## Disassemblatura
```assembly
.A3BF  38       SEC
.A3C0  A5 5A    LDA $5A
.A3C2  E5 5F    SBC $5F
.A3C4  85 22    STA $22
.A3C6  A8       TAY
.A3C7  A5 5B    LDA $5B
.A3C9  E5 60    SBC $60
.A3CB  AA       TAX
.A3CC  E8       INX
.A3CD  98       TYA
.A3CE  F0 23    BEQ $A3F3
.A3D0  A5 5A    LDA $5A
.A3D2  38       SEC
.A3D3  E5 22    SBC $22
.A3D5  85 5A    STA $5A
.A3D7  B0 03    BCS $A3DC
.A3D9  C6 5B    DEC $5B
.A3DB  38       SEC
.A3DC  A5 58    LDA $58
.A3DE...
