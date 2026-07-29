---
title: get the serial data status in Cb
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
- eea9-carry-flag-holen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EEA9
  address_end: $EEB2
  symbol: get-the-serial-data-status-in-cb
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EEA9**: read VIA 2 DRA, serial port and video address'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EEA9**: Port A laden'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EEA9**: serial port I/O register'
---

# $EEA9 — get the serial data status in Cb

## Disassemblatura
```assembly
.EEA9  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EEAC  CD 00 DD CMP $DD00   ; compare it with itself
.EEAF  D0 F8    BNE $EEA9   ; if changing got try again
.EEB1  0A       ASL   ; shift the serial data into Cb
.EEB2  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EEA9**: read VIA 2 DRA, serial port and video address
- **$EEAC**: compare it with itself
- **$EEAF**: if changing got try again
- **$EEB1**: shift the serial data into Cb

### Commodore-64-intern-Buch (Commodore)
- **$EEA9**: Port A laden
- **$EEAC**: Änderung ?
- **$EEAF**: verzweige wenn ja
- **$EEB1**: Datenbit ins Carry schieben
- **$EEB2**: Rücksprung

### Magnus Nyman (Magnus Nyman)
- **$EEA9**: serial port I/O register
- **$EEAC**: compare
- **$EEAF**: wait for bus to settle
- **$EEB1**: shift data into carry, and CLK into bit 7

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*