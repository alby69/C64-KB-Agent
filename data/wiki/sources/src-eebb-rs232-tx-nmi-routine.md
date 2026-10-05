---
id: src-eebb-rs232-tx-nmi-routine
type: source
title: 'Source Summary: RS232 Tx NMI routine'
aliases:
- RS232 Tx NMI routine
- eebb-rs232-tx-nmi-routine.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/eebb-rs232-tx-nmi-routine.md
  sha256: 9a6d715e5b58a0b63900cc392d0db91ab6cca297ff9960b4387e9d6f356e32c4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: RS232 Tx NMI routine

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/eebb-rs232-tx-nmi-routine.md`
**SHA256**: `9a6d715e5b58a0b63900cc392d0db91ab6cca297ff9960b4387e9d6f356e32c4`

## Summary



# $EEBB — RS232 Tx NMI routine

## Disassemblatura
```assembly
.EEBB  A5 B4    LDA $B4   ; get RS232 bit count
.EEBD  F0 47    BEQ $EF06   ; if zero go setup next RS232 Tx byte and return
.EEBF  30 3F    BMI $EF00   ; if -ve go do stop bit(s) else bit count is non zero and +ve
.EEC1  46 B6    LSR $B6   ; shift RS232 output byte buffer
.EEC3  A2 00    LDX #$00   ; set $00 for bit = 0
.EEC5  90 01    BCC $EEC8   ; branch if bit was 0
.EEC7  CA       DEX   ; set $FF for bit = 1
.EEC8  8A       TX...
