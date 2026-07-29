---
title: set the serial data out low
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- eea0-data-auf-high-setzen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EEA0
  address_end: $EEA8
  symbol: set-the-serial-data-out-low
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EEA0**: read VIA 2 DRA, serial port and video address'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EEA0**: Port A laden'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EEA0**: serial bus I/O resister'
---

# $EEA0 — set the serial data out low

## Disassemblatura
```assembly
.EEA0  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EEA3  09 20    ORA #$20   ; mask xx1x xxxx, set serial data out low
.EEA5  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.EEA8  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EEA0**: read VIA 2 DRA, serial port and video address
- **$EEA3**: mask xx1x xxxx, set serial data out low
- **$EEA5**: save VIA 2 DRA, serial port and video address

### Commodore-64-intern-Buch (Commodore)
- **$EEA0**: Port A laden
- **$EEA3**: Bit 5 setzen
- **$EEA5**: und wieder speichern
- **$EEA8**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EEA0**: serial bus I/O resister
- **$EEA3**: set bit 5
- **$EEA5**: store

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*