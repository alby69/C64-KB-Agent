---
id: src-f4a5-load
type: source
title: 'Source Summary: load'
aliases:
- load
- f4a5-load.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f4a5-load.md
  sha256: 9bb7f60267114a82e24068af4c21920bac9a26f45d1f6cd359da5af76cd26e41
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: load

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f4a5-load.md`
**SHA256**: `9bb7f60267114a82e24068af4c21920bac9a26f45d1f6cd359da5af76cd26e41`

## Summary



# $F4A5 — load

## Disassemblatura
```assembly
.F4A5  85 93    STA $93   ; save load/verify flag
.F4A7  A9 00    LDA #$00   ; clear A
.F4A9  85 90    STA $90   ; clear the serial status byte
.F4AB  A5 BA    LDA $BA   ; get the device number
.F4AD  D0 03    BNE $F4B2   ; if not the keyboard continue do 'illegal device number'
.F4AF  4C 13 F7 JMP $F713   ; else do 'illegal device number' and return
.F4B2  C9 03    CMP #$03
.F4B4  F0 F9    BEQ $F4AF
.F4B6  90 7B    BCC $F533
.F4B8  A4 B7    LDY $...
