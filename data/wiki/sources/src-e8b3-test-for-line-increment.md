---
id: src-e8b3-test-for-line-increment
type: source
title: 'Source Summary: test for line increment'
aliases:
- test for line increment
- e8b3-test-for-line-increment.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e8b3-test-for-line-increment.md
  sha256: e419e26b99bec8192632266f825d8cb411cfd27c94ac0329c1c6afbd963aa6c0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: test for line increment

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e8b3-test-for-line-increment.md`
**SHA256**: `e419e26b99bec8192632266f825d8cb411cfd27c94ac0329c1c6afbd963aa6c0`

## Summary



# $E8B3 — test for line increment

## Disassemblatura
```assembly
.E8B3  A2 02    LDX #$02   ; set the count
.E8B5  A9 27    LDA #$27   ; set the column
.E8B7  C5 D3    CMP $D3   ; compare the column with the cursor column
.E8B9  F0 07    BEQ $E8C2   ; if at end of line test and possibly increment cursor row
.E8BB  18       CLC   ; else clear carry for add
.E8BC  69 28    ADC #$28   ; increment to the next line
.E8BE  CA       DEX   ; decrement the loop count
.E8BF  D0 F6    BNE $E8B7   ; loop...
