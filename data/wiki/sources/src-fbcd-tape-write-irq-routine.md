---
id: src-fbcd-tape-write-irq-routine
type: source
title: 'Source Summary: tape write IRQ routine'
aliases:
- tape write IRQ routine
- fbcd-tape-write-irq-routine.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fbcd-tape-write-irq-routine.md
  sha256: 9f4829cafee598d01deae74520ae1394d2b54777f221577f75643e437719a6ae
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: tape write IRQ routine

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fbcd-tape-write-irq-routine.md`
**SHA256**: `9f4829cafee598d01deae74520ae1394d2b54777f221577f75643e437719a6ae`

## Summary



# $FBCD — tape write IRQ routine

## Disassemblatura
```assembly
.FBCD  A5 A8    LDA $A8   ; get start bit first cycle done flag
.FBCF  D0 12    BNE $FBE3   ; if first cycle done go do rest of byte each byte sent starts with two half cycles of $0110 system clocks and the whole block ends with two more such half cycles
.FBD1  A9 10    LDA #$10   ; set first start cycle time constant low byte
.FBD3  A2 01    LDX #$01   ; set first start cycle time constant high byte
.FBD5  20 B1 FB JSR $FBB1   ;...
