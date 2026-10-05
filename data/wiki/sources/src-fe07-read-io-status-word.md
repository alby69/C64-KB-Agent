---
id: src-fe07-read-io-status-word
type: source
title: 'Source Summary: read I/O status word'
aliases:
- read I/O status word
- fe07-read-io-status-word.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe07-read-io-status-word.md
  sha256: ab00925ec00e63a4a7a7a10901b02b7c7922c206ae08af17d7be91d46e8e8d8a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: read I/O status word

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fe07-read-io-status-word.md`
**SHA256**: `ab00925ec00e63a4a7a7a10901b02b7c7922c206ae08af17d7be91d46e8e8d8a`

## Summary



# $FE07 — read I/O status word

## Disassemblatura
```assembly
.FE07  A5 BA    LDA $BA   ; get the device number
.FE09  C9 02    CMP #$02   ; compare device with RS232 device
.FE0B  D0 0D    BNE $FE1A   ; if not RS232 device go ?? get RS232 device status
.FE0D  AD 97 02 LDA $0297   ; get the RS232 status register
.FE10  48       PHA   ; save the RS232 status value
.FE11  A9 00    LDA #$00   ; clear A
.FE13  8D 97 02 STA $0297   ; clear the RS232 status register
.FE16  68       PLA   ; restore ...
