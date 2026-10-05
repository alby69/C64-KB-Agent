---
id: src-ef06-setup-next-rs232-tx-byte
type: source
title: 'Source Summary: setup next RS232 Tx byte'
aliases:
- setup next RS232 Tx byte
- ef06-setup-next-rs232-tx-byte.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ef06-setup-next-rs232-tx-byte.md
  sha256: 6890e6c9d835d4d62afcfe9e295e35dcce3f06a7820b605425160f3e3eaabbf7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: setup next RS232 Tx byte

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ef06-setup-next-rs232-tx-byte.md`
**SHA256**: `6890e6c9d835d4d62afcfe9e295e35dcce3f06a7820b605425160f3e3eaabbf7`

## Summary



# $EF06 — setup next RS232 Tx byte

## Disassemblatura
```assembly
.EF06  AD 94 02 LDA $0294   ; read the 6551 pseudo command register
.EF09  4A       LSR   ; handshake bit into Cb
.EF0A  90 07    BCC $EF13   ; if 3 line interface go ??
.EF0C  2C 01 DD BIT $DD01   ; test VIA 2 DRB, RS232 port
.EF0F  10 1D    BPL $EF2E   ; if DSR = 0 set DSR signal not present and exit
.EF11  50 1E    BVC $EF31   ; if CTS = 0 set CTS signal not present and exit was 3 line interface
.EF13  A9 00    LDA #$00   ; ...
