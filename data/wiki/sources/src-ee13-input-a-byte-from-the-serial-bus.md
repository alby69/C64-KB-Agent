---
id: src-ee13-input-a-byte-from-the-serial-bus
type: source
title: 'Source Summary: input a byte from the serial bus'
aliases:
- input a byte from the serial bus
- ee13-input-a-byte-from-the-serial-bus.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ee13-input-a-byte-from-the-serial-bus.md
  sha256: cd65a24662e62f4fbd1505a5c2a527877ce5c09f878d2509b872d22e8ed5b52f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: input a byte from the serial bus

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ee13-input-a-byte-from-the-serial-bus.md`
**SHA256**: `cd65a24662e62f4fbd1505a5c2a527877ce5c09f878d2509b872d22e8ed5b52f`

## Summary



# $EE13 — input a byte from the serial bus

## Disassemblatura
```assembly
.EE13  78       SEI   ; disable the interrupts
.EE14  A9 00    LDA #$00   ; set 0 bits to do, will flag EOI on timeout
.EE16  85 A5    STA $A5   ; save the serial bus bit count
.EE18  20 85 EE JSR $EE85   ; set the serial clock out high
.EE1B  20 A9 EE JSR $EEA9   ; get the serial data status in Cb
.EE1E  10 FB    BPL $EE1B   ; loop if the serial clock is low
.EE20  A9 01    LDA #$01   ; set the timeout count high byte
...
