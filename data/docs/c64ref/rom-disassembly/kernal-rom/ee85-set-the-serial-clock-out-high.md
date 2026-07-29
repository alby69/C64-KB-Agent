---
title: set the serial clock out high
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
- ee85-clock-auf-low-setzen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EE85
  address_end: $EE8D
  symbol: set-the-serial-clock-out-high
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EE85**: read VIA 2 DRA, serial port and video address'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EE85**: Port A laden'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EE85**: serial port I/O register'
---

# $EE85 — set the serial clock out high

## Disassemblatura
```assembly
.EE85  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EE88  29 EF    AND #$EF   ; mask xxx0 xxxx, set serial clock out high
.EE8A  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.EE8D  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EE85**: read VIA 2 DRA, serial port and video address
- **$EE88**: mask xxx0 xxxx, set serial clock out high
- **$EE8A**: save VIA 2 DRA, serial port and video address

### Commodore-64-intern-Buch (Commodore)
- **$EE85**: Port A laden
- **$EE88**: Bit 4 löschen
- **$EE8A**: und wieder speichern
- **$EE8D**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EE85**: serial port I/O register
- **$EE88**: clear bit4, ie. CLK out =1
- **$EE8A**: store

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*