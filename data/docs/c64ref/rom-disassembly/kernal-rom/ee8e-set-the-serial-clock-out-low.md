---
title: set the serial clock out low
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
- ee8e-clock-auf-high-setzen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EE8E
  address_end: $EE96
  symbol: set-the-serial-clock-out-low
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EE8E**: read VIA 2 DRA, serial port and video address'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EE8E**: Port A laden'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EE8E**: serial port I/O register'
---

# $EE8E — set the serial clock out low

## Disassemblatura
```assembly
.EE8E  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EE91  09 10    ORA #$10   ; mask xxx1 xxxx, set serial clock out low
.EE93  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.EE96  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EE8E**: read VIA 2 DRA, serial port and video address
- **$EE91**: mask xxx1 xxxx, set serial clock out low
- **$EE93**: save VIA 2 DRA, serial port and video address

### Commodore-64-intern-Buch (Commodore)
- **$EE8E**: Port A laden
- **$EE91**: Bit 4 setzen
- **$EE93**: und wieder speichern
- **$EE96**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EE8E**: serial port I/O register
- **$EE91**: set bit4, ie. CLK out =0
- **$EE93**: store

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*