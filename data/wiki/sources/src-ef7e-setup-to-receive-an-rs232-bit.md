---
id: src-ef7e-setup-to-receive-an-rs232-bit
type: source
title: 'Source Summary: setup to receive an RS232 bit'
aliases:
- setup to receive an RS232 bit
- ef7e-setup-to-receive-an-rs232-bit.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ef7e-setup-to-receive-an-rs232-bit.md
  sha256: 3238b5134f8cd3328f9f9541154a1cd0c893debc74c3b49e8b66a121cba24057
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: setup to receive an RS232 bit

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ef7e-setup-to-receive-an-rs232-bit.md`
**SHA256**: `3238b5134f8cd3328f9f9541154a1cd0c893debc74c3b49e8b66a121cba24057`

## Summary



# $EF7E — setup to receive an RS232 bit

## Disassemblatura
```assembly
.EF7E  A9 90    LDA #$90   ; enable FLAG interrupt
.EF80  8D 0D DD STA $DD0D   ; save VIA 2 ICR
.EF83  0D A1 02 ORA $02A1   ; OR with the RS-232 interrupt enable byte
.EF86  8D A1 02 STA $02A1   ; save the RS-232 interrupt enable byte
.EF89  85 A9    STA $A9   ; set start bit check flag, set no start bit received
.EF8B  A9 02    LDA #$02   ; disable timer B interrupt
.EF8D  4C 3B EF JMP $EF3B   ; set VIA 2 ICR from A and r...
