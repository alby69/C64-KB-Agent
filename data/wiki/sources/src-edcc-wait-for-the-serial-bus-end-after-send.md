---
id: src-edcc-wait-for-the-serial-bus-end-after-send
type: source
title: 'Source Summary: wait for the serial bus end after send'
aliases:
- wait for the serial bus end after send
- edcc-wait-for-the-serial-bus-end-after-send.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/edcc-wait-for-the-serial-bus-end-after-send.md
  sha256: 7bebafed01b939388fe5f74a5762ec4c87f582e4046bc15b125551501a7098e6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: wait for the serial bus end after send

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/edcc-wait-for-the-serial-bus-end-after-send.md`
**SHA256**: `7bebafed01b939388fe5f74a5762ec4c87f582e4046bc15b125551501a7098e6`

## Summary



# $EDCC — wait for the serial bus end after send

## Disassemblatura
```assembly
.EDCC  78       SEI   ; disable the interrupts
.EDCD  20 A0 EE JSR $EEA0   ; set the serial data out low
.EDD0  20 BE ED JSR $EDBE   ; set serial ATN high
.EDD3  20 85 EE JSR $EE85   ; set the serial clock out high
.EDD6  20 A9 EE JSR $EEA9   ; get the serial data status in Cb
.EDD9  30 FB    BMI $EDD6   ; loop if the clock is high
.EDDB  58       CLI   ; enable the interrupts
.EDDC  60       RTS
```


## Commenti...
