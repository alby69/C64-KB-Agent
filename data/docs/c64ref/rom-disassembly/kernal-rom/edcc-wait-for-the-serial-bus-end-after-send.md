---
title: wait for the serial bus end after send
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- edcc-wait-for-clock
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $EDCC
  address_end: $EDDC
  symbol: wait-for-the-serial-bus-end-after-send
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EDCC**: disable the interrupts'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EDCC**: disable interrupts'
---

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