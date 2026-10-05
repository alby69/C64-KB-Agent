---
id: src-f1ad-get-from-serialrs232
type: source
title: 'Source Summary: GET FROM SERIAL/RS232'
aliases:
- GET FROM SERIAL/RS232
- f1ad-get-from-serialrs232.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f1ad-get-from-serialrs232.md
  sha256: 6df3b8feaad83be40f45525867b84d6dab594b1594242439c7655b80fe9bcdcc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: GET FROM SERIAL/RS232

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f1ad-get-from-serialrs232.md`
**SHA256**: `6df3b8feaad83be40f45525867b84d6dab594b1594242439c7655b80fe9bcdcc`

## Summary



# $F1AD — GET FROM SERIAL/RS232

## Disassemblatura
```assembly
.F1AD  A5 90    LDA $90   ; STATUS, I/O status word
.F1AF  F0 04    BEQ $F1B5   ; status OK
.F1B1  A9 0D    LDA #$0D   ; else return <CR> and exit
.F1B3  18       CLC
.F1B4  60       RTS
.F1B5  4C 13 EE JMP $EE13   ; ACPTR, get byte from serial bus
.F1B8  20 4E F1 JSR $F14E   ; receive from RS232
.F1BB  B0 F7    BCS $F1B4   ; end with carry set
.F1BD  C9 00    CMP #$00
.F1BF  D0 F2    BNE $F1B3   ; end with  carry clear
.F1C1  AD ...
