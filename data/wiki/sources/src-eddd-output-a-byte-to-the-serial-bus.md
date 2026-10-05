---
id: src-eddd-output-a-byte-to-the-serial-bus
type: source
title: 'Source Summary: output a byte to the serial bus'
aliases:
- output a byte to the serial bus
- eddd-output-a-byte-to-the-serial-bus.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/eddd-output-a-byte-to-the-serial-bus.md
  sha256: 5127efd6754be0b529d6ea52e5ee6f9bdf4dd87ed9ae2902be1765e2d5e7a405
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: output a byte to the serial bus

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/eddd-output-a-byte-to-the-serial-bus.md`
**SHA256**: `5127efd6754be0b529d6ea52e5ee6f9bdf4dd87ed9ae2902be1765e2d5e7a405`

## Summary



# $EDDD — output a byte to the serial bus

## Disassemblatura
```assembly
.EDDD  24 94    BIT $94   ; test the deferred character flag
.EDDF  30 05    BMI $EDE6   ; if there is a deferred character go send it
.EDE1  38       SEC   ; set carry
.EDE2  66 94    ROR $94   ; shift into the deferred character flag
.EDE4  D0 05    BNE $EDEB   ; save the byte and exit, branch always
.EDE6  48       PHA   ; save the byte
.EDE7  20 40 ED JSR $ED40   ; Tx byte on serial bus
.EDEA  68       PLA   ; restor...
