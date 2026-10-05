---
id: src-eed7-do-rs232-parity-bit-enters-with-rs232-bit-count-0
type: source
title: 'Source Summary: do RS232 parity bit, enters with RS232 bit count = 0'
aliases:
- do RS232 parity bit, enters with RS232 bit count = 0
- eed7-do-rs232-parity-bit-enters-with-rs232-bit-count-0.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/eed7-do-rs232-parity-bit-enters-with-rs232-bit-count-0.md
  sha256: 99afb076267701c80bae0d3fbee3a081a8a08c0cbae08f186fe9d7e704d35297
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: do RS232 parity bit, enters with RS232 bit count = 0

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/eed7-do-rs232-parity-bit-enters-with-rs232-bit-count-0.md`
**SHA256**: `99afb076267701c80bae0d3fbee3a081a8a08c0cbae08f186fe9d7e704d35297`

## Summary



# $EED7 — do RS232 parity bit, enters with RS232 bit count = 0

## Disassemblatura
```assembly
.EED7  A9 20    LDA #$20   ; mask 00x0 0000, parity enable bit
.EED9  2C 94 02 BIT $0294   ; test the pseudo 6551 command register
.EEDC  F0 14    BEQ $EEF2   ; if parity disabled go ??
.EEDE  30 1C    BMI $EEFC   ; if fixed mark or space parity go ??
.EEE0  70 14    BVS $EEF6   ; if even parity go ?? else odd parity
.EEE2  A5 BD    LDA $BD   ; get RS232 parity byte
.EEE4  D0 01    BNE $EEE7   ; if p...
