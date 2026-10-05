---
id: src-f3d5-send-secondary-address-and-filename
type: source
title: 'Source Summary: send secondary address and filename'
aliases:
- send secondary address and filename
- f3d5-send-secondary-address-and-filename.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f3d5-send-secondary-address-and-filename.md
  sha256: 154fcd4cb0cc9d25de41022ce254df68b5d574510bc7cec2c4972b1a06c22ea6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: send secondary address and filename

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f3d5-send-secondary-address-and-filename.md`
**SHA256**: `154fcd4cb0cc9d25de41022ce254df68b5d574510bc7cec2c4972b1a06c22ea6`

## Summary



# $F3D5 — send secondary address and filename

## Disassemblatura
```assembly
.F3D5  A5 B9    LDA $B9   ; get the secondary address
.F3D7  30 FA    BMI $F3D3   ; ok exit if -ve
.F3D9  A4 B7    LDY $B7   ; get file name length
.F3DB  F0 F6    BEQ $F3D3   ; ok exit if null
.F3DD  A9 00    LDA #$00   ; clear A
.F3DF  85 90    STA $90   ; clear the serial status byte
.F3E1  A5 BA    LDA $BA   ; get the device number
.F3E3  20 0C ED JSR $ED0C   ; command devices on the serial bus to LISTEN
.F3E6  A...
