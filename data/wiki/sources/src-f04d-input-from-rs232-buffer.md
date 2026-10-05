---
id: src-f04d-input-from-rs232-buffer
type: source
title: 'Source Summary: input from RS232 buffer'
aliases:
- input from RS232 buffer
- f04d-input-from-rs232-buffer.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f04d-input-from-rs232-buffer.md
  sha256: 27ddf15eee6d44c55445338314ff3cbb9f515188e3f7efa139d93ca29595290a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: input from RS232 buffer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f04d-input-from-rs232-buffer.md`
**SHA256**: `27ddf15eee6d44c55445338314ff3cbb9f515188e3f7efa139d93ca29595290a`

## Summary



# $F04D — input from RS232 buffer

## Disassemblatura
```assembly
.F04D  85 99    STA $99   ; save the input device number
.F04F  AD 94 02 LDA $0294   ; get pseudo 6551 command register
.F052  4A       LSR   ; shift the handshake bit to Cb
.F053  90 28    BCC $F07D   ; if 3 line interface go ??
.F055  29 08    AND #$08   ; mask the duplex bit, pseudo 6551 command is >> 1
.F057  F0 24    BEQ $F07D   ; if full duplex go ??
.F059  A9 02    LDA #$02   ; mask 0000 00x0, RTS out
.F05B  2C 01 DD BIT ...
