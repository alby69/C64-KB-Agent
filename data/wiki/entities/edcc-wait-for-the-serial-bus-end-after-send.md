---
id: edcc-wait-for-the-serial-bus-end-after-send
type: entity
title: wait for the serial bus end after send
aliases:
- wait for the serial bus end after send
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/edcc-wait-for-the-serial-bus-end-after-send.md
  sha256: 7bebafed01b939388fe5f74a5762ec4c87f582e4046bc15b125551501a7098e6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-edcc-wait-for-the-serial-bus-end-after-send
---

# wait for the serial bus end after send



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


## Commenti

### Original Disassembly (—)
- **$EDCC**: disable the interrupts
- **$EDCD**: set the serial data out low
- **$EDD0**: set serial ATN high
- **$EDD3**: set the serial clock out high
- **$EDD6**: get the serial data status in Cb
- **$EDD9**: loop if the clock is high
- **$EDDB**: enable the interrupts

### Magnus Nyman (Magnus Nyman)
- **$EDCC**: disable interrupts
- **$EDCD**: set data 0
- **$EDD0**: set ATN 1
- **$EDD3**: set CLK 1
- **$EDD6**: read serial bus I/O port
- **$EDD9**: test bit6, and wait for CLK = 0
- **$EDDB**: enable interrupt

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-edcc-wait-for-the-serial-bus-end-after-send]]
