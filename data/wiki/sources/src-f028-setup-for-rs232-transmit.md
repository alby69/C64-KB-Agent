---
id: src-f028-setup-for-rs232-transmit
type: source
title: 'Source Summary: setup for RS232 transmit'
aliases:
- setup for RS232 transmit
- f028-setup-for-rs232-transmit.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f028-setup-for-rs232-transmit.md
  sha256: f463b5dda398e632e1f6ca2f68d356ca7deee8af709233cc4e8375eaec776c09
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: setup for RS232 transmit

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f028-setup-for-rs232-transmit.md`
**SHA256**: `f463b5dda398e632e1f6ca2f68d356ca7deee8af709233cc4e8375eaec776c09`

## Summary



# $F028 — setup for RS232 transmit

## Disassemblatura
```assembly
.F028  AD A1 02 LDA $02A1   ; get the RS-232 interrupt enable byte
.F02B  4A       LSR   ; shift the enable bit to Cb
.F02C  B0 1E    BCS $F04C   ; if interrupts are enabled just exit
.F02E  A9 10    LDA #$10   ; start timer A
.F030  8D 0E DD STA $DD0E   ; save VIA 2 CRA
.F033  AD 99 02 LDA $0299   ; get the baud rate bit time low byte
.F036  8D 04 DD STA $DD04   ; save VIA 2 timer A low byte
.F039  AD 9A 02 LDA $029A   ; get t...
