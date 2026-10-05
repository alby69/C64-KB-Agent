---
id: src-ea31-irq-vector
type: source
title: 'Source Summary: IRQ vector'
aliases:
- IRQ vector
- ea31-irq-vector.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ea31-irq-vector.md
  sha256: 4cc51861fec841884f2041db964af82d47c40571f1fe9002c6c863055b4e6fd6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: IRQ vector

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ea31-irq-vector.md`
**SHA256**: `4cc51861fec841884f2041db964af82d47c40571f1fe9002c6c863055b4e6fd6`

## Summary



# $EA31 — IRQ vector

## Disassemblatura
```assembly
.EA31  20 EA FF JSR $FFEA   ; increment the real time clock
.EA34  A5 CC    LDA $CC   ; get the cursor enable, $00 = flash cursor
.EA36  D0 29    BNE $EA61   ; if flash not enabled skip the flash
.EA38  C6 CD    DEC $CD   ; decrement the cursor timing countdown
.EA3A  D0 25    BNE $EA61   ; if not counted out skip the flash
.EA3C  A9 14    LDA #$14   ; set the flash count
.EA3E  85 CD    STA $CD   ; save the cursor timing countdown
.EA40  A4...
