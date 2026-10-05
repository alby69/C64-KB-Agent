---
id: src-e544-clear-the-screen
type: source
title: 'Source Summary: clear the screen'
aliases:
- clear the screen
- e544-clear-the-screen.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e544-clear-the-screen.md
  sha256: 107670732f760a9915f640082ac0e369c159dc6a72145a93c28b09da5b2ae2bd
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: clear the screen

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e544-clear-the-screen.md`
**SHA256**: `107670732f760a9915f640082ac0e369c159dc6a72145a93c28b09da5b2ae2bd`

## Summary



# $E544 — clear the screen

## Disassemblatura
```assembly
.E544  AD 88 02 LDA $0288   ; get the screen memory page
.E547  09 80    ORA #$80   ; set the high bit, flag every line is a logical line start
.E549  A8       TAY   ; copy to Y
.E54A  A9 00    LDA #$00   ; clear the line start low byte
.E54C  AA       TAX   ; clear the index
.E54D  94 D9    STY $D9,X   ; save the start of line X pointer high byte
.E54F  18       CLC   ; clear carry for add
.E550  69 28    ADC #$28   ; add the line len...
