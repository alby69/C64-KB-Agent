---
title: flag the RS232 start bit and set the parity
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
- e4d3-rs232-patch
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $E4D3
  address_end: $E4D9
  symbol: flag-the-rs232-start-bit-and-set-the-parity
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E4D3**: save the start bit check flag, set start bit received'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E4D3**: RINONE, check for start bit'
---

# $E4D3 — flag the RS232 start bit and set the parity

## Disassemblatura
```assembly
.E4D3  85 A9    STA $A9   ; save the start bit check flag, set start bit received
.E4D5  A9 01    LDA #$01   ; set the initial parity state
.E4D7  85 AB    STA $AB   ; save the receiver parity bit
.E4D9  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E4D3**: save the start bit check flag, set start bit received
- **$E4D5**: set the initial parity state
- **$E4D7**: save the receiver parity bit

### Magnus Nyman (Magnus Nyman)
- **$E4D3**: RINONE, check for start bit
- **$E4D7**: RIPRTY, RS232 input parity

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*