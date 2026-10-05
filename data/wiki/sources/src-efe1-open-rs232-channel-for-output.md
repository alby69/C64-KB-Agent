---
id: src-efe1-open-rs232-channel-for-output
type: source
title: 'Source Summary: open RS232 channel for output'
aliases:
- open RS232 channel for output
- efe1-open-rs232-channel-for-output.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/efe1-open-rs232-channel-for-output.md
  sha256: 6441c4cd2763020f5f213661fae6435f54ce9cfd89c308d0c9ddcf093eff0409
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: open RS232 channel for output

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/efe1-open-rs232-channel-for-output.md`
**SHA256**: `6441c4cd2763020f5f213661fae6435f54ce9cfd89c308d0c9ddcf093eff0409`

## Summary



# $EFE1 — open RS232 channel for output

## Disassemblatura
```assembly
.EFE1  85 9A    STA $9A   ; save the output device number
.EFE3  AD 94 02 LDA $0294   ; read the pseudo 6551 command register
.EFE6  4A       LSR   ; shift handshake bit to carry
.EFE7  90 29    BCC $F012   ; if 3 line interface go ??
.EFE9  A9 02    LDA #$02   ; mask 0000 00x0, RTS out
.EFEB  2C 01 DD BIT $DD01   ; test VIA 2 DRB, RS232 port
.EFEE  10 1D    BPL $F00D   ; if DSR = 0 set DSR not present and exit
.EFF0  D0 2...
