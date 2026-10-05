---
id: src-e8a1-test-for-line-decrement
type: source
title: 'Source Summary: test for line decrement'
aliases:
- test for line decrement
- e8a1-test-for-line-decrement.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e8a1-test-for-line-decrement.md
  sha256: 45c60248682dddf99e262d72b55ca617544842469a755cbc3ec419511f48df3f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: test for line decrement

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e8a1-test-for-line-decrement.md`
**SHA256**: `45c60248682dddf99e262d72b55ca617544842469a755cbc3ec419511f48df3f`

## Summary



# $E8A1 — test for line decrement

## Disassemblatura
```assembly
.E8A1  A2 02    LDX #$02   ; set the count
.E8A3  A9 00    LDA #$00   ; set the column
.E8A5  C5 D3    CMP $D3   ; compare the column with the cursor column
.E8A7  F0 07    BEQ $E8B0   ; if at the start of the line go decrement the cursor row and exit
.E8A9  18       CLC   ; else clear carry for add
.E8AA  69 28    ADC #$28   ; increment to next line
.E8AC  CA       DEX   ; decrement loop count
.E8AD  D0 F6    BNE $E8A5   ; loop...
