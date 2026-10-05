---
id: src-ed40-tx-byte-on-serial-bus
type: source
title: 'Source Summary: Tx byte on serial bus'
aliases:
- Tx byte on serial bus
- ed40-tx-byte-on-serial-bus.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ed40-tx-byte-on-serial-bus.md
  sha256: 19433da7355237bc420ae9e9237d260ee6f987a5af9c4b39a2fec1dad71c9e68
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Tx byte on serial bus

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ed40-tx-byte-on-serial-bus.md`
**SHA256**: `19433da7355237bc420ae9e9237d260ee6f987a5af9c4b39a2fec1dad71c9e68`

## Summary



# $ED40 — Tx byte on serial bus

## Disassemblatura
```assembly
.ED40  78       SEI   ; disable the interrupts
.ED41  20 97 EE JSR $EE97   ; set the serial data out high
.ED44  20 A9 EE JSR $EEA9   ; get the serial data status in Cb
.ED47  B0 64    BCS $EDAD   ; if the serial data is high go do 'device not present'
.ED49  20 85 EE JSR $EE85   ; set the serial clock out high
.ED4C  24 A3    BIT $A3   ; test the EOI flag
.ED4E  10 0A    BPL $ED5A   ; if not EOI go ?? I think this is the EOI sequ...
