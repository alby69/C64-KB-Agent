---
id: src-f864-initiate-a-tape-write
type: source
title: 'Source Summary: initiate a tape write'
aliases:
- initiate a tape write
- f864-initiate-a-tape-write.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f864-initiate-a-tape-write.md
  sha256: 1b86618a949bedcc58c87fbe47b1e5de59793abf4f109a58756ea31835e0516c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: initiate a tape write

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f864-initiate-a-tape-write.md`
**SHA256**: `1b86618a949bedcc58c87fbe47b1e5de59793abf4f109a58756ea31835e0516c`

## Summary



# $F864 — initiate a tape write

## Disassemblatura
```assembly
.F864  20 D7 F7 JSR $F7D7   ; set tape buffer start and end pointers do tape write, 20 cycle count
.F867  A9 14    LDA #$14   ; set write lead cycle count
.F869  85 AB    STA $AB   ; save write lead cycle count do tape write, no cycle count set
.F86B  20 38 F8 JSR $F838   ; wait for PLAY/RECORD
.F86E  B0 6C    BCS $F8DC   ; if STOPped clear save IRQ address and exit
.F870  78       SEI   ; disable interrupts
.F871  A9 82    LDA #$...
