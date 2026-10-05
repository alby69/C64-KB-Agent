---
id: src-f086-get-byte-from-rs232-buffer
type: source
title: 'Source Summary: get byte from RS232 buffer'
aliases:
- get byte from RS232 buffer
- f086-get-byte-from-rs232-buffer.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f086-get-byte-from-rs232-buffer.md
  sha256: 9c8d3b0821f01ac6de39750a41725bc3f890fe1d678445e5a985d07c1bcc97f6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: get byte from RS232 buffer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f086-get-byte-from-rs232-buffer.md`
**SHA256**: `9c8d3b0821f01ac6de39750a41725bc3f890fe1d678445e5a985d07c1bcc97f6`

## Summary



# $F086 — get byte from RS232 buffer

## Disassemblatura
```assembly
.F086  AD 97 02 LDA $0297   ; get the RS232 status register
.F089  AC 9C 02 LDY $029C   ; get index to Rx buffer start
.F08C  CC 9B 02 CPY $029B   ; compare with index to Rx buffer end
.F08F  F0 0B    BEQ $F09C   ; return null if buffer empty
.F091  29 F7    AND #$F7   ; clear the Rx buffer empty bit
.F093  8D 97 02 STA $0297   ; save the RS232 status register
.F096  B1 F7    LDA ($F7),Y   ; get byte from Rx buffer
.F098  EE ...
