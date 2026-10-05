---
id: src-ef59-rs232-rx-nmi
type: source
title: 'Source Summary: RS232 Rx NMI'
aliases:
- RS232 Rx NMI
- ef59-rs232-rx-nmi.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ef59-rs232-rx-nmi.md
  sha256: 5b01cbf26a827a56532c83998c59b0a4a9a49122dd6f02d76062329d25cf0e19
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: RS232 Rx NMI

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ef59-rs232-rx-nmi.md`
**SHA256**: `5b01cbf26a827a56532c83998c59b0a4a9a49122dd6f02d76062329d25cf0e19`

## Summary



# $EF59 — RS232 Rx NMI

## Disassemblatura
```assembly
.EF59  A6 A9    LDX $A9   ; get start bit check flag
.EF5B  D0 33    BNE $EF90   ; if no start bit received go ??
.EF5D  C6 A8    DEC $A8   ; decrement receiver bit count in
.EF5F  F0 36    BEQ $EF97   ; if the byte is complete go add it to the buffer
.EF61  30 0D    BMI $EF70
.EF63  A5 A7    LDA $A7   ; get the RS232 received data bit
.EF65  45 AB    EOR $AB   ; EOR with the receiver parity bit
.EF67  85 AB    STA $AB   ; save the receive...
