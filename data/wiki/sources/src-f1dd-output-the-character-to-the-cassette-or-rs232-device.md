---
id: src-f1dd-output-the-character-to-the-cassette-or-rs232-device
type: source
title: 'Source Summary: output the character to the cassette or RS232 device'
aliases:
- output the character to the cassette or RS232 device
- f1dd-output-the-character-to-the-cassette-or-rs232-device.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f1dd-output-the-character-to-the-cassette-or-rs232-device.md
  sha256: def2accf2f6c6a8cee74c9c452f583ab6f3f7a31a8d7a36aa83c66c0b4e8542f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: output the character to the cassette or RS232 device

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f1dd-output-the-character-to-the-cassette-or-rs232-device.md`
**SHA256**: `def2accf2f6c6a8cee74c9c452f583ab6f3f7a31a8d7a36aa83c66c0b4e8542f`

## Summary



# $F1DD — output the character to the cassette or RS232 device

## Disassemblatura
```assembly
.F1DD  85 9E    STA $9E   ; save the character to the character buffer
.F1DF  8A       TXA   ; copy X
.F1E0  48       PHA   ; save X
.F1E1  98       TYA   ; copy Y
.F1E2  48       PHA   ; save Y
.F1E3  90 23    BCC $F208   ; if Cb is clear it must be the RS232 device output the character to the cassette
.F1E5  20 0D F8 JSR $F80D   ; bump the tape pointer
.F1E8  D0 0E    BNE $F1F8   ; if not end save ...
