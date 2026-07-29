---
title: set serial ATN high
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
- edbe-clear-atn
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $EDBE
  address_end: $EDC6
  symbol: set-serial-atn-high
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EDBE**: read VIA 2 DRA, serial port and video address'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EDBE**: serial bus I/O port'
---

# $EDBE — set serial ATN high

## Disassemblatura
```assembly
.EDBE  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EDC1  29 F7    AND #$F7   ; mask xxxx 0xxx, set serial ATN high
.EDC3  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.EDC6  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EDBE**: read VIA 2 DRA, serial port and video address
- **$EDC1**: mask xxxx 0xxx, set serial ATN high
- **$EDC3**: save VIA 2 DRA, serial port and video address

### Magnus Nyman (Magnus Nyman)
- **$EDBE**: serial bus I/O port
- **$EDC1**: clear bit4, ie. ATN 1
- **$EDC3**: store to port

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*