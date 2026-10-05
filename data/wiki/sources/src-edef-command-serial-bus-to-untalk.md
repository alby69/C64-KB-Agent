---
id: src-edef-command-serial-bus-to-untalk
type: source
title: 'Source Summary: command serial bus to UNTALK'
aliases:
- command serial bus to UNTALK
- edef-command-serial-bus-to-untalk.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/edef-command-serial-bus-to-untalk.md
  sha256: 9750c18ca232e2307117e1ba2db438d64653b7f7c691a01e2be50039c6bdf74e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: command serial bus to UNTALK

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/edef-command-serial-bus-to-untalk.md`
**SHA256**: `9750c18ca232e2307117e1ba2db438d64653b7f7c691a01e2be50039c6bdf74e`

## Summary



# $EDEF — command serial bus to UNTALK

## Disassemblatura
```assembly
.EDEF  78       SEI   ; disable the interrupts
.EDF0  20 8E EE JSR $EE8E   ; set the serial clock out low
.EDF3  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EDF6  09 08    ORA #$08   ; mask xxxx 1xxx, set the serial ATN low
.EDF8  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.EDFB  A9 5F    LDA #$5F   ; set the UNTALK command
.EDFD  2C       .BYTE $2C   ; makes next line BIT...
