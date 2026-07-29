---
title: set the serial data out high
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
- ee97-data-auf-low-setzen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EE97
  address_end: $EE9F
  symbol: set-the-serial-data-out-high
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EE97**: read VIA 2 DRA, serial port and video address'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EE97**: Port A laden'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EE97**: serial bus I/O register'
---

# $EE97 — set the serial data out high

## Disassemblatura
```assembly
.EE97  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EE9A  29 DF    AND #$DF   ; mask xx0x xxxx, set serial data out high
.EE9C  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.EE9F  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EE97**: read VIA 2 DRA, serial port and video address
- **$EE9A**: mask xx0x xxxx, set serial data out high
- **$EE9C**: save VIA 2 DRA, serial port and video address

### Commodore-64-intern-Buch (Commodore)
- **$EE97**: Port A laden
- **$EE9A**: Bit 5 löschen
- **$EE9C**: und wieder speichern
- **$EE9F**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EE97**: serial bus I/O register
- **$EE9A**: clear bit5
- **$EE9C**: store

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*