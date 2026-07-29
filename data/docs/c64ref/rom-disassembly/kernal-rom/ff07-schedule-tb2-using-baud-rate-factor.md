---
title: schedule TB2 using baud rate factor
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FF07
  address_end: $FF2D
  symbol: schedule-tb2-using-baud-rate-factor
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FF07**: LOW- und HIGH-Byte'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FF07**: M51AJB - non standard BPS time'
---

# $FF07 — schedule TB2 using baud rate factor

## Disassemblatura
```assembly
.FF07  AD 95 02 LDA $0295
.FF0A  8D 06 DD STA $DD06
.FF0D  AD 96 02 LDA $0296
.FF10  8D 07 DD STA $DD07
.FF13  A9 11    LDA #$11
.FF15  8D 0F DD STA $DD0F
.FF18  A9 12    LDA #$12
.FF1A  4D A1 02 EOR $02A1
.FF1D  8D A1 02 STA $02A1
.FF20  A9 FF    LDA #$FF
.FF22  8D 06 DD STA $DD06
.FF25  8D 07 DD STA $DD07
.FF28  AE 98 02 LDX $0298
.FF2B  86 A8    STX $A8
.FF2D  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$FF07**: LOW- und HIGH-Byte
- **$FF0A**: holen und in
- **$FF0D**: RS 232 Timerkonstanten für
- **$FF10**: Baudrate
- **$FF13**: Timer B starten
- **$FF15**: Control Register B
- **$FF18**: Bit 1 und 4 für Verknüpfung
- **$FF1A**: mit NMI-Flag für CIA 2
- **$FF1D**: Wert wieder speichern
- **$FF20**: höchsten Wert laden
- **$FF22**: und in Latch von
- **$FF25**: Timer B laden
- **$FF28**: Anzahl der zu sendenden Bits
- **$FF2B**: in Zähler für Wortlänge
- **$FF2D**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FF07**: M51AJB - non standard BPS time
- **$FF0A**: timer B low
- **$FF10**: timer B high
- **$FF15**: CIA#2 control register B
- **$FF1D**: ENABL, RS232 enables
- **$FF25**: timer B
- **$FF28**: BITNUM, number of bits still to send in this byte
- **$FF2B**: BITC1, RS232 bitcount

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*