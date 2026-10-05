---
id: src-f483-initialise-rs232-output
type: source
title: 'Source Summary: initialise RS232 output'
aliases:
- initialise RS232 output
- f483-initialise-rs232-output.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f483-initialise-rs232-output.md
  sha256: 6e45ef89d339ebb3249a3e15aa3141231dd6a0329eb626c623e443102c04a719
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: initialise RS232 output

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f483-initialise-rs232-output.md`
**SHA256**: `6e45ef89d339ebb3249a3e15aa3141231dd6a0329eb626c623e443102c04a719`

## Summary



# $F483 — initialise RS232 output

## Disassemblatura
```assembly
.F483  A9 7F    LDA #$7F   ; disable all interrupts
.F485  8D 0D DD STA $DD0D   ; save VIA 2 ICR
.F488  A9 06    LDA #$06   ; set RS232 DTR output, RS232 RTS output
.F48A  8D 03 DD STA $DD03   ; save VIA 2 DDRB, RS232 port
.F48D  8D 01 DD STA $DD01   ; save VIA 2 DRB, RS232 port
.F490  A9 04    LDA #$04   ; mask xxxx x1xx, set RS232 Tx DATA high
.F492  0D 00 DD ORA $DD00   ; OR it with VIA 2 DRA, serial port and video address
.F...
